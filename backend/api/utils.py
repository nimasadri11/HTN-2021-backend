#Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-custom-labels-developer-guide/blob/master/LICENSE-SAMPLECODE.)

from itertools import groupby
import boto3
import io
from PIL import Image, ImageDraw, ExifTags, ImageColor, ImageFont
import cv2
import sys

def get_image():
    camera = cv2.VideoCapture(0)
    for i in range(10):
        temp = camera.read()
    retval, im = camera.read()
    return_value, image = camera.read()
    cv2.imshow('image', image)
    #cv2.waitKey(1000)
    _, image = cv2.imencode('.png', image)
    image = image.tobytes()
    camera.release()
    return image


def display_image(response,img):
    
    image = Image.open(io.BytesIO(img))

    # Ready image to draw bounding boxes on it.
    imgWidth, imgHeight = image.size
    draw = ImageDraw.Draw(image)

    # calculate and display bounding boxes for each detected custom label
    print(response)
    print('Detected custom labels')
    for customLabel in response['CustomLabels']:
        print('Label ' + str(customLabel['Name']))
        print('Confidence ' + str(customLabel['Confidence']))
        if 'Geometry' in customLabel:
            box = customLabel['Geometry']['BoundingBox']
            left = imgWidth * box['Left']
            top = imgHeight * box['Top']
            width = imgWidth * box['Width']
            height = imgHeight * box['Height']

            fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 10)
            draw.text((left,top), customLabel['Name'], fill='#00d400', font=fnt)

            print('Left: ' + '{0:.0f}'.format(left))
            print('Top: ' + '{0:.0f}'.format(top))
            print('Label Width: ' + "{0:.0f}".format(width))
            print('Label Height: ' + "{0:.0f}".format(height))

            points = (
                (left,top),
                (left + width, top),
                (left + width, top + height),
                (left , top + height),
                (left, top))
            draw.line(points, fill='#00d400', width=5)
    print("SHOWING IMAGE")
    image.show()

def show_custom_labels(model, min_confidence):
    client=boto3.client('rekognition')
    #image = open("img5.jpg", "rb")
    #img = image.read()
    img = get_image()

    #Call DetectCustomLabels
    response = client.detect_custom_labels(
        #Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        Image={'Bytes': img},
        MinConfidence=min_confidence,
        ProjectVersionArn=model)
    #image.close()
    r = list(map(lambda x: x['Name'], response['CustomLabels']))
    results = {value: len(list(freq)) for value, freq in groupby(sorted(r))}
    # For object detection use case, uncomment below code to display image.
    display_image(response,img)
    return results

def capture():
    model='arn:aws:rekognition:us-east-1:039418442864:project/htn-store-2/version/htn-store-2.2021-09-17T20.55.32/1631926532256'
    min_confidence=80
    res = show_custom_labels(model, min_confidence)
    print(res)
    cv2.destroyAllWindows()
    return res

def main():

    capture()


if __name__ == "__main__":
    main()

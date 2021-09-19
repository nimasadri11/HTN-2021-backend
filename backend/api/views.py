from backend.api import models
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .utils import capture
from .models import *
# from avybe_api.api.models import Ballot, BookedCall, Call, User
# import avybe_api.api.serializers as serializers
# import boto3
# from django.forms.models import model_to_dict
# from rest_framework import generics, filters, status
# from rest_framework import pagination
# from datetime import datetime
# from django.db.models import Max


class Root(APIView):
    def get(self, request):
        
        
        return Response({})


class Capture(APIView):
    def get(self, request):
        res = capture()
        return Response(res)

class Update(APIView):
    def post(self, request):
        bought = {}
        c = 0
        t = 0
        for k,v in request.data.items():
            p = Product.objects.get(title = k)
            bought[k] = p.count - int(v)
            print(k)
            print("OLD: ", p.count)
            print("NEW: ", v)
            p.count = v
            p.save()

            c += p.price * bought[k]
            t += round(float(c) * float(1.13),2)
            
            

            
        print(bought)
        return Response({"Your total is": t})
        return Response(bought)
        
        
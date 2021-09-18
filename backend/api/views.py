from backend.api import models
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .utils import capture
from models import *
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
        request.data
        for k,v in request.data.items():
            p = Product.objects.get(title = k)
            p.count = v
            p.save()
        
        
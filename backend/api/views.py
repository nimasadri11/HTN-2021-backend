from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
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

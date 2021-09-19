from itertools import product
from backend.api import models
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .utils import *
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

class Checkout(APIView):
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
        
class StartShoping(APIView):
    def post(self, request):
        res = capture()
        send_to_firestore({'orange': 0, 'coke': 0, 'cup': 0})
        Product.objects.all().update(count = 0)
        for k,v in res.items():
            p = Product.objects.get(title = k)
            p.count = v
            p.save()
            print(p)
        return Response(res)

class GetCart(APIView):
    def post(self, request):
        data = request.data.dict()
        print(type(data))
        print(data)
        data.setdefault('orange', 0)
        data.setdefault('coke', 0)
        data.setdefault('cup', 0)
        # print(list(data.values()))
        cart = {}
        for k,v in data.items():
            print(k)
            print(v)
            p = Product.objects.get(title = k)
            cart[k] = p.count - int(v)
            p.cart_count = cart[k]
            p.save()
        
        return Response(cart)
            

class Inventory(APIView):
    def get(self, request):
        ps = Product.objects.all()
        res = {}
        for prod in ps:
            av = prod.count - prod.cart_count
            res[prod.title] = av
        return Response(res)

            

        
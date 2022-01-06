from django.http.response import JsonResponse
from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse, request
from rest_framework.fields import JSONField
from worker.models import WorkerDetails
from worker.serializers import WorkerDetailsSerializer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import generics
import psycopg2
from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings

# Create your views here.
# def detail(request,id):
#     owner_obj = WorkerDetails.objects.get(id=id)
#     return HttpResponse(owner_obj.createdOn)
# conn = psycopg2.connect(
#    database="d3jin5mrtffce1", user='cpackgtbjygfgf', password='7868590ae7a9a8c781be508c9f3c97a01bdd008c047a541acf3917018d3083ed', host='ec2-54-173-2-216.compute-1.amazonaws.com', port= '5432'
# )
# #Setting auto commit false
# conn.autocommit = True


# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()


@csrf_exempt
def worker_list(request):
    if request.method == 'GET':
        worker_data = JSONParser().parse(request)
        id = worker_data['id']
        worker = WorkerDetails.objects.raw('SELECT * FROM worker_workerdetails WHERE id =  %s',[id])
        # print(customers['password'])
        
        # base64 decode

        worker_serializer = WorkerDetailsSerializer(worker, many=True)
        
        #decrypt the password 
        # txt = base64.urlsafe_b64decode(worker_serializer.data[0]['password'])
        # cipher_suite = Fernet(settings.ENCRYPT_KEY)
        # decrypt_text = cipher_suite.decrypt(txt).decode("ascii")
        # worker_serializer.data[0]['password'] = cipher_suite.decrypt(txt).decode("ascii")
        return JsonResponse(worker_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        worker_data = JSONParser().parse(request)

        #password encryption
        password = str(worker_data['password'])
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        encrypted_text = cipher_suite.encrypt(password.encode('ascii'))
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii") 
        worker_data['password'] = encrypted_text

        customer_serializer = WorkerDetailsSerializer(data=worker_data)
        if customer_serializer.is_valid():
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt 
# def customer_detail(request, pk):
#     try: 
#         customer = Customer.objects.get(pk=pk) 
#     except Customer.DoesNotExist: 
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND) 
 
#     if request.method == 'GET': 
#         customer_serializer = CustomerSerializer(customer) 
#         return JsonResponse(customer_serializer.data) 
 
#     elif request.method == 'PUT': 
#         customer_data = JSONParser().parse(request) 
#         customer_serializer = CustomerSerializer(customer, data=customer_data) 
#         if customer_serializer.is_valid(): 
#             customer_serializer.save() 
#             return JsonResponse(customer_serializer.data) 
#         return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
#     elif request.method == 'DELETE': 
#         customer.delete() 
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)



## For worker authentication
@csrf_exempt
def worker_authentication(request):
    if request.method == 'GET':
        worker_data = JSONParser().parse(request)
        user = worker_data['username']
        worker = WorkerDetails.objects.raw('SELECT * FROM worker_workerdetails WHERE username =  %s',[user])
        if(worker):
            worker_serializer = WorkerDetailsSerializer(worker, many=True)
            
            #decrypt the password 
            txt = base64.urlsafe_b64decode(worker_serializer.data[0]['password'])
            cipher_suite = Fernet(settings.ENCRYPT_KEY)
            decrypt_text = cipher_suite.decrypt(txt).decode("ascii")
            if(worker_data['password'] == decrypt_text):
                return JsonResponse(worker_serializer.data[0]['id'], safe=False)
            return JsonResponse({"data":'false'})
        return JsonResponse({"data":'false'})
        # return JsonResponse(worker_serializer.data, safe=False)

        # In order to serialize objects, we must set 'safe=False'
    elif request.method == 'POST':
        worker_data = JSONParser().parse(request)
        user = worker_data['username']
        #password encryption
        password = str(worker_data['password'])
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        encrypted_text = cipher_suite.encrypt(password.encode('ascii'))
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii") 
        worker_data['password'] = encrypted_text

        customer_serializer = WorkerDetailsSerializer(data=worker_data)
        if customer_serializer.is_valid():
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    




@csrf_exempt
def worker_authenticate(request):
    if request.method == 'GET':
        worker = WorkerDetails.objects.raw('SELECT * FROM worker_workerdetails')
        # print(customers['password'])
        
        # base64 decode

        worker_serializer = WorkerDetailsSerializer(worker, many=True)
        
        #decrypt the password 
        txt = base64.urlsafe_b64decode(worker_serializer.data[0]['password'])
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        decrypt_text = cipher_suite.decrypt(txt).decode("ascii")
        # worker_serializer.data[0]['password'] = cipher_suite.decrypt(txt).decode("ascii")
        print(decrypt_text)

        return JsonResponse(worker_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'
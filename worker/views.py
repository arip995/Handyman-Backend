from re import T
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



# @csrf_exempt
@api_view(['GET', 'POST'])
def worker_list(request):
    if request.method == 'GET':
        worker = WorkerDetails.objects.all()
        worker_serializer = WorkerDetailsSerializer(worker,many=True)
        # if worker_serializer.is_valid():
        return Response(worker_serializer.data)
        
        # In order to serialize objects, we must set 'safe=False'


## For worker authentication
@api_view(['GET', 'POST'])
def worker_authentication(request):
    if request.method == 'GET':
        user = request.data['username']
        worker = WorkerDetails.objects.raw('SELECT * FROM worker_workerdetails WHERE username =  %s',[user])
        if(worker):
            worker_serializer = WorkerDetailsSerializer(worker, many=True)
            
            #decrypt the password 
            txt = base64.urlsafe_b64decode(worker_serializer.data[0]['password'])
            cipher_suite = Fernet(settings.ENCRYPT_KEY)
            decrypt_text = cipher_suite.decrypt(txt).decode("ascii")
            if(request.data['password'] == decrypt_text):
                return Response(worker_serializer.data[0]['id'])
            return Response({"data":'false'})
        return Response({"data":'false'})
        # return JsonResponse(worker_serializer.data)

        # In order to serialize objects, we must set'
    elif request.method == 'POST':
        user = request.data['username']
        #password encryption
        password = str(request.data['password'])
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        encrypted_text = cipher_suite.encrypt(password.encode('ascii'))
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii") 
        request.data['password'] = encrypted_text


        ##Create access token with some salt
        accessToken = str(request.data['password']+str(request.data['username'])+str(request.data['mobileNumber']))
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        encrypted_text = cipher_suite.encrypt(accessToken.encode('ascii'))
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
        request.data['accessToken'] = encrypted_text

        customer_serializer = WorkerDetailsSerializer(data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    




# @csrf_exempt
@api_view(['GET', 'POST'])
def worker_authenticate(request):
    if request.method == 'POST':
        user = request.data['username']
        worker = WorkerDetails.objects.raw('SELECT * FROM worker_workerdetails WHERE username =  %s',[user])
        if(worker):
            worker_serializer = WorkerDetailsSerializer(worker, many=True)
            
            #decrypt the password 
            txt = base64.urlsafe_b64decode(worker_serializer.data[0]['password'])
            cipher_suite = Fernet(settings.ENCRYPT_KEY)
            decrypt_text = cipher_suite.decrypt(txt).decode("ascii")
            if(request.data['password'] == decrypt_text):
                data = {
                "id"             :worker_serializer.data[0]['id'],
                "firstName"      :worker_serializer.data[0]['firstName'],
                "lastName"      :worker_serializer.data[0]['lastName'],
                "username"       :worker_serializer.data[0]['username'],
                "worktype"       :worker_serializer.data[0]['worktype'],
                "isActivated"    :worker_serializer.data[0]['isActivated'],
                "createdOn"      :worker_serializer.data[0]['createdOn'],
                "accessToken"    :worker_serializer.data[0]['accessToken']
            }
                return JsonResponse(data)
            return JsonResponse({"error":'Invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
        # return Response({"data":'false'})
        # return JsonResponse(worker_serializer.data)




@api_view(['GET', 'POST'])
def worker_authenticateaccesstoken(request):
    if request.method == 'POST':
        user = request.data['accessToken']
        worker = WorkerDetails.objects.raw('SELECT * FROM worker_workerdetails WHERE "accessToken" =  %s',[user])
        if(worker):
            worker_serializer = WorkerDetailsSerializer(worker, many=True)
            data = {
                "id"             :worker_serializer.data[0]['id'],
                "firstName"      :worker_serializer.data[0]['firstName'],
                "lastName"      :worker_serializer.data[0]['lastName'],
                "username"       :worker_serializer.data[0]['username'],
                "worktype"       :worker_serializer.data[0]['worktype'],
                "isActivated"    :worker_serializer.data[0]['isActivated'],
                "createdOn"      :worker_serializer.data[0]['createdOn'],
                "accessToken"    :worker_serializer.data[0]['accessToken']
            }
            return JsonResponse(data)
        return JsonResponse({"error":'Invalid credentials. Please Sign in'},status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'GET':
    #     print(accesstoken)
    #     user = accesstoken
    #     worker = WorkerDetails.objects.raw('SELECT * FROM worker_workerdetails WHERE "accessToken" =  %s',[user])
    #     if(worker):
    #         worker_serializer = WorkerDetailsSerializer(worker, many=True)
    #         data = {
    #             "id"             :worker_serializer.data[0]['id'],
    #             "firstName"      :worker_serializer.data[0]['firstName'],
    #             "lastName"      :worker_serializer.data[0]['lastName'],
    #             "username"       :worker_serializer.data[0]['username'],
    #             "worktype"       :worker_serializer.data[0]['worktype'],
    #             "isActivated"    :worker_serializer.data[0]['isActivated'],
    #             "createdOn"      :worker_serializer.data[0]['createdOn'],
    #             "accessToken"    :worker_serializer.data[0]['accessToken']
    #         }
    #         return JsonResponse(data)
    #     return JsonResponse({"error":'Invalid credentials. Please Sign in'},status=status.HTTP_400_BAD_REQUEST)

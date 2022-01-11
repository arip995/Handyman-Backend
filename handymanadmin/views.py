from django.shortcuts import render
from handymanadmin.serializers import HandymanAdminDetailsSerializer
from handymanadmin.models import HandymanAdminDetails
from django.http.response import JsonResponse
from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse, request
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from cryptography.fernet import Fernet
import base64
from django.conf import settings

# Create your views here.
# data table name handymanadmin_handymanadmindetails


#Api to get all the details of the admin
@api_view(['GET', 'POST'])
def handymanadmin_details(request):
    if (request.method == 'GET'):
        worker = HandymanAdminDetails.objects.all()
        handymanadmin_serializer = HandymanAdminDetailsSerializer(worker,many=True)
        return Response(handymanadmin_serializer.data)
    return JsonResponse({"error":'no admin found'}, status=status.HTTP_400_BAD_REQUEST)


#api to create the admin
@api_view(['GET', 'POST'])
def handymanadmin_authentication(request):
    if(request.method == 'POST'):
        user = request.data['username']
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

        #convert the object into readable form
        handymanadmin_serializer = HandymanAdminDetailsSerializer(data=request.data)
        if handymanadmin_serializer.is_valid():
            handymanadmin_serializer.save()
            return Response(handymanadmin_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(handymanadmin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#api to signin the admin
@api_view(['GET', 'POST'])
def handymanadmin_authenticate(request):
    if(request.method == 'POST'):
        user = request.data['username']
        handymanadmin  = HandymanAdminDetails.objects.raw('SELECT * FROM handymanadmin_handymanadmindetails WHERE username =  %s',[user])
        if (handymanadmin):
            handymanadmin_serializer = HandymanAdminDetailsSerializer(handymanadmin,many=True)
            txt = base64.urlsafe_b64decode(handymanadmin_serializer.data[0]['password'])
            cipher_suite = Fernet(settings.ENCRYPT_KEY)
            decrypt_text = cipher_suite.decrypt(txt).decode("ascii")
            if request.data['password']== decrypt_text:
                data = {
                "id"             :handymanadmin_serializer.data[0]['id'],
                "name"           :handymanadmin_serializer.data[0]['name'],
                "username"       :handymanadmin_serializer.data[0]['username'],
                "createdOn"      :handymanadmin_serializer.data[0]['createdOn'],
                "accessToken"    :handymanadmin_serializer.data[0]['accessToken'],
                "branchId"       :handymanadmin_serializer.data[0]['branchId'],
                "stateName"      :handymanadmin_serializer.data[0]['stateName'],
                "country"        :handymanadmin_serializer.data[0]['country'],
                "status"         :handymanadmin_serializer.data[0]['status']
            }
            return Response(data)
        return JsonResponse({"error":'Invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
    # elif(request.method == 'GET'):
    #     handymanadmin  = HandymanAdminDetails.objects.raw('SELECT * FROM handymanadmin_handymanadmindetails WHERE username =  %s',[username])
    #     if (handymanadmin):
    #         handymanadmin_serializer = HandymanAdminDetailsSerializer(handymanadmin,many=True)
    #         txt = base64.urlsafe_b64decode(password)
    #         cipher_suite = Fernet(settings.ENCRYPT_KEY)
    #         decrypt_text = cipher_suite.decrypt(txt).decode("ascii")
    #         if password == decrypt_text:
    #             data = {
    #             "id"             :handymanadmin_serializer.data[0]['id'],
    #             "name"           :handymanadmin_serializer.data[0]['name'],
    #             "username"       :handymanadmin_serializer.data[0]['username'],
    #             "createdOn"      :handymanadmin_serializer.data[0]['createdOn'],
    #             "accessToken"    :handymanadmin_serializer.data[0]['accessToken']
    #         }
    #         return Response(data)
    #     return JsonResponse({"error":'Invalid credentials'},status=status.HTTP_400_BAD_REQUEST)






#api to authenticate admin by access token
@api_view(['GET', 'POST'])
def handymanadmin_authenticateaccesstoken(request,accessToken):
    if(request.method == 'POST'):
        accessToken = request.data['accessToken']
        handymanadmin  = HandymanAdminDetails.objects.raw('SELECT * FROM handymanadmin_handymanadmindetails WHERE "accessToken" =  %s',[accessToken])
        if (handymanadmin):
            handymanadmin_serializer = HandymanAdminDetailsSerializer(handymanadmin,many=True)
            data = {
                "id"             :handymanadmin_serializer.data[0]['id'],
                "name"           :handymanadmin_serializer.data[0]['name'],
                "username"       :handymanadmin_serializer.data[0]['username'],
                "createdOn"      :handymanadmin_serializer.data[0]['createdOn'],
                "accessToken"    :handymanadmin_serializer.data[0]['accessToken'],
                "branchId"       :handymanadmin_serializer.data[0]['branchId'],
                "stateName"      :handymanadmin_serializer.data[0]['stateName'],
                "country"        :handymanadmin_serializer.data[0]['country'],
                "status"         :handymanadmin_serializer.data[0]['status']
            }
            return Response(data)
        return JsonResponse({"error":'Invalid credentials. Please Signin'},status=status.HTTP_400_BAD_REQUEST)
    # return JsonResponse({"error":'Invalid credentials. Please Signin'},status=status.HTTP_400_BAD_REQUEST)

    elif(request.method == 'GET'):
        handymanadmin  = HandymanAdminDetails.objects.raw('SELECT * FROM handymanadmin_handymanadmindetails WHERE "accessToken" =  %s',[accessToken])
        if (handymanadmin):
            handymanadmin_serializer = HandymanAdminDetailsSerializer(handymanadmin,many=True)
            data = {
                "id"             :handymanadmin_serializer.data[0]['id'],
                "name"           :handymanadmin_serializer.data[0]['name'],
                "username"       :handymanadmin_serializer.data[0]['username'],
                "createdOn"      :handymanadmin_serializer.data[0]['createdOn'],
                "accessToken"    :handymanadmin_serializer.data[0]['accessToken'],
                "branchId"       :handymanadmin_serializer.data[0]['branchId'],
                "stateName"      :handymanadmin_serializer.data[0]['stateName'],
                "country"        :handymanadmin_serializer.data[0]['country'],
                "status"         :handymanadmin_serializer.data[0]['status']
            }
            return Response(data)
        return JsonResponse({"error":'Invalid credentials. Please Signin'},status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"error":'Invalid credentials. Please Signin'},status=status.HTTP_400_BAD_REQUEST)
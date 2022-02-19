from functools import partial
from re import T
from django.http.response import JsonResponse
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from cryptography.fernet import Fernet
from product.models import ProductDetails
from product.serializers import ProductDetailsSerializer


##################  Get all the product details  ##################
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        product = ProductDetails.objects.all()
        product_serializer = ProductDetailsSerializer(product,many=True)
        return Response(product_serializer.data)

##################  Add a product  ##################
@api_view(['POST'])
def add_product(request):
    if request.method == 'POST':
        product_serializer = ProductDetailsSerializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##################  Add a product  ##################
@api_view(['POST','PUT'])
def edit_product(request,id):
    try:
        product = ProductDetails.objects.get(ProductId=id)
    except ProductDetails.DoesNotExist: 
        return JsonResponse({"error":'Product doesnot exist doesnot exist'},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        product_serializer = ProductDetailsSerializer(product,data=request.data,partial=True)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data)
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



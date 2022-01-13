from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from worker.serializers import WorkerInformationSerializer
from rest_framework import status
from rest_framework.response import Response
from worker.models import WorkerDetails, WorkerInformation
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST'])
def add_worker_information(request):
    if request.method == 'POST':
        try:
            worker = WorkerDetails.objects.get(id=request.data['foreignId'])
        except WorkerDetails.DoesNotExist: 
            return JsonResponse({"error":'Worker doesnot exist with this id'},status=status.HTTP_404_NOT_FOUND)
    
        worker_information_serializer = WorkerInformationSerializer(data=request.data)
        if worker_information_serializer.is_valid():
            worker_information_serializer.save()
            return JsonResponse(worker_information_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(worker_information_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'DELETE'])
def update_worker_information(request,id):
    try:
        worker = WorkerInformation.objects.get(foreignId=id)
    except WorkerInformation.DoesNotExist: 
        return JsonResponse({"error":'Worker doesnot exist'},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        #In serializer the worker object is passed to make the django know to update which user
        #data is passsed because is nedded for django to validate the request
        worker_information_serializer = WorkerInformationSerializer(worker,data=request.data)
        if(worker_information_serializer.is_valid()):
            worker_information_serializer.save()
            return JsonResponse(worker_information_serializer.data)
        return JsonResponse(worker_information_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        worker_information_serializer = WorkerInformationSerializer(worker)
        return JsonResponse(worker_information_serializer.data)


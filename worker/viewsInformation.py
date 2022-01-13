from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from worker.serializers import WorkerInformationSerializer
from rest_framework import status
from rest_framework.response import Response
from worker.models import WorkerInformation

@api_view(['GET', 'POST'])
def add_worker_information(request):
    if request.method == 'POST':
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
        worker_information_serializer = WorkerInformationSerializer(worker)
        return JsonResponse(worker_information_serializer.data)

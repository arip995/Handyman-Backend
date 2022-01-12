from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from worker.serializers import WorkerInformationSerializer
from rest_framework import status
from rest_framework.response import Response
from worker.models import WorkerInformation

@api_view(['PUT', 'POST'])
def add_worker_information(request):
    if request.method == 'POST':
        worker_information_serializer = WorkerInformationSerializer(data=request.data)
        if worker_information_serializer.is_valid():
            worker_information_serializer.save()
            return JsonResponse(worker_information_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(worker_information_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        user = request.data['key']
        print(user)
        workerInfo = WorkerInformation.objects.raw('SELECT * FROM worker_workerinformation WHERE key =  %s',[user])
        if(workerInfo):
            worker_information_serializer = WorkerInformationSerializer(workerInfo)
            return JsonResponse(worker_information_serializer.data)
        return JsonResponse({"error":'User not found'},status=status.HTTP_400_BAD_REQUEST)
        

from rest_framework import serializers
from worker.models import WorkerDetails

class WorkerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerDetails
        # fields = ('id','name')
        fields = '__all__'
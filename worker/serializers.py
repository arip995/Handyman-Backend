import json
from rest_framework import serializers
from worker.models import WorkerDetails
from worker.models import WorkerInformation

class WorkerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerDetails
        # fields = ('id','name')
        fields = '__all__'


# For getting details of all the workers, we should not give password and accessToken
class WorkerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerDetails
        fields = ('id','firstName','lastName','username','worktype','isActivated','createdOn','mobileNumber')
        # fields = '__all__'


class WorkerInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerInformation
        fields = '__all__'

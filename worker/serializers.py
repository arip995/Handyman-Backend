from rest_framework import serializers
from worker.models import WorkerDetails

class WorkerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerDetails
        # fields = ('id','name')
        fields = '__all__'


# For getting details of all the workers, we should not give password and accessToken
class WorkerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerDetails
        fields = ('id','firstName','lastName','username','worktype','isActivated','createdOn')
        # fields = '__all__'
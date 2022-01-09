from rest_framework import serializers
from handymanadmin.models import HandymanAdminDetails

class HandymanAdminDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandymanAdminDetails
        # fields = ('id','name')
        fields = '__all__'
from rest_framework import serializers
from product.models import ProductDetails

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        # fields = ('id','name')
        fields = '__all__'

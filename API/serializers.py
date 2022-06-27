from rest_framework import serializers
from .models import Product

# serializing product's data
class ProductSeriarizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
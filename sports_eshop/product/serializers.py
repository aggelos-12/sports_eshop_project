from rest_framework import serializers
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "productName",
            "color",
            "price",
            "getAbsoluteURL",
            "getThumbnail",
            "getImage"
        )
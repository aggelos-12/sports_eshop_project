import injector as injector
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from dependency_injector import containers, providers


##### Προσπαθησα να χρησιμοποιησω το dependency_injector αλλα δεν βρηκα πολλα για το πως,
##### κώδικα κάτω δεν λειτουργεί, δειτε πρώτα πως τρέχει με την
##### κάτω class py manage.py runserver link αυτο που θα βγάλει στο terminal + /api/v1/latest-products

class LatestProductsList(APIView):
    def __init__(self, productSerializer: ProductSerializer):
        self.productSerializer = productSerializer

    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = self.productSerializer(products, many=True)
        return Response(serializer.data)



################# ETSI TO EXEI STO VIDEO #################

# class LatestProductsList(APIView):
#     def get(self, request, format=None):
#         products = Product.objects.all()[0:4]
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

####################################################################



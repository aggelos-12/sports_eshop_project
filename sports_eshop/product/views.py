from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.http import Http404


class LatestProductsList(APIView):
    product_model = Product
    serializer_class = ProductSerializer

    def get(self, request, format=None):
        products = self.product_model.objects.all()[0:4]
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    product_model = Product
    serializer_class = ProductSerializer

    def get_object(self, category_slug, product_slug):
        try:
            return self.product_model.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except self.product_model.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = self.serializer_class(product)
        return Response(serializer.data)
class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerialiazer(category)
        return Response(serializer.data)
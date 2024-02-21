from django.urls import path, include
from . import views

urlpatterns = [
    path('latest-products/', views.LatestProductList.as_view(), name='latest-products'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view(), name='product-page'),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view(), name='category-page'),

]
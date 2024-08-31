from django.shortcuts import render,get_object_or_404
from rest_framework  import  viewsets,pagination,filters,status
from rest_framework import viewsets, filters 
from .import models
from .import  serializers
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.http import Http404
from rest_framework.response import Response

class BrandViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=models.Brand.objects.all()
    serializer_class=serializers.BrandSerializer

class CategoryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=models.Category.objects.all()
    serializer_class=serializers.CategorySerializer

class SizeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=models.Size.objects.all()
    serializer_class=serializers.SizeSerializer

# class ProductPagination(pagination.PageNumberPagination):
#     page_size=5
#     page_size_query_param=page_size
#     max_page_size=100


class ProductViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    search_fields = ['brand__brand', 'category__category', 'size__size', 'color__color']


class ProductsDetail(APIView):
    def get_object(self, pk):
        try:
            return models.Product.objects.get(pk=pk)
        except models.Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = serializers.ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = serializers.ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ReviewViewset(viewsets.ModelViewSet):
 
    queryset=models.Review.objects.all()
    serializer_class=serializers.ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product']  

class ColorViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=models.Color.objects.all()
    serializer_class=serializers.ColorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['color']


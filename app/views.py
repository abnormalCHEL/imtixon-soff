from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework import generics
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Blog, Category
from .serializers import  CategorySerializer,BlogRecomendationSerializer,BlogDetailSerializer,BlogListSerializer



class SponsorCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.BlogCreateSerializer

class BlogListView(generics.ListAPIView):
    

    serializer_class = serializers.BlogListSerializer    
    queryset = models.Blog.objects.all()
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogListSerializer(blogs, many=True)
        filter_backends = [filters.SearchFilter, DjangoFilterBackend]
       
        filterset_fields = ['cat']
        return Response(serializer.data)

# class CategoryListView(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
    
    
    
class BlogRecomendationView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogRecomendationSerializer(blogs, many=True)
        return Response(serializer.data)
    
    
    
class BlogDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.BlogDetailSerializer
    queryset = models.Blog.objects.all()
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogDetailSerializer(blogs, many=True)
        return Response(serializer.data)


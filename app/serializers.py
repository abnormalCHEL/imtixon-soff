from rest_framework import serializers

from . import models




class BlogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = ('name', 'image', 'body',
                  'cat', 'author','created_at',)
        



class BlogListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = ('name', 'image', 'created_at',
                  'cat',)
        
        
class BlogRecomendationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        exclude = ('body')
        
        
class BlogDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = '__all__'
        
        
        
class CategorySerializer(serializers.ModelSerializer):
     class Meta:
        model = models.Category
        fields = '__all__'
        
        
       
        

        

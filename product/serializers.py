from rest_framework import  serializers
from .import models 
class BrandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Brand
        fields='__all__'
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Category
        fields='__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Size
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField(many=True)
    color=serializers.StringRelatedField(many=True)
    size=serializers.StringRelatedField(many=True)
    
    class Meta:
        model=models.Product
        fields='__all__'
      
        

class ReviewSerializer(serializers.ModelSerializer):
    # reviewer=serializers.StringRelatedField()
    class Meta:
        model=models.Review
        fields='__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Color
        fields='__all__'

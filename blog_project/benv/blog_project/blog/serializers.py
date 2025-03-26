from rest_framework import serializers
from .models import Post, Comment, Like, Category

# serializer for post
class PostSerializer(serializers.ModelSerializer):
    # Prevents modification of the author field when creating/updating posts.
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = '__all__' #Includes all model fields in the API response
        
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Comment
        fields = '__all__'
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

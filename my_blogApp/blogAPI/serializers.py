from .models import Blog
from rest_framework import serializers

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class EachBlogSerializer(serializers.Serializer):
    blog = BlogSerializers()
    related_blogs = BlogSerializers(many=True)
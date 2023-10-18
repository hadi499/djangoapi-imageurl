from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'image_url')

    def get_image_url(self, obj):
        url = 'http://localhost:8000'
        return url + obj.image.url

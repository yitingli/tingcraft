from rest_framework import serializers

from .models import MicroBlog
from mediaframes.serializers import MediaFrameSerializer


class MicroBlogSerializer(serializers.ModelSerializer):

    media_frame = MediaFrameSerializer()

    class Meta:
        model = MicroBlog
        fields = ('id', 'content', 'media_frame', 'created')

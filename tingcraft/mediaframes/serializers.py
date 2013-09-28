from django.conf import settings
from rest_framework import serializers

from .models import MediaFrame


class MediaField(serializers.Field):

    def field_to_native(self, obj, field_name):
        if obj.content_type == "I" and obj.image_item:
            geometry = settings.IMAGE_SIZE['MICROBLOG_IMAGE']
            url = obj.image_item.get_image_url(geometry)
            width, height = obj.image_item.get_image_size(geometry)
            return {
                'url': url,
                'width': width,
                'height': height,
            }
        return ''


class MediaFrameSerializer(serializers.ModelSerializer):

    media = MediaField()

    class Meta:
        model = MediaFrame
        fields = ('id', 'album', 'owner', 'description', 'media',)

from django.db import models
from model_utils.models import TimeStampedModel
from sorl.thumbnail import get_thumbnail

from .helpers import upload_image_filename, upload_file_filename


class MediaBase(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    link = models.URLField(default='', blank=True)

    class Meta:
        abstract = True


class MediaImage(MediaBase):

    extension = models.CharField(max_length=10, default='', blank=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(upload_to=upload_image_filename, width_field='width',
                              height_field='height')

    def get_image(self, geometry, crop='center'):
        if crop:
            thumbnail = get_thumbnail(self.image, geometry, crop=crop)
        else:
            thumbnail = get_thumbnail(self.image, geometry)
        return thumbnail

    def get_image_url(self, geometry, crop='center'):
        image = self.get_image(geometry, crop)
        return image.url


class MediaVideo(MediaBase):

    video_code = models.CharField(max_length=255, default='', blank=True)


class MediaFile(MediaBase):

    title = models.CharField(max_length=50, default='Untitled', blank=True)
    doc = models.FileField(upload_to=upload_file_filename)
    rank = models.FloatField(default=100.0, blank=True)

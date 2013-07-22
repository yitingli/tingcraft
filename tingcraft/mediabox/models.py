from django.db import models
from model_utils.models import TimeStampedModel


class MediaBase(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    link = models.URLField(default='', blank=True)

    class Meta:
        abstract = True


class MediaImage(MediaBase):

    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', width_field='width', height_field='height',
                              null=True, blank=True)


class MediaVideo(MediaBase):

    video_code = models.CharField(max_length=300, default='', blank=True)

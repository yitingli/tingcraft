from django.db import models
from model_utils.models import TimeStampedModel


class MediaBase(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    link = models.URLField(default='', blank=True)

    class Meta:
        abstract = True


class MediaImage(MediaBase):

    extension = models.CharField(max_length=10, default='', blank=True)
    image = models.ImageField(upload_to='images/origin/')


class MediaVideo(MediaBase):

    video_code = models.CharField(max_length=300, default='', blank=True)

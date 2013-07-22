from django.db import models
from model_utils.models import TimeStampedModel


class MicroBlog(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    content = models.CharField(max_length=180, default='', blank=True)
    image_item = models.ForeignKey('mediabox.MediaImage', null=True, blank=True)
    video_item = models.ForeignKey('mediabox.MediaVideo', null=True, blank=True)


class MicroComment(TimeStampedModel):

    micro_blog = models.ForeignKey('microblogs.MicroBlog')
    content = models.CharField(max_length=180)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

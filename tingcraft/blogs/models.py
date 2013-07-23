from django.db import models
from model_utils.models import TimeStampedModel


class Blog(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    content = models.TextField(default='')


class Comment(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    blog = models.ForeignKey('blogs.Blog')
    content = models.TextField(default='')
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

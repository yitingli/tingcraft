from django.db import models
from django.core.urlresolvers import reverse
from model_utils.models import TimeStampedModel


class Blog(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    title = models.CharField(max_length=255, default='', db_index=True)
    content = models.TextField(default='')
    is_public = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('blog:list', kwargs={'username': self.owner.username})


class Comment(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    blog = models.ForeignKey('blogs.Blog')
    content = models.TextField(default='')
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

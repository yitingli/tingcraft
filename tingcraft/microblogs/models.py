from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from model_utils.models import TimeStampedModel


class MicroBlog(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    content = models.CharField(max_length=180, default='', blank=True)
    image_item = models.ForeignKey('mediabox.MediaImage', null=True, blank=True)
    video_item = models.ForeignKey('mediabox.MediaVideo', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('microblog:list', kwargs={'username': self.owner.username})

    def get_microcomments(self, start_index, size=settings.PAGE_SIZE['MICROCOMMENT']):
        end_index = start_index + size
        return MicroComment.objects.filter(micro_blog=self)[start_index:end_index]


class MicroComment(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    micro_blog = models.ForeignKey('microblogs.MicroBlog')
    content = models.CharField(max_length=180)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

from django.db import models
from model_utils.models import TimeStampedModel


class Album(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    name = models.CharField(max_length=100)
    cover = models.ForeignKey('mediaframes.MediaFrame', null=True, blank=True, related_name='cover')
    description = models.CharField(max_length=300)

    is_public = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

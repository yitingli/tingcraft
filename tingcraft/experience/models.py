from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class ExpDevision(TimeStampedModel):

    name = models.CharField(max_length=255)
    owner = models.ForeignKey('users.TingUser')
    rank = models.IntegerField(default=100)


class ExpItem(TimeStampedModel):

    devision = models.ForeignKey('experience.ExpDevision', null=True, blank=True)

    title = models.CharField(max_length=255)
    place = models.CharField(max_length=50, default='', blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=255, default='', blank=True)
    other = models.CharField(max_length=255, default='', blank=True)

    content = models.TextField(default='', blank=True)
    rank = models.IntegerField(default=100)
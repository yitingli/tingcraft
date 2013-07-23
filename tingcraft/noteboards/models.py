from django.db import models
from model_utils.models import TimeStampedModel


class NoteBoard(TimeStampedModel):

    title = models.CharField(max_length=30)
    owner = models.ForeignKey('users.TingUser')
    rank = models.IntegerField(default=0)


class Note(TimeStampedModel):

    board = models.ForeignKey('noteboards.NoteBoard')
    content = models.TextField(default='', blank=True)


class NoteComment(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    note = models.ForeignKey('noteboards.Note')
    content = models.TextField(default='', blank=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True)

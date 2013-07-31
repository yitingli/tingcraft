from slugify import slugify

from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel


class NoteBoard(TimeStampedModel):

    title = models.CharField(max_length=30)
    owner = models.ForeignKey('users.TingUser')
    rank = models.IntegerField(default=100)

    # default max_length = 50
    slug = models.SlugField()

    class Meta:
        unique_together = (('owner', 'slug'), )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NoteBoard, self).save(*args, **kwargs)

    def get_notes(self, max_id, size=settings.PAGE_SIZE['NOTE']):
        if max_id == 0:
            return Note.objects.filter(board=self)[:size]
        else:
            return Note.objects.filter(pk__lt=max_id, board=self)[:size]


class Note(TimeStampedModel):

    board = models.ForeignKey('noteboards.NoteBoard')
    content = models.TextField(default='', blank=True)


class NoteComment(TimeStampedModel):

    owner = models.ForeignKey('users.TingUser')
    note = models.ForeignKey('noteboards.Note')
    content = models.TextField(default='', blank=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True)

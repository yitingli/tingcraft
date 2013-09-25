from rest_framework import serializers

from .models import NoteBoard, Note


class NoteCreateSerializer(serializers.ModelSerializer):

    board = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Note
        fields = ('board', 'content')

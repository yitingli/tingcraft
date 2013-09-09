from rest_framework import serializers

from .models import ExpDevision, ExpItem


class ExpDevisionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpDevision
        fields = ('name', 'rank')

    def restore_object(self, attrs, instance=None):
        attrs['owner'] = self.context['user']
        devision = ExpDevision(**attrs)
        return devision


class ExpItemCreateSerializer(serializers.ModelSerializer):

    devision = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = ExpItem
        fields = ('devision', 'title', 'place', 'start_date', 'end_date',
                  'position', 'other', 'content', 'rank')

from django import forms

from .models import MediaFrame
from albums.models import Album
from mediabox.models import MediaImage, MediaVideo


class MediaFrameCreateForm(forms.ModelForm):

    description = forms.CharField(max_length=300, widget=forms.Textarea)
    image = forms.ImageField(required=False)
    video_code = forms.CharField(max_length=300, required=False)
    album = forms.ModelChoiceField(queryset=None, empty_label=None)

    class Meta:
        model = MediaFrame
        fields = ('description', 'image', 'video_code', 'album')

    def __init__(self, *args, **kwargs):
        self.owner = kwargs['initial']['owner']
        super(MediaFrameCreateForm, self).__init__(*args, **kwargs)
        self.album = Album.objects.filter(owner=self.owner).order_by('created')
        self.fields['album'].queryset = self.album
        if len(self.album) > 0:
            self.fields['album'].initial = self.album[0]

    def save(self, commit=True):
        media_frame = super(MediaFrameCreateForm, self).save(commit=False)
        if commit:
            image = self.cleaned_data['image']
            video_code = self.cleaned_data['video_code']
            if image:
                image_item = MediaImage(image=image, owner=self.owner)
                image_item.save()
                media_frame.content_type = 'I'
                media_frame.image_item = image_item
            elif video_code:
                video_item = MediaVideo(video_code=video_code, owner=self.owner)
                video_item.save()
                media_frame.content_type = 'V'
                media_frame.video_item = video_item
            else:
                raise
            media_frame.owner = self.owner
            media_frame.save()
        return media_frame

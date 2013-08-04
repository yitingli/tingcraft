from django import forms

from .models import MicroBlog
from albums.models import Album
from mediaframes.models import MediaFrame
from mediabox.models import MediaImage, MediaVideo


class MicroBlogCreateForm(forms.ModelForm):

    image = forms.ImageField(required=False)
    video_code = forms.CharField(max_length=300, required=False)
    album = forms.ModelChoiceField(queryset=None, empty_label=None)

    class Meta:
        model = MicroBlog
        fields = ('content', 'image', 'video_code')

    def __init__(self, *args, **kwargs):
        self.owner = kwargs['initial']['owner']
        super(MicroBlogCreateForm, self).__init__(*args, **kwargs)
        self.album = Album.objects.filter(owner=self.owner).order_by('created')
        self.fields['album'].queryset = self.album
        if len(self.album) > 0:
            self.fields['album'].initial = self.album[0]

    def save(self, commit=True):
        microblog = super(MicroBlogCreateForm, self).save(commit=False)
        if commit:
            image = self.cleaned_data['image']
            video_code = self.cleaned_data['video_code']
            album = self.cleaned_data['album']
            if image:
                image_item = MediaImage(image=image, owner=self.owner)
                image_item.save()
                media_frame = MediaFrame(album=album, content_type='I', owner=self.owner)
                media_frame.image_item = image_item
                media_frame.save()
                microblog.media_frame = media_frame
            elif video_code:
                video_item = MediaVideo(video_code=video_code, owner=self.owner)
                video_item.save()
                media_frame = MediaFrame(album=album, content_type='V', owner=self.owner)
                media_frame.video_item = video_item
                media_frame.save()
                microblog.media_frame = media_frame
            microblog.owner = self.owner
            microblog.save()
        return microblog

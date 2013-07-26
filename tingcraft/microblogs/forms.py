from django import forms

from .models import MicroBlog
from mediabox.models import MediaImage, MediaVideo


class MicroBlogCreateForm(forms.ModelForm):

    image = forms.ImageField(required=False)
    video_code = forms.CharField(max_length=300, required=False)

    class Meta:
        model = MicroBlog
        fields = ('content', 'image', 'video_code')

    def __init__(self, *args, **kwargs):
        self.owner = kwargs['initial']['owner']
        super(MicroBlogCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        microblog = super(MicroBlogCreateForm, self).save(commit=False)
        if commit:
            image = self.cleaned_data['image']
            video_code = self.cleaned_data['video_code']
            if image:
                image_item = MediaImage(image=image, owner=self.owner)
                image_item.save()
                microblog.image_item = image_item
            elif video_code:
                video_item = MediaVideo(video_code=video_code, owner=self.owner)
                video_item.save()
                microblog.video_item = video_item
            microblog.owner = self.owner
            microblog.save()
        return microblog

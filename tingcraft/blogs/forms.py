from django import forms

from .models import Blog


class BlogCreateForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'content', 'is_public')

    def __init__(self, *args, **kwargs):
        self.owner = kwargs['initial']['owner']
        super(BlogCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        blog = super(BlogCreateForm, self).save(commit=False)
        if commit:
            blog.owner = self.owner
            blog.save()
        return blog

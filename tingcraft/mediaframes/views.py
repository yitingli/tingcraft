from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView

from .models import MediaFrame
from .forms import MediaFrameCreateForm
from core.mixins import OwnerContextMixin, OwnerRequiredMixin


class MediaFrameCreateView(LoginRequiredMixin, OwnerContextMixin, OwnerRequiredMixin, CreateView):

    model = MediaFrame
    form_class = MediaFrameCreateForm
    template_name = 'mediaframes/create.html'

    def get_initial(self):
        self.initial['owner'] = self.request.user
        return super(MediaFrameCreateView, self).get_initial()

    def get_login_url(self):
        return reverse('login')

    def get_sucessful_url(self):
        return reverse('album:list', kwargs={'username': self.request.user})


class MediaFrameDetailView(OwnerContextMixin, DetailView):

    model = MediaFrame
    template_name = 'mediaframes/detail.html'

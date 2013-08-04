from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView

from .models import Blog
from users.models import TingUser
from core.pagination import BlogPaginationMixin
from core.mixins import OwnerContextMixin


class BlogListView(BlogPaginationMixin, OwnerContextMixin, ListView):

    model = Blog
    context_object_name = 'blogs'
    template_name = 'blogs/list.html'

    def get_queryset(self):
        username = self.kwargs['username']
        self.owner = get_object_or_404(TingUser, username=username)
        if self.request.user == self.owner:
            queryset = self.owner.get_blogs(max_id=self.max_id, only_public=False)
        else:
            queryset = self.owner.get_blogs(max_id=self.max_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['owner'] = self.owner
        return context


class BlogCreateView(OwnerContextMixin, CreateView):
    pass

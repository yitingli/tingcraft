from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView

from .models import MicroBlog
from .forms import MicroBlogCreateForm
from users.models import TingUser
from core.pagination import MicroBlogPaginationMixin
from core.mixins import OwnerContextMixin


class MicroBlogListView(MicroBlogPaginationMixin, OwnerContextMixin, ListView):

    model = MicroBlog
    context_object_name = 'microblogs'
    template_name = 'microblogs/list.html'

    def get_queryset(self):
        queryset = self.owner.get_microblogs(max_id=self.max_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(MicroBlogListView, self).get_context_data(**kwargs)
        return context


class MicroBlogCreateView(LoginRequiredMixin, OwnerContextMixin, CreateView):

    model = MicroBlog
    form_class = MicroBlogCreateForm
    template_name = 'microblogs/create.html'

    def get_initial(self):
        self.initial['owner'] = self.request.user
        return super(MicroBlogCreateView, self).get_initial()

    def get_login_url(self):
        return reverse('login')

    def get_sucessful_url(self):
        return reverse('microblog:list', kwargs={'username': self.request.user})

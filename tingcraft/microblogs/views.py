from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .models import MicroBlog
from .forms import MicroBlogCreateForm
from .serializers import MicroBlogSerializer
from users.models import TingUser
from core.pagination import MicroBlogPaginationMixin, MicroBlogPaginationAPIMixin
from core.mixins import OwnerContextMixin


class MicroBlogListView(MicroBlogPaginationMixin, OwnerContextMixin, ListView):

    model = MicroBlog
    context_object_name = 'microblogs'
    template_name = 'microblogs/list.html'

    def dispatch(self, request, *args, **kwargs):
        if request.is_ajax():
            self.template_name = 'microblogs/list_ajax.html'
        return super(MicroBlogListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.owner.get_microblogs(max_id=self.max_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(MicroBlogListView, self).get_context_data(**kwargs)
        return context


class MicroBlogListAPIView(MicroBlogPaginationAPIMixin, APIView):

     permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

     def get(self, request, pk, format=None):
        self.owner = get_object_or_404(TingUser, pk=pk)
        self.get_max_id(request)
        queryset = self.owner.get_microblogs(max_id=self.max_id)
        serializer = MicroBlogSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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

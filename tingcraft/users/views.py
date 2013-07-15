from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, resolve_url
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView
from django.views.generic.edit import FormMixin

from .models import User
from .forms import UserCreateForm, UserLoginForm, UserUpdateForm, UserPasswordChangeForm


def login(request):
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
        return render(request, 'users/login.html', {'form': form})
    else:
        form = UserLoginForm()
        return render(request, 'users/login.html', {'form': form})


class UserCreateView(CreateView):

    model = User
    form_class = UserCreateForm
    template_name = 'users/create.html'

    #@Note: CreateView, UpdateView has built-in FormMixin
    def get_success_url(self):
        return reverse('home')

    #@Note: replace [if form.is_valid():]; redirects to get_success_url()
    def form_valid(self, form):
        form.save()
        user = auth.authenticate(username=form.cleaned_data['email'],
                                 password=form.cleaned_data['password'])
        if user is not None:
            auth.login(self.request, user)
            return super(UserCreateView, self).form_valid(form)
        else:
            return render(self.request, 'users/create.html', {'form': form, 'error_msg': 'create error'})


class UserUpdateView(UpdateView):

    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'

    #@Note: By default, it will get object from pk or slug
    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        return render(self.request, 'users/update.html', {'form': form, 'update_success': True})


class UserPasswordChangeView(UpdateView):

    model = User
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change.html'

    #@Note: By default, it will get initial data from self.initial variable
    def get_initial(self):
        self.initial.update({'user': self.request.user})
        return super(UserPasswordChangeView, self).get_initial()

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('user_update')

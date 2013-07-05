from django.contrib import auth
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, resolve_url

from .forms import CraftCrewCreateForm, CraftCrewLoginForm


def login(request):
    if request.POST:
        form = CraftCrewLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
        return render(request, 'users/login.html', {'form': form})
    else:
        form = CraftCrewLoginForm()
        return render(request, 'users/login.html', {'form': form})

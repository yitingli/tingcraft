from datetime import datetime

from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .models import NoteBoard, Note
from .serializers import NoteCreateSerializer
from users.models import TingUser
from core.permissions import IsOwnerOrReadOnly
from core.pagination import NoteBoardPaginationMixin, NotePaginationMixin
from core.mixins import OwnerContextMixin


class NoteBoardListView(NoteBoardPaginationMixin, OwnerContextMixin, ListView):

    model = NoteBoard
    context_object_name = 'noteboards'
    template_name = 'noteboards/list.html'

    def get_queryset(self):
        username = self.kwargs['username']
        self.owner = get_object_or_404(TingUser, username=username)
        queryset = self.owner.get_noteboards(max_id=self.max_id)
        return queryset


class NoteListView(NotePaginationMixin, OwnerContextMixin, ListView):

    model = Note
    context_object_name = 'notes'
    template_name = 'noteboards/noteboard.html'

    def get_queryset(self):
        username = self.kwargs['username']
        slug = self.kwargs['slug']
        self.owner = get_object_or_404(TingUser, username=username)
        self.board = get_object_or_404(NoteBoard, owner=self.owner, slug=slug)
        queryset = self.board.get_notes(max_id=self.max_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(NoteListView, self).get_context_data(**kwargs)
        context['noteboard'] = self.board
        return context


class NoteCreateAPIView(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def post(self, request, format=None):
        serializer = NoteCreateSerializer(data=request.DATA)
        if serializer.is_valid():
            self.check_object_permissions(request, serializer.object.board)
            serializer.save()
            return Response({
                                'id': serializer.object.pk,
                                'created': serializer.object.created.strftime('%b %d, %Y, %H:%M %P'),
                            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

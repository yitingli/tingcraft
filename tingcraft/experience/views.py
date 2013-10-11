from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .models import ExpDevision, ExpItem
from .serializers import ExpDevisionCreateSerializer, ExpItemCreateSerializer
from core.permissions import IsOwnerOrReadOnly
from core.mixins import OwnerContextMixin
from users.models import TingUser
from mediabox.models import MediaFile


class ExpListView(OwnerContextMixin, ListView):

    template_name = 'experience/list.html'
    context_object_name = 'experience'

    def get_queryset(self):
        username = self.kwargs['username']
        self.owner = get_object_or_404(TingUser, username=username)
        queryset = self.owner.get_experience()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ExpListView, self).get_context_data(**kwargs)
        context['documents'] = MediaFile.objects.filter(owner=self.owner, is_public=True).order_by('-rank')
        return context


class ExpDevisionCreateAPIView(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def post(self, request, format=None):
        serializer = ExpDevisionCreateSerializer(data=request.DATA)
        if serializer.is_valid():
            self.check_object_permissions(request, serializer.object)
            serializer.save()
            return Response({
                                'id': serializer.object.pk,
                            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpItemCreateAPIView(APIView):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def post(self, request, format=None):
        serializer = ExpItemCreateSerializer(data=request.DATA)
        if serializer.is_valid():
            self.check_object_permissions(request, serializer.object)
            serializer.save()
            return Response({
                                'id': serializer.object.pk,
                            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

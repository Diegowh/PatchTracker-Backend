from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Episode, PatchNote, Content
from .serializers import EpisodeSerializer, PatchNoteSerializer, ContentSerializer


class EpisodeView(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['episode']

class PatchNoteView(viewsets.ModelViewSet):
    queryset = PatchNote.objects.all()
    serializer_class = PatchNoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['patchnote']

class ContentView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['content']
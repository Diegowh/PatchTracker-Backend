from django.shortcuts import render
from rest_framework import viewsets

from .models import Episode, PatchNote, Content
from .serializers import EpisodeSerializer, PatchNoteSerializer, ContentSerializer
from .filters import ContentFilter, PatchNoteFilter


class EpisodeView(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class PatchNoteView(viewsets.ModelViewSet):
    queryset = PatchNote.objects.all()
    serializer_class = PatchNoteSerializer
    filterset_class = PatchNoteFilter

class ContentView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filterset_class = ContentFilter
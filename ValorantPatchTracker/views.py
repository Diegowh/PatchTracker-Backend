from django.shortcuts import render
from rest_framework import viewsets

from .models import Episode, PatchNote, Content
from .serializers import EpisodeSerializer, PatchNoteSerializer, ContentSerializer


class EpisodeView(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class PatchNoteView(viewsets.ModelViewSet):
    queryset = PatchNote.objects.all()
    serializer_class = PatchNoteSerializer

class ContentView(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
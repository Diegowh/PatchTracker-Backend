from django.shortcuts import render
from rest_framework import viewsets

from .models import Episode, PatchNote, Content
from .serializers import EpisodeSerializer, PatchNoteSerializer, ContentSerializer

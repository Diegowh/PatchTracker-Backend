from django.shortcuts import render
from django.http import HttpResponse
from .scraper.scraper import LoLScraper
import json

from rest_framework import viewsets
from .models import Season, Patch, Notes
from . serializers import SeasonSerializer, PatchSerializer, NotesSerializer
from .filters import PatchFilter, NotesFilter

def test_view(request):
    scraper = LoLScraper()
    result = scraper.all_seasons_data
    return HttpResponse(json.dumps(result), content_type="application/json")


class SeasonView(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    
class PatchView(viewsets.ModelViewSet):
    queryset = Patch.objects.all()
    serializer_class = PatchSerializer
    filterset_class = PatchFilter
    
class NotesView(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    filterset_class = NotesFilter
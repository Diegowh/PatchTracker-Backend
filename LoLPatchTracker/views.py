from django.shortcuts import render
from django.http import HttpResponse
from .scraper.scraper import LoLScraper
import json

from rest_framework import viewsets
from .models import Season, Patch, Notes
from . serializers import SeasonSerializer, PatchSerializer, NotesSerializer

def test_view(request):
    test_endpoint = "/Season_Thirteen"
    scraper = LoLScraper()
    result = scraper.all_seasons_data
    return HttpResponse(json.dumps(result), content_type="application/json")

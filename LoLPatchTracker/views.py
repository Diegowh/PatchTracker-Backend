from django.shortcuts import render
from django.http import HttpResponse
from .scraper.scraper import LoLScraper

def test_view(request):
    test_endpoint = "/Season_Thirteen"
    scraper = LoLScraper()
    result = []
    for season in scraper._seasons():
        result.append(season + ', ')
    
    return HttpResponse(result)

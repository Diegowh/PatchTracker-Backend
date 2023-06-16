from django.urls import path
from .views import test_view, SeasonView, PatchView, NotesView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('test/', test_view),
]

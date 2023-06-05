from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EpisodeView, ContentView, PatchNoteView


router = DefaultRouter()

router.register(r'episodes', EpisodeView)
router.register(r'patchnotes', PatchNoteView)
router.register(r'contents', ContentView)


urlpatterns = [
    path('', include(router.urls)),
]
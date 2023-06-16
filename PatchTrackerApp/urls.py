from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from ValorantPatchTracker.views import EpisodeView, PatchNoteView, ContentView
from LoLPatchTracker.views import SeasonView, PatchView, NotesView

router = DefaultRouter()
router.register(r'valorant/episodes', EpisodeView)
router.register(r'valorant/patchnotes', PatchNoteView)
router.register(r'valorant/contents', ContentView)
router.register(r'lol/seasons', SeasonView)
router.register(r'lol/patches', PatchView)
router.register(r'lol/notes', NotesView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

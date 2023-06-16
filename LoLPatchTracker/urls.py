from django.urls import path, include
from .views import test_view, SeasonView, PatchView, NotesView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'seasons', SeasonView)
router.register(r'patches', PatchView)
router.register(r'notes', NotesView)

urlpatterns = [
    path('test/', test_view),
    path('', include(router.urls)),
]

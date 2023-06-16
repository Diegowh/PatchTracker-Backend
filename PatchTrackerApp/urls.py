from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('valorantpatchtracker/', include('ValorantPatchTracker.urls')),
    path('lolpatchtracker/', include('LoLPatchTracker.urls')),
]

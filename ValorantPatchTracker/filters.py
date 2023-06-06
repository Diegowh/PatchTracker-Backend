import django_filters
from .models import Content

class ContentFilter(django_filters.FilterSet):
    class Meta:
        model = Content
        fields = ['patch_note']  # Aquí especificas los campos por los que quieres filtrar.

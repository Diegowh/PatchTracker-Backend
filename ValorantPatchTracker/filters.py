import django_filters
from .models import Content, PatchNote

class ContentFilter(django_filters.FilterSet):
    class Meta:
        model = Content
        fields = ['patch_note']


class PatchNoteFilter(django_filters.FilterSet):
    class meta:
        model = PatchNote
        fields = ['episode']
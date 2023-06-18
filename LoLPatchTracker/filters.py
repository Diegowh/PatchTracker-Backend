import django_filters
from .models import Patch, Notes

class PatchFilter(django_filters.FilterSet):
    class Meta:
        model = Patch
        fields = ['season']
        
        
class NotesFilter(django_filters.FilterSet):
    class Meta:
        model = Notes
        fields = ['patch']
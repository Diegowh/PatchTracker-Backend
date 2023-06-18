import django_filters
from .models import Patch, Notes

class PatchFilter(django_filters.filterset):
    class Meta:
        model = Patch
        fields = ['season']
        
        
class NotesFilter(django_filters.filterset):
    class Meta:
        model = Notes
        fields = ['patch']
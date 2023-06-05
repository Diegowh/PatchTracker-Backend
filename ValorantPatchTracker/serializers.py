from rest_framework import serializers
from .models import Episode, PatchNote, Content

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'

class PatchNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchNote
        fields = '__all__'
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
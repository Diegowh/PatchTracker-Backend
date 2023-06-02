from django.db import models

class Episode(models.Model):
    episode_name = models.TextField()

class PatchNote(models.Model):
    version = models.CharField(max_length=10)
    release_date = models.TextField()
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)

class Content(models.Model):
    patch_note = models.ForeignKey(PatchNote, on_delete=models.CASCADE)
    html = models.TextField()
from django.db import models

class PatchNote(models.Model):
    version = models.CharField(max_length=10)
    release_date = models.DateField()

class Content(models.Model):
    patch_note = models.ForeignKey(PatchNote, on_delete=models.CASCADE)
    html = models.TextField()
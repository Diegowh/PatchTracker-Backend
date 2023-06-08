from django.db import models

class Season(models.Model):
    name = models.TextField()

class Patch(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    release_date = models.TextField()
    
class Notes(models.Model):
    patch = models.ForeignKey(Patch, on_delete=models.CASCADE)
    html = models.TextField()
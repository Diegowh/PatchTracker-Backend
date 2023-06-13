from django.db import models

class Season(models.Model):
    name = models.TextField()
    date = models.TextField()

class Patch(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    date = models.TextField()
    new_champion = models.TextField(null=True, blank=True)
    url = models.TextField(null=True)
    
class Notes(models.Model):
    patch = models.ForeignKey(Patch, on_delete=models.CASCADE)
    html = models.TextField()
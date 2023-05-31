from django.db import models

class PatchNote(models.Model):
    version = models.CharField(max_length=10)
    release_date = models.DateField()
    general_updates = models.TextField()
    known_issues = models.TextField()

class AgentUpdate(models.Model):
    patch_note = models.ForeignKey(PatchNote, on_delete=models.CASCADE)
    agent_name = models.CharField(max_length=50)
    update_details = models.TextField()

class CosmeticUpdate(models.Model):
    patch_note = models.ForeignKey(PatchNote, on_delete=models.CASCADE)
    update_details = models.TextField()

class SystemExperienceUpdate(models.Model):
    patch_note = models.ForeignKey(PatchNote, on_delete=models.CASCADE)
    update_details = models.TextField()

class BugFix(models.Model):
    patch_note = models.ForeignKey(PatchNote, on_delete=models.CASCADE)
    fix_details = models.TextField()
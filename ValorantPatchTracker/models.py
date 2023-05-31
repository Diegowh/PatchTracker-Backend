from django.db import models

class PatchNote(models.Model):
    version = models.CharField(max_length=10)
    release_date = models.DateField()

class GeneralUpdates(models.Model):
    patch_note = models.ForeignKey(PatchNote, on_delete=models.CASCADE)
    update_detail = models.TextField()

class AgentUpdates(models.Model):
    patch_note = models.ForeignKey(PatchNote, on_delete=models.CASCADE)
    agent_name = models.CharField(max_length=50)
    update_detail = models.TextField()

class CosmeticUpdates(models.Model):
    patch_note = models.ForeignKey(PatchNote, on_delete=models.CASCADE)
    update_detail = models.TextField()

class SystemExperienceUpdates(models.Model):
    patch_note = models.ForeignKey(PatchNote, on_delete=models.CASCADE)
    update_detail = models.TextField()

class BugFixes(models.Model):
    patch_note = models.ForeignKey(PatchNote, on_delete=models.CASCADE)
    fix_detail = models.TextField()

class KnownIssues(models.Model):
    patch_note = models.ForeignKey(PatchNote, on_delete=models.CASCADE)
    issue_detail = models.TextField()
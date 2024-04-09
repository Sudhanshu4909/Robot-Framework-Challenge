from django.db import models

class TestCase(models.Model):
    title = models.CharField(max_length=100)
    steps = models.JSONField()
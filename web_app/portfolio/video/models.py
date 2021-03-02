from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=50, unique=True)
    episode = models.CharField()


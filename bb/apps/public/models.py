from django.db import models
from embed_video.fields import EmbedVideoField

class Video(models.Model):
    title = models.CharField(max_length=250)
    video = EmbedVideoField()

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=250)
    #url = EmbedVideoField()
    url = models.URLField(max_length=1000)

    def __str__(self):
        return self.title
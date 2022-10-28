from typing import Any
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

class Song(models.Model):
   artiste = models.ForeignKey(Artiste, on_delete = models.CASCADE)
   artiste = models.OneToOneField(Artiste,
          on_delete = models.CASCADE, primary_key = True)
   title = models.CharField(max_length=100)
   date_released = models.DateField()
   likes = models.IntegerField()
   artiste_id = models.ForeignKey()

class Lyric(models.Model):
    song = models.ForeignKey(Song, on_delete = models.CASCADE)
    song = models.OneToOneField(Song, 
          on_delete = models.CASCADE, primary_key = True)
    content = models.TextField()
    song_id = models.ForeignKey()
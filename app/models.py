from django.db import models


class Music(models.Model):
    name = models.CharField(max_length=256)
    artist = models.CharField(max_length=256)
    layer = models.ImageField(upload_to='img/layers/')
    sound = models.FileField(upload_to='music/sound/')

    def __str__(self) -> str:
        return self.name
    

class Playlist(models.Model):
    musics = models.ManyToManyField(Music, related_name="musics", blank=True)

    def __str__(self):
        return 'Playlist'
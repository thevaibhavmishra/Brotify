from distutils.command import upload
from pyexpat import model
from sunau import AUDIO_FILE_ENCODING_ADPCM_G721
from turtle import title
from django.db import models
from .helpers import get_audio_length
from .validators import validate_isaudio

class Musics(models.Model):
    title =models.CharField(max_length=500)
    artist =models.CharField(max_length=500)
    album = models.ForeignKey('Album',on_delete=models.SET_NULL,null=True,blank=True)
    time_length = models.DecimalField(blank=True,max_digits=20,decimal_places=2)
    audio_file = models.FileField(upload_to='Musics',validators=[validate_isaudio])
    cover_page = models.ImageField(upload_to= "music_image/")

    def save(self,*args,**kwargs):
        if not self.time_length:
            self.time_length = get_audio_length(self.audio_file)
        return super().save(*args,**kwargs)

class Album(models.Model):
    name = models.CharField(max_length=500)  
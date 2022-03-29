import re
from django.shortcuts import  render

from musics.models import Musics

def homePage(request):
    music = Musics.objects.all()
    music_list = list(Musics.objects.all().values())
    return render(request,'home.html',{
        'music': music,
        'music_list' : music_list,
    })
import re
from django.shortcuts import  redirect, render
from musics.form import AddMusicForm
from musics.models import Musics,Album
from django.http import HttpResponseRedirect

def homePage(request):
    music = Musics.objects.all()
    music_list = list(Musics.objects.all().values())
    return render(request,'home.html',{
        'music': music,
        'music_list' : music_list,
    })

def AddForm(request):
    form= AddMusicForm()
    if request.POST:
        form = AddMusicForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            album = form.cleaned_data.get('album')
            if album:
                music_album = Album.objects.get_or_create(name =album)
                instance.album=music_album[0]
                instance.save()
            else:
                instance.save()

        return redirect("musics:home_page")

    return render(request,'addPage.html',{
        'form':form
    })

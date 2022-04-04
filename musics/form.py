from django import forms
from .models import Musics

class AddMusicForm(forms.ModelForm):
    album = forms.CharField(max_length=500,required=False)
    class Meta:
        model=Musics
        fields=("title","artist","audio_file","cover_page")

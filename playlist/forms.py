from django import forms
from .models import Filme, Playlist

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
from django import forms

from .models import Partida, Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Partida
        fields = ('juego', 'duracion','puntos')
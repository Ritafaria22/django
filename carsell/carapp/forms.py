from django import forms 
from .models import Car ,Comment

class Carform(forms.ModelForm):
    class Meta:
        model = Car
        fields= '__all__'

class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields=  ['text']
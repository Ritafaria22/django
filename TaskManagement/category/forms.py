from django import forms 
from .models import Catagory 


class Categoryform(forms.ModelForm):
    class Meta:
        model= Catagory
        fields= '__all__'

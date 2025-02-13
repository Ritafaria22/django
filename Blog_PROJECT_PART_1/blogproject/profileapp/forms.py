from django import forms 
from .models import Profile 

class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields= '__all__'
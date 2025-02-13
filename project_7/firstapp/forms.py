from django import forms 
from firstapp.models import studentmodel

class Studentform(forms.ModelForm):
    class Meta:
        model = studentmodel
        fields= '__all__'
         
        labels = {
            'name': 'student Name',
            'roll' : 'student roll'
        }
        widgets= {
             
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name': 'write ur full name'
        }

        error_messages= {
            'name' : {'required': 'ur name is required'}
        }
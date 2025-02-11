from django import forms
from django.core import validators #builtin validators use korte hole eta import korte hbe
class contactform(forms.Form):
    name = forms.CharField(label="User Name  ",   help_text="enter ur name", 
    required=False,  widget=forms.Textarea(attrs= {'id' : "textarea", 
    'class' : 'class1 class2', 'placeholder': 'enter ur name'}))
    file=forms.FileField()
    email = forms.EmailField(label= "User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age= forms.CharField(widget= forms.NumberInput)
    check= forms.BooleanField()
    appointment=forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    birthdate = forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    CHOICES = [('S', 'S'), ('M', 'Medium'), ('L', 'L')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL= [('P', 'p'), ('M', 'M'), ('B', 'B')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)

# class studentdata(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) <10:
    #         raise forms.ValidationError("name should be at least 10 characters")
    #     return valname
    # def clean_email(self):
    #     valemail=self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("your email must contain .com")
    #     return valemail
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname= self.cleaned_data['name']
    #     valemail= self.cleaned_data['email']
    #     if len(valname) <10:
    #         raise forms.ValidationError("name should be at least 10 characters")
         
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("your email must contain .com")

def len_check(value):
    if len(value) <10:
        raise forms.ValidationError("Enter a text at least 10 char ")


class studentdata(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10,
       message= 'ur name should be at least 10 characters' )])

    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput, validators= [validators.EmailValidator
      (message='enter a valid mail')])

    age= forms.IntegerField(validators=[validators.MaxValueValidator(35, message= 'maximum age is 35'),  validators.MinValueValidator(25,message= 'minimum age is 25')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message= 'File extension must be a pdf file')])
    

class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data =  super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass   != val_pass:
            raise forms.ValidationError("Password does not match")
        if len(val_name ) < 10:
            raise forms.ValidationError("NAme must be at least 10 char")
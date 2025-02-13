from django.shortcuts import render,redirect
from . import forms 
# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        profile_form = forms.Profileform(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profile')
    else:
        profile_form = forms.Profileform()
    return render(request, 'addprofile.html', {'form' : profile_form})
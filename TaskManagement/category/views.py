from django.shortcuts import render,redirect
from . import forms 
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_form = forms.Categoryform(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('homepage')
    else:
        category_form =forms.Categoryform()
    return render(request, 'addcategory.html',  {'form' : category_form })
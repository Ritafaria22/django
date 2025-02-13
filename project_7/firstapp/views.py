from django.shortcuts import render
from firstapp.forms import Studentform
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = Studentform(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)

    else:
        form= Studentform()
    return render(request, 'home.html', {'form': form})


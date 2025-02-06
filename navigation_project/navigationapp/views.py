from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,'navigationapp/about.html')
     

def contact(request):
    return render(request,'navigationapp/contact.html')
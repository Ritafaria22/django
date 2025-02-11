from django.shortcuts import render
from . forms import contactform 
from . forms import studentdata , passwordValidationProject 
# Create your views here.
def home(request):
    return render(request, './firstapp/home.html')

def about(request):
    if request.method == 'POST':
         
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, './firstapp/about.html', {'name' : name, 'email': email, 'select': select})
    else:
        return render(request, './firstapp/about.html')
     

def submit_form(request):
    return render(request, './firstapp/form.html' )

def djangoform(request):
    if request.method == 'POST':
        form = contactform(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./firstapp/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            #return render(request, './firstapp/djangoform.html', {'form': form})
    else:
        form = contactform()
    return render(request, './firstapp/djangoform.html', {'form': form})

def studentform(request):
    if request.method == 'POST':
        form = studentdata(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = studentdata()
    return render(request, './firstapp/djangoform.html', {'form': form})
    



def PasswordValidation(request):
    if request.method == 'POST':
        form = passwordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = passwordValidationProject()
    return render(request, './firstapp/djangoform.html', {'form': form})
    
    
    




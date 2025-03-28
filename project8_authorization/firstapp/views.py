from django.shortcuts import render,redirect
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login,logout, update_session_auth_hash
#Create your views here.

def home(requst):
    return render(requst, './home.html' )


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=RegisterForm(request.POST)
            if form.is_valid():
                
                form.save()
                messages.success(request, "User registered successfully!")
                print(form.cleaned_data)

        else:
            form=RegisterForm()

        return render(request, './signup.html', {'form': form})

    else:
        return redirect('profile')

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method =='POST':
            form = AuthenticationForm(request=request, data= request.POST)#user data access kortchi
            if form.is_valid():
                name= form.cleaned_data['username']
                userpass= form.cleaned_data['password']
                user=authenticate(username=name, password = userpass)#check user database a ase kina
                
                if user is not None:
                    login(request,user)
                    return redirect('profile')
                
            return render(request, './login.html', {'form': form})#if form is invalid it will get back to login page
       
        else:
            form = AuthenticationForm()
            return render(request, './login.html', {'form': form}) 
    else:
        return redirect('profile')


def profile(request):
   if request.user.is_authenticated:
        if request.method == 'POST':
            form=ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                
                form.save()
                messages.success(request, "Account updated successfully!")
                 

        else:
            form=ChangeUserData(instance = request.user)

        return render(request, './profile.html', {'form': form})

   else:
        return redirect('signup')


def user_logout(request):
    logout(request)
    return redirect('userlogin')


def pass_change(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form= PasswordChangeForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form= PasswordChangeForm(user=request.user)
        return render(request, './passchange.html', {'form': form})
    
    else:
        return redirect('userlogin')

 
def pass_change2(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form= SetPasswordForm(user=request.user, data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form= SetPasswordForm(user=request.user)
        return render(request, './passchange.html', {'form': form})
    
    else:
        return redirect('userlogin')


def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form=ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                
                form.save()
                messages.success(request, "Account updated successfully!")
                print(form.cleaned_data)

        else:
            form=ChangeUserData(i)

        return render(request, './profile.html', {'form': form})

    else:
        return redirect('signup')
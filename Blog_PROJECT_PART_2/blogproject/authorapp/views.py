from django.shortcuts import render,redirect
from . import forms 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth  import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from postapp.models import Post

# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully !!')
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : register_form, 'type':'Register'})

def user_login(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user= authenticate(username=user_name, password=user_pass)#check korbe user er data ache kina j login korte chai
            if user is not None:
                messages.success(request, 'Logged in successfully !!')
                login(request,user) #user login korlo
                return redirect('profile')
            # else:
            #     messages.warning(request, 'Log in information is incorrect !!')
            #     return redirect('register')
        else:
            messages.warning(request, ' Log in information is incorrect !!!')
            return redirect('register')    
    else:
        form= AuthenticationForm()
        return render(request, 'register.html', {'form': form, 'type':'Login' })

def user_logout(request):
    
    logout(request)
    messages.success(request, 'Logged out successfully !!')
    return redirect('user_login')

 
@login_required            
def profile(request):
    data= Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'data': data})



@login_required            
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully !!')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance=request.user)#instance diye edit er profile fillup kora thakbe by default
    return render(request, 'update_profile.html', {'form' : profile_form })


 

def pass_change(request):
    if request.method == 'POST':
         form =PasswordChangeForm(request.user, data=request.POST)
         if form.is_valid():
            form.save()
            messages.success(request, 'password updated successfully !!')
            update_session_auth_hash(request, request.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form' :  form, 'type':'Register'})

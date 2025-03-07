from django.shortcuts import render,redirect
from django.contrib import messages
from carapp.models import Order 
from . import forms 
from . import models
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView,UpdateView,DeleteView
from carapp.models import Purchase 
from . import views 

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


#login with class based view
class UserLoginView(LoginView):
    template_name='register.html'
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self,form):
         messages.success(self.request, 'logged in successful')
         return super().form_valid(form)
    def form_invalid(self,form):
         messages.success(self.request, 'logged in information is incorrect')
         return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Login'
        return context



 
@login_required
def profile(request):
    purchases = Purchase.objects.filter(user=request.user).select_related('car')
    return render(request, 'profile.html', {'purchases': purchases})


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

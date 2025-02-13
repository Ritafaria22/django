from django.shortcuts import render,redirect
from . import forms 
from . import models
# Create your views here.

def add_post(request):
    if request.method == 'POST':
        post_form = forms.Postform(request.POST)#request mane form user fillup korse
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form  = forms.Postform()
    return render(request, 'addpost.html', {'form' : post_form})


def edit_post(request,id):
    post = models.Post.objects.get(pk=id)#j post edit korte chai seta filter kore niye aslam.j post a click korbo setar id diye.
    post_form = forms.Postform(instance=post)#edit a click kore 1st a edit page niye ekta instance dekhabe.jekhane age the post er title,content thakbe.mane form fill up kora thakbe
    if request.method == 'POST':
        post_form = forms.Postform(request.POST, instance=post)#request mane form user fillup korse
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')#edit kore submit korar pore homepage a niye jabe
     
    return render(request, 'addpost.html', {'form' : post_form})


def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')


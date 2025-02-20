from django.shortcuts import render,redirect
from . import forms 
from . import models
# Create your views here.

def add_task(request):
    if request.method == 'POST':
        task_form = forms.Taskform(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
    else:
        task_form = forms.Taskform()
    return render(request, 'addtask.html', {'form' : task_form})


def edit_task(request,id):
    task = models.Task.objects.get(pk=id)#j post edit korte chai seta filter kore niye aslam.j post a click korbo setar id diye.
    task_form = forms.Taskform(instance=task)#edit a click kore 1st a edit page niye ekta instance dekhabe.jekhane age the post er title,content thakbe.mane form fill up kora thakbe
    if request.method == 'POST':
        task_form = forms.Taskform(request.POST, instance=task)#request mane form user fillup korse
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')#edit kore submit korar pore homepage a niye jabe
     
    return render(request, 'addtask.html', {'form' : task_form})


def delete_task(request,id):
    task = models.Task.objects.get(pk=id)
    task.delete()
    return redirect('homepage')

# def complete_task(request, id):
#     task = models.Task.objects.get(pk=id)
#     task.is_completed = True
#     task.save()
#     return redirect('homepage')

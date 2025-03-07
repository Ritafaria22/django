from django.shortcuts import render,redirect
from . import forms 
from django.urls import reverse_lazy
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from django.utils.decorators import method_decorator #login required er kaj er jnno



@login_required
def add_post(request):
    if request.method == 'POST': #user post request koreche
        post_form = forms.Postform(request.POST)# user request er data ekhane store korlam
        if post_form.is_valid():#post kora data valid kina check korlam
           post_form.instance.author=request.user
           post_form.save()
           return redirect('add_post')
    else:#user normally website a gele blank form pabe
        post_form  = forms.Postform()
    return render(request, 'addpost.html', {'form' : post_form})


#addpost using class based view
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model=models.Post
    form_class= forms.Postform
    template_name= 'addpost.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model= models.Post
    form_class = forms.Postform
    template_name= 'addpost.html'
    pk_url_kwarg='id'
    success_url = reverse_lazy('profile')


@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model= models.Post
    template_name= 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg='id'


class DetailPostView(DetailView):
    model=models.Post
    pk_url_kwarg = 'id'
    template_name='post_details.html'

    def post(self,request, *args, **kwargs):
        comment_form =forms.Commentform(data=self.request.POST)
        post= self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post= post
            new_comment.save()
        return self.get(request, *args, **kwargs)
      

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        post=self.object
        comments = post.comments.all()
        comment_form=forms.Commentform()
       

        context['comments']=comments
        context['comment_form']=comment_form
        return context






@login_required
def edit_post(request,id):
    post = models.Post.objects.get(pk=id)#j post edit korte chai seta filter kore niye aslam.j post a click korbo setar id diye.
    post_form = forms.Postform(instance=post)#edit a click kore 1st a edit page niye ekta instance dekhabe.jekhane age the post er title,content thakbe.mane form fill up kora thakbe
    if request.method == 'POST':
        post_form = forms.Postform(request.POST, instance=post)#request mane form user fillup korse
        if post_form.is_valid():
            post_form.instance.author=request.user
            post_form.save()
            return redirect('homepage')#edit kore submit korar pore homepage a niye jabe
     
    return render(request, 'addpost.html', {'form' : post_form})

@login_required
def delete_post(request,id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')


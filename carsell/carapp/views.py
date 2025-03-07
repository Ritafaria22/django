from django.shortcuts import redirect,render
from django.utils.decorators import method_decorator
from . import forms 
from . import models
from .models import Purchase 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Purchase 


#using class based view
@method_decorator(login_required, name='dispatch')
class AddCarCreateView(DetailView):
    model = models.Car
    template_name = 'buycar.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_authenticated'] = self.request.user.is_authenticated
        return context

    def post(self, request, *args, **kwargs):
        car = self.get_object()
 
#using class based view
class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name ='cardetails.html'

    def post(self,request, *args, **kwargs):
        car= self.get_object()
        comment_form =forms.Commentform(data=self.request.POST)
        

        if 'buy_car' in request.POST:
            if car.quantity > 0:
                car.quantity -= 1  # Deduct one from the quantity
                car.save()  # Save the updated car object
                 # Create a Purchase record
                Purchase.objects.create(user=request.user, car=car)
                messages.success(request, f'You have successfully bought the car: {car.title}!')


            else:
                messages.error(request, 'Sorry, this car is currently out of stock.')

            return redirect('detail_car', id=car.id)  # Redirect back to the car details page

        
        
        
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post= car
            new_comment.user = request.user  # Set the user to the currently logged-in user
            new_comment.save()
        return self.get(request, *args, **kwargs)
      

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        car=self.object
        comments = car.comments.all()
        comment_form=forms.Commentform()
       

        context['comments']=comments
        context['comment_form']=comment_form
        return context

 
def buy_car(request, car_id):
    if request.method == "POST":
        print("Car purchased!")

    return HttpResponse(f"Car {car_id} has been purchased successfully!")

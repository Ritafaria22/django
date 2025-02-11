from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('form/', views.submit_form, name="submit_form"),
    #path('djangoform/', views.studentform, name="djangoform"),
    path('djangoform/', views.PasswordValidation, name="djangoform"),


]

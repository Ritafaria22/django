from django.urls import path,include
from . import views
urlpatterns = [
     
    path('',  views.home, name='home'),
    path('signup/',  views.signup, name='signup'),
    path('userlogin/',  views.userlogin, name='userlogin'),
    path('logout/',  views.user_logout, name='logout'),
    path('passchange/',  views.pass_change, name='passchange'),
    path('passchange2/',  views.pass_change2, name='passchange2'),
    path('profile/',  views.profile, name='profile'),
]

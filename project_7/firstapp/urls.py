from django.urls import path 
# from . import views
from firstapp.views import home

urlpatterns = [

    path('', home, name='homepage')
]
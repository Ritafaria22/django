from django.urls import path
from . import views 
urlpatterns = [
    
    path('add/', views.AddCarCreateView.as_view(), name='add_car'),
    path('details/<int:id>/', views.DetailCarView.as_view(), name='detail_car'),
    path('buy/<int:car_id>/', views.buy_car, name='buy_car'),
    
]

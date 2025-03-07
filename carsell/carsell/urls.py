from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('brand/<slug:brand_slug>/', views.home, name='brandwise_car' ),
    path('carapp/', include('carapp.urls')),
    path('userapp/', include('userapp.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
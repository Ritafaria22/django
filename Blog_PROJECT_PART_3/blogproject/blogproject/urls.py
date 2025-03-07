 
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('category/<slug:category_slug>/', views.home, name='category_wise_post'),
    path('author/', include('authorapp.urls')),
    path('post/', include('postapp.urls')),
    path('category/', include('categoriesapp.urls')),
]
 
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
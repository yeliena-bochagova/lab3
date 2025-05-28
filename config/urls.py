from django.contrib import admin
from django.urls import path
from . import views  # Імпортуємо view з config/views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
]
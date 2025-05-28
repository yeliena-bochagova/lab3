# crm/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Домашня сторінка з формою
    path('submit_request/', views.submit_request, name='submit_request'),
    path('client_list.html', views.client_list, name='client_list'),
    path('request_list.html', views.request_list, name='request_list'),
    path('create_request.html', views.create_request, name='create_request'),
    path('about.html', views.about, name='about'),
    path('about.html', views.about, name='about'),
    path('blog.html', views.blog, name='blog'),
    path('blog-single.html', views.blog_single, name='blog-single'),
    path('contact.html', views.contact, name='contact'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('pricing.html', views.pricing, name='pricing'),
    path('services.html', views.services, name='services'),
]
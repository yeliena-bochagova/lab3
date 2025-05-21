# crm/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # домашня сторінка
    path('client_list.html', views.client_list, name='client_list'),
    path('request_list.html', views.request_list, name='request_list'),
    path('create_request.html', views.create_request, name='create_request'),
    path('about.html', views.about, name='about'),
    path('blog.html', views.blog, name='blog'),
    path('blog-single.html', views.blog_single, name='blog-single'),
    path('contact.html', views.contact, name='contact'),
    #path('main.html', views.main, name='main_html'),
    #path('main/', views.main_page, name='main_page'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('pricing.html', views.pricing, name='pricing'),
    path('services.html', views.services, name='services'),
]
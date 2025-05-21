# crm/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # домашня сторінка
    path('about.html', views.about, name='about_html'),
    path('blog.html', views.blog, name='blog_html'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('contact.html', views.contact, name='contact_html'),
    #path('main.html', views.main, name='main_html'),
    #path('main/', views.main_page, name='main_page'),
    path('portfolio.html', views.portfolio, name='portfolio_html'),
    path('pricing.html', views.pricing, name='pricing_html'),
    path('services.html', views.services, name='services_html'),
]
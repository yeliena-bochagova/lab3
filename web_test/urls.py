# web_test/urls.py

from django.contrib import admin
from django.urls import path, include
from crm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),  # всі маршрути з crm беруться з окремого файлу
]
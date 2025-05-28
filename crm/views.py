from django.shortcuts import render, redirect
from .models import Client, ServiceRequest, ServiceType
from django import forms
from django.shortcuts import render, redirect
from .models import ServiceRequest
from django.utils import timezone
# Форма для створення заявки
class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['client', 'service_type', 'date', 'status']

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'crm/client_list.html', {'clients': clients})

def request_list(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'crm/request_list.html', {'requests': requests})

import logging
logger = logging.getLogger(__name__)

# Окрема view для обробки форми (submit_request)
def submit_request(request):
    if request.method == 'POST':
        logger.info("submit_request POST received: %s", request.POST)
        # або просто:
        print("POST data:", request.POST)
        # Отримуємо дані, які надсилає форма
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        service_name = request.POST.get('service')
        cleaner = request.POST.get('cleaner')

        # Створюємо або отримуємо клієнта за іменем (можна додатково використовувати phone)
        client, created = Client.objects.get_or_create(
            name=name,
            defaults={'phone': phone}
        )

        # Знаходимо ServiceType за ім'ям. Переконайся, що варіанти в select співпадають з іменами із бази.
        try:
            service_type = ServiceType.objects.get(name=service_name)
        except ServiceType.DoesNotExist:
            service_type = None

        if service_type:
            # Якщо дата не надсилається, можна використати поточний час
            ServiceRequest.objects.create(
                client=client,
                service_type=service_type,
                date=timezone.now(),  # або отримувати з форми, якщо є відповідне поле
                comment=f"Cleaner selected: {cleaner}",
                status='pending'  # за замовчуванням
            )
        # Після створення заявки переходимо до сторінки, де їх відображають
        return redirect('request_list')
    return redirect('index')

def create_request(request):
    if request.method == 'POST':
        client_id = request.POST.get('client')
        service_type_id = request.POST.get('service_type')
        date = request.POST.get('date')
        comment = request.POST.get('comment')

        # знайди об'єкти моделі
        client = Client.objects.get(id=client_id)
        service_type = ServiceType.objects.get(id=service_type_id)

        ServiceRequest.objects.create(
            client=client,
            service_type=service_type,
            date=date,
            comment=comment
        )
        return redirect('index')

    return redirect('index')

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def blog(request):
    return render(request, 'main/blog-single.html')

def blog_single(request):
    return render(request, 'main/blog-single.html')

def contact(request):
    return render(request, 'main/contact.html')

def main_page(request):
    return render(request, 'main/main.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def pricing(request):
    return render(request, 'main/pricing.html')

def services(request):
    return render(request, 'main/services.html')
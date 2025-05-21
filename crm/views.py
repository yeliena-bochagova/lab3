from django.shortcuts import render, redirect
from .models import Client, ServiceRequest, ServiceType
from django import forms
from django.shortcuts import render, redirect
from .models import ServiceRequest
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
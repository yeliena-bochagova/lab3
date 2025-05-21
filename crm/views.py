from django.shortcuts import render, redirect
from .models import Client, ServiceRequest, ServiceType
from django import forms

# Форма для створення заявки
class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['client', 'service_type', 'date', 'status']

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'crm/client_list.html', {'clients': clients})

def request_list(request):
    requests = ServiceRequest.objects.select_related('client', 'service_type').all()
    return render(request, 'crm/request_list.html', {'requests': requests})

def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'crm/create_request.html', {'form': form})


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def blog(request):
    return render(request, 'main/blog.html')

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
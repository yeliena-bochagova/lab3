from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['client', 'service_type', 'date', 'notes']  # поля, які потрібно виводити у формі

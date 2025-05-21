from django.test import TestCase
from django.urls import reverse
from ..models import Client, ServiceType, ServiceRequest
from django.utils import timezone
from datetime import timedelta

class ViewTests(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(
            name="Test Client",
            email="test@example.com",
            phone="1234567890",
            address="Test Address"
        )
        self.service_type = ServiceType.objects.create(
            name="Standard Cleaning",
            description="Standard cleaning service",
            price=100.00
        )
        self.service_request = ServiceRequest.objects.create(
            client=self.client_obj,
            service_type=self.service_type,
            date=timezone.now() + timedelta(days=1),
            status='pending',
            comment="Test comment"
        )

    def test_client_list_view(self):
        response = self.client.get(reverse('client_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crm/client_list.html')

    def test_request_list_view(self):
        response = self.client.get(reverse('request_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crm/request_list.html')

    def test_create_request_get(self):
        # Якщо твоя форма працює тільки через POST, тоді цей тест має просто перевіряти редирект
        response = self.client.get(reverse('create_request'))
        self.assertEqual(response.status_code, 302)

    def test_create_request_post(self):
        post_data = {
            'client': self.client_obj.id,
            'service_type': self.service_type.id,
            'date': '2025-07-01T10:00',
            'comment': 'Urgent request'
        }
        response = self.client.post(reverse('create_request'), data=post_data)
        self.assertEqual(response.status_code, 302)  # Очікується редирект
        self.assertEqual(ServiceRequest.objects.count(), 2)  # Була 1 в setUp, ще 1 зараз
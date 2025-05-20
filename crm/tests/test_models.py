from django.test import TestCase
from django.utils import timezone
from crm.models import Client, ServiceType, ServiceRequest

class ClientModelTest(TestCase):
    def test_create_client(self):
        client = Client.objects.create(
            name="Test User",
            email="test@example.com",
            phone="1234567890",
            address="Test Address"
        )
        self.assertEqual(client.name, "Test User")
        self.assertEqual(client.email, "test@example.com")

class ServiceTypeModelTest(TestCase):
    def test_create_service_type(self):
        service = ServiceType.objects.create(
            name="General Cleaning",
            description="Full cleaning service",
            price="150.00"
        )
        self.assertEqual(service.name, "General Cleaning")
        self.assertEqual(float(service.price), 150.00)

class ServiceRequestModelTest(TestCase):
    def test_create_service_request(self):
        client = Client.objects.create(
            name="Test Client",
            email="client@example.com",
            phone="0987654321",
            address="Client Address"
        )
        service_type = ServiceType.objects.create(
            name="Window Cleaning",
            description="Cleaning windows thoroughly",
            price="75.00"
        )
        now = timezone.now()
        request = ServiceRequest.objects.create(
            client=client,
            service_type=service_type,
            date=now,
            status="pending"
        )
        self.assertEqual(request.status, "pending")
        self.assertEqual(request.client, client)
        self.assertEqual(request.service_type, service_type)

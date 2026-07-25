from django.test import TestCase
from django.contrib.auth.models import User
from .models import Lead


class LeadTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            password="12345"
        )

    def test_create_lead(self):

        lead = Lead.objects.create(
            name="Rahul",
            email="rahul@gmail.com",
            phone="9876543210",
            company="ABC",
            source="Website",
            status="New",
            assigned_to=self.user,
            created_by=self.user,
        )

        self.assertEqual(lead.name, "Rahul")

class LeadModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            password="123456"
        )

    def test_create_lead(self):
        lead = Lead.objects.create(
            name="Rahul",
            email="rahul@gmail.com",
            phone="9876543210",
            company="ABC",
            source="Website",
            status="New",
            assigned_to=self.user,
            created_by=self.user,
        )

        self.assertEqual(lead.name, "Rahul")
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from leads.models import Lead
from .serializers import LeadSerializer


class LeadListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    # Add these here
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]

    filterset_fields = [
        "status",
        "assigned_to",
    ]

    search_fields = [
        "name",
        "company",
        "email",
    ]

    def get_queryset(self):

        user = self.request.user

        if user.groups.filter(name="Admin").exists():
            return Lead.objects.all().order_by("-created_at")

        return Lead.objects.filter(
            assigned_to=user
        ).order_by("-created_at")


class LeadRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):

    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user

        if user.groups.filter(name="Admin").exists():
            return Lead.objects.all()

        return Lead.objects.filter(
            assigned_to=user
        )
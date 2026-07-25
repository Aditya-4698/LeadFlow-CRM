from django.urls import path
from .views import (
    LeadListCreateAPIView,
    LeadRetrieveUpdateDestroyAPIView,
)

urlpatterns = [

    path(
        "leads/",
        LeadListCreateAPIView.as_view(),
        name="api_leads",
    ),

    path(
        "leads/<int:pk>/",
        LeadRetrieveUpdateDestroyAPIView.as_view(),
        name="lead-detail",
    ),
]
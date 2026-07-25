from django.db import models
from django.contrib.auth.models import User
from leads.models import Lead


class Activity(models.Model):

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    action = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action
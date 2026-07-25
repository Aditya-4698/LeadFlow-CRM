from django import forms
from .models import Lead, Note
from django.contrib.auth.models import User


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = [
            "name",
            "email",
            "phone",
            "company",
            "source",
            "status",
            "assigned_to",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "company": forms.TextInput(attrs={"class": "form-control"}),
            "source": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "assigned_to": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["assigned_to"].queryset = User.objects.filter(
            groups__name="member"
        )


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ["note"]

        widgets = {
            "note": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Write a note..."
                }
            )
        }
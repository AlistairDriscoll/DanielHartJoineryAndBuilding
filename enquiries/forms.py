from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ["name", "email", "location", "job_title", "description"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control", "placeholder": "Your full name"
                    }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control", "placeholder": "you@example.com"
                    }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control", "placeholder": " i.e. Leeds, LS7"
                    }
            ),
            "job_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": " i.e. Kitchen extension"
                    }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Brief description of the job…",
                }
            ),
        }
        labels = {
            "job_title": "Job title",
        }

    def clean_description(self):
        text = self.cleaned_data["description"].strip()
        if len(text) < 10:
            raise forms.ValidationError(
                "Please add a bit more detail (at least 10 characters)."
            )
        return text

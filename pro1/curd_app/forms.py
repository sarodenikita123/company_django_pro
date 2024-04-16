from django import forms
from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

        widgets = {
            "Title": forms.TextInput(attrs={"class": "form-control"}),
            "company": forms.TextInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "job_function": forms.RadioSelect(),
            "training_date": forms.DateInput(attrs={"type": "date"}),
            "dietary_requirement": forms.TextInput(attrs={"class": "form-control"}),
            "exceptions": forms.TextInput(attrs={"class": "form-control"})
        }



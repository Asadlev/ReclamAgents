from django import forms

from .models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company

        fields = [
            'name',
            'slug',
            'address',
            'description',
            'contact_info',
            'unique_code',
            'image',
            'category',
        ]



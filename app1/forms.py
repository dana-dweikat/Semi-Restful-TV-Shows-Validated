
from django import forms

from .models import Show


class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ["title", "network", 'release_date', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'network': forms.TextInput(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

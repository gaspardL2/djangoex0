from django import forms
from .models import Countries

class CountryForm(forms.ModelForm):

    class Meta:
        model = Countries
        fields = ['name', 'area']
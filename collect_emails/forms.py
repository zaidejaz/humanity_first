from django import forms
from .models import Supporter

class SupporterForm(forms.ModelForm):
    class Meta:
        model = Supporter
        fields = ['name', 'email', 'phone_number']

from django import forms
from .models import Bnda
class PersonRegistration(forms.ModelForm):
    class Meta:
        model = Bnda
        fields = ['name', 'bill', 'paidDate']
   
from django import forms

class PersonRegistration(forms.Form):
    name=forms.CharField()
    bill=forms.IntegerField()
    paidDate=forms.DateInput()
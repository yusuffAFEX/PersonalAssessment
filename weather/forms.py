from django import forms


class VisitorForm(forms.Form):
    email = forms.EmailField()
    location = forms.CharField(max_length=200)

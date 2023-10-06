from django import forms
from .models import Bundle, Link

class BundleForm(forms.ModelForm):
    class Meta:
        model = Bundle
        fields = ['name', 'password']

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url']

class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

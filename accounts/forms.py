from django import forms

class UserLoginForm(forms.Form):
    """Form to be used by login users"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
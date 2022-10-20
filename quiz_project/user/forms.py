from django import forms
from .models import UserDb, Options, SetofQuestions


class UserForm(forms.ModelForm):
    class Meta:
        model = UserDb
        fields = ['first_name', 'last_name', 'email', 'password']
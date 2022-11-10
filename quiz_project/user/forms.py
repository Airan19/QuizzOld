from django import forms
from .models import UserDb, Options, SetofQuestions


class UserForm(forms.ModelForm):
    class Meta:
        model = UserDb
        fields = ['first_name', 'last_name', 'email', 'password']


class OptionsForm(forms.ModelForm):
    class Meta:
        model = Options
        fields = ['opt']


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = SetofQuestions
        fields = ['question', 'answer', 'options', 'tags', 'date_created']


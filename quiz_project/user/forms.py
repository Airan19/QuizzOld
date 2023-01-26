from django import forms
from .models import User, Options, SetofQuestions


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']


class OptionsForm(forms.ModelForm):
    class Meta:
        model = Options
        fields = ['opt']


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = SetofQuestions
        fields = ['question', 'answer', 'options', 'tags', 'date_created']


from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'email')
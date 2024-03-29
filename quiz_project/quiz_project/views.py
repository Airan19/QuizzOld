from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from user.models import *
from user.forms import UserForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic.detail import DetailView
from django.conf import settings
import requests

def dashboard(request):
    # user = request.GET['user']
    user = request.user
    return render(request, 'index.html', {'user':user})


def landing_page(request):
    return render(request, 'home.html')


def home(request):
    if request.method == 'POST':
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''
        if result['success']:
            messages.success(request, 'New comment added with success!')
        # return redirect('comments')
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'username or password not correct')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')

        return redirect('home')
    return render(request, 'login.html')


def about_us(request):
    return render(request, 'about.html')


def signup_redirect(request):
    messages.error(request, "Something wrong here, it may be that you already have account!")
    return redirect("dashboard")


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def contact_us(request):
    return render(request, 'contact.html')


def delete(request, id):
    item = User.objects.get(id=id)
    item.delete()
    messages.success(request, 'User removed successfully.')
    return redirect('home')


# def logout(request):
#     logout(request.user)
#     return redirect('home')
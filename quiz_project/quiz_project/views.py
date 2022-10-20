from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from user.models import *
from user.forms import UserForm


def dashboard(request):
    user = request.GET['user']
    return render(request, 'index.html', {'user':user})


def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_db = UserDb.objects.filter(email=email).first()
        if user_db:
            if user_db.password == password:
                user = user_db.first_name + ' ' + user_db.last_name
                url = '/dashboard?user={}'.format(user)  ##just for temporary use.
                return redirect(url)
            # else:

        return redirect('home')
        # return render(request, 'home.html', {'username':email, 'password':password})
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about.html')


def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        user = first_name + ' ' + last_name
        url = '/dashboard?user={}'.format(user) ##just for temporary use.
        return redirect(url)
    return render(request, 'signup.html')
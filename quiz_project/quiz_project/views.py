from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from user.models import *
from user.forms import UserForm
from django.contrib import messages


def dashboard(request, user_id):
    # user = request.GET['user']
    user = UserDb.objects.get(id=int(user_id))
    return render(request, 'index.html', {'user':user})

def landing_page(request):
    return render(request, 'home.html')


def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_db = UserDb.objects.filter(email=email).first()
        print(user_db)
        if user_db:
            if user_db.password == password:
                user_id = user_db.id
                return redirect('dashboard', user_id)
        else:
            messages.error(request, 'username or password not correct')

        return redirect('home')
        # return render(request, 'home.html', {'username':email, 'password':password})
    return render(request, 'login.html')


def about_us(request):
    return render(request, 'about.html')


def sign_up(request):
    if request.method == 'POST':
        print(request.POST)
        return
        form = UserForm(request.POST or None)
        if form.is_valid():
            print(UserDb.objects.all())
            form.save()
            print(UserDb.objects.all())
            messages.success(request, ('Successfully signed-up.'))
            user = 'dummy'
            return render(request, 'index.html', {'user': user})
    return render(request, 'signup.html')


def delete(request, id):
    item = UserDb.objects.get(id=id)
    item.delete()
    messages.success(request, 'User removed successfully.')
    return redirect('home')
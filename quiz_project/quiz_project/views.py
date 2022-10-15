from django.shortcuts import render
from django.http import HttpResponseRedirect


def task(request):
    return render(request, 'index.html')


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        return render(request, 'home.html', {'username':username, 'password':password})
    # if request.method == "POST":
    #     pDict = request.POST.copy()
    #     form = EmployeeForm(pDict)  # if not valid shows error with previous post values in corresponding field
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('')
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about.html')

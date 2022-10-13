from django.shortcuts import render
from django.http import HttpResponse

def home_view(request,*args,**kwargs):
  return render(request,"about.html",{})

#def index(request):
#    return HttpResponse("Hello world!")
# Create your views here.

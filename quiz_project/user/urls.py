from . import views   ## './dot' here means the file we are importing is in the same folder.
from django.urls import path

urlpatterns = [
    path('', views.about_view,name='about'),
]
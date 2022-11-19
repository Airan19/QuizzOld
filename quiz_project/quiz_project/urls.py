"""quiz_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views   ## './dot' here means the file we are importing is in the same folder.
from django.urls import path , include
# from user import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('contact', views.contact_us, name='contact_us'),
    path('login', views.home, name='home'),
    path('dashboard/<user_id>', views.dashboard, name='dashboard'),
    path('about/',include('user.urls'),name='about'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('delete/<id>', views.delete, name='delete'),
]


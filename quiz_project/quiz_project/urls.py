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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('user.urls')),
    path('accounts/', include('allauth.urls')),
    path('social/signup/', views.signup_redirect, name='signup_redirect'),
    path('', views.landing_page, name='landing_page'),
    path('contact/', views.contact_us, name='contact_us'),
    path('home', views.home, name='home'),
    path('dashboard/', login_required(views.dashboard), name='dashboard'),
    path('about/',views.about_us,name='about'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('delete/<id>', login_required(views.delete), name='delete'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    # path('profile/', login_required(UserView.as_view()), name='profile'),
    # path('signup/', sign_up, name='signup'),
]


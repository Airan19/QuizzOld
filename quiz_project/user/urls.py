# from . import views   ## './dot' here means the file we are importing is in the same folder.
# from django.urls import path
#
# urlpatterns = [
#     path('', views.about_view,name='about'),
# ]
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = 'user'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    # path("password_reset", views.password_reset_request, name="password_reset"),
    # path('profile/',  login_required(UserView.as_view(template_name='login.html')), name='profile'),
    # path('signup/', signup, name='signup')
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
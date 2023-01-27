# # from django.shortcuts import render
# # # from django.http import HttpResponse
# #
# # def about_view(request,*args,**kwargs):
# #   return render(request,"about.html",{})
# #
# # #def index(request):
# # #    return HttpResponse("Hello world!")
# # # Create your views here.
#
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.views.generic.detail import DetailView
#
# from .forms import SignUpForm
#
#
# class UserView(DetailView):
#   template_name = 'users/profile.html'
#
#   def get_object(self):
#     return self.request.user
#
#
# def landing_page(request):
#   return 'working...'
#   # return render(request, '../templates/home.html')
#
#
# def signup(request):
#     if request.method == 'POST':
#       form = SignUpForm(request.POST)
#       if form.is_valid():
#         print('USERS valid k andrr takk')
#         user = form.save()
#         raw_password = form.cleaned_data.get('password1')
#         user = authenticate(request, email=user.email, password=raw_password)
#         if user is not None:
#           login(request, user)
#         else:
#           print("user is not authenticated")
#         return redirect('users:profile')
#     else:
#       form = SignUpForm()
#     return render(request, 'users/signup.html', {'form': form})
#
# def profile(request):
#   return 'redirected to profile'

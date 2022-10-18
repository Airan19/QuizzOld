from django.contrib import admin
from .models import  UserDb, Options, SetofQuestions, Tags
# Register your models here.

admin.site.register(UserDb)
admin.site.register(Options)
admin.site.register(SetofQuestions)
admin.site.register(Tags)

from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class userModel(UserAdmin):
    list_display = ['username', 'user_type']

admin.site.register(CustomUser, userModel)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)

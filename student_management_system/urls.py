from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, Hod_Views, Staff_Views, Student_Views

urlpatterns = [
                  
                  path('base/', views.BASE, name='base'),
                  path('temp',views.temp),
                  #Login path
                  path('', views.LOGIN, name='login'),
                  path("capture",views.camera,name='capture'),
                  path('doLogin', views.doLogin, name='doLogin'),
                  path('doLogout', views.doLogout, name='logout'),


                  #Profile Update
                  path('Profile', views.PROFILE, name='profile'),
                  path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

                  #This is HOD Panel URL
                  path('Hod/Home', Hod_Views.HOME, name='hod_home'),
                  path('Hod/Student/Add', Hod_Views.ADD_STUDENT, name='add_student'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

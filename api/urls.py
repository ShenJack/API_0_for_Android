from django.conf.urls import url
from django.contrib import admin

from api import views

urlpatterns = [
    url(r'^login/',views.LoginUser,name='login'),
    url(r'^register/',views.CreateUser,name='register'),
    url(r'^list/',views.ListUser,name='list' ),

]
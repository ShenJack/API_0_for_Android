from django.conf.urls import url
from django.contrib import admin

from api import views

urlpatterns = [
    url(r'^login/', views.loginUser, name='login'),
    url(r'^register/', views.createUser, name='register'),
    url(r'^list/', views.listUser, name='list'),

]
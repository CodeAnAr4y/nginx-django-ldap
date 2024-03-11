from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('connect_to_ldap', connect_to_ldap, name='connect_to_ldap'),
]
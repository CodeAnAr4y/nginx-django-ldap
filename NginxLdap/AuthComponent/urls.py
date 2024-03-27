from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('login', login_view),
    path('logout', logout_view),
    path('auth', authorize_view)
]
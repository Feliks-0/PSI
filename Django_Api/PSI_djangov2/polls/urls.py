from django.urls import path
from .api import *
from . import views

urlpatterns = [
    path('api', Generic_Api.as_view()),
    path('zmarli_api', Zmarli_Api.as_view()),
    path('user_api', ListUsers.as_view() )
]
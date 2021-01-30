from django.urls import path
from .api import Dead_Api,ListUsers
from . import views

urlpatterns = [
    path('api', Dead_Api.as_view()),
    path('api2', ListUsers.as_view() )
]
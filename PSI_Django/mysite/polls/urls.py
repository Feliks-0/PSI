from django.urls import path
from .api import *
from . import views

urlpatterns = [

    path('Dead_people', Dead_peopleList.as_view(), name=Dead_peopleList.name),
    path('Dead_people-detail/<int:pk>', Dead_peopleDetail.as_view(), name=Dead_peopleDetail.name),
    path('Nagrobki', NagrobkiList.as_view(), name=NagrobkiList.name),
    path('Nagrobki-detail/<int:pk>', NagrobkiDetail.as_view(), name=NagrobkiDetail.name),
    path('user_api', ListUsers.as_view()),
    path('', ApiRoot.as_view(), name=ApiRoot.name)
]

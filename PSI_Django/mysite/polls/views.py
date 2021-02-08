from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


from . import models
from . import serializers


@api_view(["GET"])
def home(request):
    return Response({"message":"Welcome Home!"},
                    status=status.HTTP_200_OK)



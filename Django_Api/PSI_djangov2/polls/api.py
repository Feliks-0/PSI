from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import Nagrobki as ns
from .serializers import Dead_people as ds
from .models import Nagrobki,Dead_people
class Generic_Api(generics.ListCreateAPIView):
    queryset = Dead_people.objects.all()
    serializer_class = ds

class Zmarli_Api(APIView):
    queryset = Dead_people.objects.all()
    serializer_class = ds

class ListUsers(APIView):
    """
    View to list all users in the system.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)



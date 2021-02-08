from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import Nagrobki as ns
from .serializers import Dead_people as ds
from .models import Nagrobki, Dead_people
from rest_framework.reverse import reverse


class Dead_peopleList(generics.ListCreateAPIView):
    queryset = Dead_people.objects.all()
    serializer_class = ds
    name = "Dead_people"

class Dead_peopleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dead_people.objects.all()
    serializer_class = ds
    name = 'Dead_people-detail'


class NagrobkiList(generics.ListCreateAPIView):
    queryset = Nagrobki.objects.all()
    serializer_class = ns
    name = "Nagrobki"



class NagrobkiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nagrobki.objects.all()
    serializer_class = ns
    name = "Nagrobki-detail"


class ListUsers(APIView):
    """
    View to list all users in the system.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'Dead_people': reverse(Dead_peopleList.name, request=request),
                         'Nagrobki': reverse(NagrobkiList.name, request=request)
                         })

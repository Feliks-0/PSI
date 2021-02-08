from rest_framework import serializers
from . import models


class Dead_people(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=models.Dead_people.GENDER_CHOICES)
    class Meta:
        model = models.Dead_people
        fields = ['gender','Imie','Nazwisko','Data_uro','Data_smier']


class Nagrobki(serializers.ModelSerializer):
    dead_people = serializers.SlugRelatedField(queryset=models.Dead_people.objects.all(), slug_field='idDead_people')
    class Meta:
        model = models.Nagrobki
        fields = ['Sektor','Rzad','Miejsce_rzad','Wiadomosc','dead_people']
    #Sektor = serializers.CharField(max_length=2)
    #Rzad = serializers.CharField(max_length=2)
    #Miejsce_rzad = serializers.IntegerField(default=0)
    #Wiadomosc = serializers.CharField(max_length=60)

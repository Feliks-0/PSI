from rest_framework import serializers
from .models import Dead_people

class Dead_people(serializers.ModelSerializer):
    class Meta:
        model = Dead_people
        fields = ['idDead_peopl', 'Imie', 'Nazwisko', 'Data_uro', 'Data_smier']


class Nagrobki(serializers.Serializer):
    Sektor = serializers.CharField(max_length=10)
    Rzad = serializers.CharField(max_length=10)
    Miejsce_rzad = serializers.IntegerField(default=0)
    Wiadomosc = serializers.CharField(max_length=60)
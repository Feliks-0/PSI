from django.db import models




class Dead_people(models.Model):
    idDead_people = models.AutoField(primary_key=True)
    Imie = models.CharField(max_length=15)
    Nazwisko = models.CharField(max_length=20)
    Data_uro = models.DateField()
    Data_smier = models.DateField()

class Nagrobki(models.Model):
    idNagrobki = models.AutoField(primary_key=True)
    Sektor = models.CharField(max_length=10)
    Rzad = models.CharField(max_length=10)
    Miejsce_rzad = models.IntegerField(default=0)
    Wiadomosc = models.CharField(max_length=60)
    Dead_people_idDead_people = models.ForeignKey(Dead_people, on_delete=models.CASCADE)

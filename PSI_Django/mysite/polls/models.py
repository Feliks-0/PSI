from django.db import models




class Dead_people(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'),)
    idDead_people = models.AutoField(primary_key=True)
    Imie = models.CharField(max_length=15)
    Nazwisko = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    Data_uro = models.DateField()
    Data_smier = models.DateField(blank=True, null=True)

class Nagrobki(models.Model):
    idNagrobki = models.AutoField(primary_key=True)
    Sektor = models.CharField(max_length=2)
    Rzad = models.CharField(max_length=2)
    Miejsce_rzad = models.IntegerField(default=0)
    Wiadomosc = models.CharField(max_length=60)
    dead_people = models.ForeignKey(Dead_people, on_delete=models.CASCADE)

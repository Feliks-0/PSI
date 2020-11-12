
#ZAD 1
def Wypisz (a_list,b_list):
    print("indeksy parzyste listy a:")
    for i in a_list:
        if i%2==0:
            print(a_list[i])
    print("indeksy nieparzyste listy b:")
    for j in b_list:
        if j%2!=0:
            print(b_list[j])

a_list = [0,1,2,3,4,5,6,7,8,9]
b_list = [0,1,2,3,4,5,6,7,8,9]
Wypisz(a_list,b_list)

#ZAD 2
def Slownik(data_text):
    duze =[]
    male =[]
    for i in data_text:
        if i.isupper():
            duze.append(i)
        else:
            male.append(i)
    info = {'length':len(data_text),'letters':list(data_text),'big_letters':duze,'small_letters':male}
    print(info)

txt = "bAduM K"
Slownik(txt)

#ZAD 3
def Sprawdz(text,letter):
    tex = list(text)
    tex.remove(letter)
    print(tex)
Sprawdz(txt,'A')

#ZAD 4
def Temperatura(celcjusz):
    print("Kelviny:{0}".format(celcjusz-273.15))
    print("Fahrenheity:{0}".format(celcjusz*1.8+32))
    print("Fahrenheity:{0}".format(celcjusz*1.8+491.67))
Temperatura(0)

#ZAD 5
class Calculator:
    def Dodaj(self,in1,in2):
        return in1 + in2
    def Usun(self,in1,in2):
        return in1 - in2
    def Mnoz(self,in1,in2):
        return in1 * in2
    def Dziel(self,in1,in2):
        return in1 / in2


#ZAD 6
class ScienceCalculator(Calculator):
    def Potega(self,in1,in2):
        return in1**in2
kalk = ScienceCalculator()
a=2
b=7
print(kalk.Dodaj(a,b))
#ZAD 7
def Odwrot(text):
    print(text[::-1])
Odwrot("koteł")
#ZAD 8
class FileManager:
    def __init__(self, file):
        self.file=file

    def updatef(self, text):
        plik=open(self.file, 'a' ,encoding='utf-8')
        plik.write(text)

    def readf(self):
        zapis = open(self.file, 'r', encoding='utf-8')
        while True:
            dane = zapis.read(1024)
            print(dane, end='')
            if not dane:
                zapis.close()
                break
#ZAD 9
from CW_02 import *
plik = FileManager('plik.txt')
FileManager.updatef(plik,'Witam dodaje tekst')
plik.readf()
#ZAD 10
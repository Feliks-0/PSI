pierwsze = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. "\
           "Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. "\
           "Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. "\
           "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających "\
           "fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem "\
           "przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Piotr"
nazwisko = "Pawlukowski"
litera1 = imie[2]
litera2 = nazwisko[3]
liczba_liter1 = pierwsze.count(litera1)
liczba_liter2 = pierwsze.count(litera2)
print(f"W tekście jest {liczba_liter1} liter {litera1} oraz {liczba_liter2} liter {litera2}")
imie_no = imie[::-1]
nazwisko_no = nazwisko[::-1]
print(imie_no.capitalize())
print(nazwisko_no.capitalize())

tablica = [i for i in range(1,11)]
pier = tablica[:5]
drug = tablica[5:]
print(pier, drug)

cale = [0]
cale += pier + drug
cale.reverse()
print(cale)

lista_studentow = ("Romeo Rini", 164545), ("Cibe Cibelli", 156877), ("Feliks lavida", 134515)
print(lista_studentow)

slownik_list_stud = dict(lista_studentow)
print(slownik_list_stud)

tab11 = [i for i in range(1,11)]
print(tab11)

tab12 = [i for i in range(100,20,-5)]
print(tab12)

#Zadanie 1
akapit = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
#Zadanie 2
liczba_lit = [akapit.count('f'),akapit.count('e'),akapit.count('o'),akapit.count('l'),akapit.count('s')]
print("W tekście jest {0} liter f, {1} liter e, {2} liter o, {3} liter l, {4} liter s ".format(liczba_lit[0],liczba_lit[1],liczba_lit[2],liczba_lit[3],liczba_lit[4]))
#Zadanie 5
prowadzacy = "Ikswezslo Skilef"
prawda = prowadzacy[::-1]
imie = slice(6)
nazwisko = slice(7,16)
print(prawda[imie].capitalize(),prawda[nazwisko].capitalize())
#Zadanie 6
tablica = [i for i in range(1,11)]
pier = tablica[:5]
drug = tablica[5:]
print(pier, drug)
#Zadanie 7
cale = [0]
cale += pier + drug
cale.reverse()
print(cale)
#Zadanie 8
lista_studentow = ("Patryk Baranowski", 142345),("Maciek Balkonowski", 152775),("Konrad calkowski", 122375)
print(lista_studentow)
#Zadanie 9
slownik_list_stud = dict(lista_studentow)
print(slownik_list_stud)
#Zadanie 11
tab11 = [i for i in range(1,11)]
print(tab11)
#Zadanie 12
tab12 = [i for i in range(100,20,-5)]
print(tab12)
#Zadanie 13



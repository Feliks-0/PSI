def Wypisz (a_list, b_list):
    print("indeksy parzyste listy a:")
    for i in a_list:
        if i % 2 == 0:
            print(a_list[i])
    print("indeksy nieparzyste listy b:")
    for j in b_list:
        if j % 2 != 0:
            print(b_list[j])


a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Wypisz(a_list,b_list)


def Slownik(data_text):
    duze =[]
    male =[]
    for i in data_text:
        if i.isupper():
            duze.append(i)
        else:
            male.append(i)
    info = {'length' : len(data_text),'letters':list(data_text), 'big_letters': duze, 'small_letters': male}
    print(info)


txt = "MonKAs XDd"
Slownik(txt)


def sprawdz(text, letter):
    tex = list(text)
    tex.remove(letter)
    print(tex)


sprawdz(txt, 'd')


def temperatura(celcjusz):
    print("Kelviny:{0}".format(celcjusz-273.15))
    print("Fahrenheity:{0}".format(celcjusz*1.8+32))
    print("Rankine:{0}".format(celcjusz*1.8+491.67))


temperatura(30)


class calculator:

    def dodaj(self, in1, in2):
        return in1 + in2

    def od(self, in1, in2):
        return in1 - in2

    def mnoz(self, in1, in2):
        return in1 * in2

    def dziel(self, in1, in2):
        return in1 / in2


class scienceCalculator(calculator):
    def potega(self, in1, in2):
        return in1**in2


calc = scienceCalculator()
a = 6
b = 3
print(calc.mnoz(a, b))


def odwrot(text):
    print(text[::-1])


odwrot("zwiedzać")
import sys

operacje = ("wychowawca", "nauczyciel", "uczen", "koniec")

wychowawcy = []
nauczyciele = []
uczniowie = []
grupy = {}


def wydruk(argument):
    if argument in wychowawcy:
        print(wychowawcy)
    if argument in nauczyciele:
        print(nauczyciele)
    if argument in uczniowie:
        print(uczniowie)
    if argument in klasy: 
        print(f"wychowawca:\n{klasy[argument][0]} \nuczniowie:")
        for osoba in klasy[argument][1:]:
            print(osoba)


class Grupa:
    def __init__(self,numer):
        self.numer = numer
        self.wychowawca = None
        self.nauczyciele = []
        self.uczniowie  = []

def dodanie_grupy(numer):
    if numer not in grupy:
        grupa = Grupa(numer)
        grupy[numer] = grupa  
    return grupy[numer]           


class Wychowawca:
    def __init__(self):
        self.imie = ""
        self.klasy = []

    def pobor_danych(self):
        self.imie = input()
        wychowawcy.append(self.imie)
        klasy = []
        while True:
            klasa = input()
            if not klasa:
                break    
            self.klasy.append(klasa)
            #grupa = dodanie_grupy(self.klasa)
            #grupa.wychowawca = self      


class Nauczyciel:
    def __init__(self):
        self.imie = ""
        self.przedmiot = ""
        self.klasy = []

    def pobor_danych(self):
        self.imie = input()
        nauczyciele.append(self.imie)
        self.przedmiot = input()
        klasy = []
        while True:
            klasa = input()
            if not klasa:
                break    
            self.klasy.append(klasa)
            #grupa = dodanie_grupy(self.klasa)
            #grupa.nauczyciele.append(self)


class Uczen:
    def __init__(self):
        self.imie = ""
        self.klasa = ""

    def pobor_danych(self):
        self.imie = input()
        uczniowie.append(self.imie)
        self.klasa = input()    
        grupa = dodanie_grupy(self.klasa)
        grupa.uczniowie.append(self)

while True:
    typ = input()
    if typ not in operacje:
        print("blad")
        continue
    if typ == "wychowawca":
        osoba = Wychowawca()
    if typ == "nauczyciel":
        osoba = Nauczyciel()
    if typ == "uczen":
        osoba = Uczen()        
    if typ == "koniec":
        break 
    osoba.pobor_danych()


if len(sys.argv) !=2:
    print("Nie podano prawidłowej funkcji programu")    
else:
    komenda = sys.argv[1]
    if komenda in grupy:
        #print(grupy[komenda])
        print("klasa")
    if komenda in wychowawcy:
        print("wychow")
    if komenda in nauczyciele: 
        print("naucz")
    if komenda in uczniowie:
        print("uczen")

#print(dir(grupy))

#print(grupy.__contains__)


import sys

operacje = ("wychowawca", "nauczyciel", "uczen", "koniec")

wychowawcy = []
wychowawcy2 = {}
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

class Wychowawca:
    def __init__(self):
        self.imie = ""
        self.klasy = []

    def pobor_danych(self):
        self.imie = input()
        klasy = []
        while True:
            klasa = input()
            if not klasa:
                break    
            self.klasy.append(klasa)
            
    

class Nauczyciel:
    def __init__(self):
        self.imie = ""
        self.przedmiot = ""
        self.klasy = []

    def pobor_danych(self):
        self.imie = input()
        self.przedmiot = input()
        klasy = []
        while True:
            klasa = input()
            if not klasa:
                break    
            self.klasy.append(klasa)
            print("klasy")


class Uczen:
    def __init__(self):
        self.imie = ""
        self.klasa = ""

    def pobor_danych(self):
        self.imie = input()
        self.klasa = input()    


while True:
    typ = input()

    if typ not in operacje:
        print("blad")
        continue

    if typ == "wychowawca":
        osoba = Wychowawca()
        osoba.pobor_danych()
        wychowawcy.append(osoba)

    if typ == "nauczyciel":
        osoba = Nauczyciel()
        osoba.pobor_danych()
        nauczyciele.append(osoba)

    if typ == "uczen":
        osoba = Uczen()
        osoba.pobor_danych()
        uczniowie.append(osoba)
      
    if typ == "koniec":
        break 
    

if len(sys.argv) !=2:
    print("Nie podano prawidłowej funkcji programu")    
else:
    wydruk(sys.argv[1])

   
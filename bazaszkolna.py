import sys

wychowawcy = set()
nauczyciele = set()
uczniowie = set()
klasy = set()

def wydruk(argument):
    if argument in wychowawcy:

    if argument in nauczyciele:

    if argument in uczniowie:

    if argument in klasy    





class Grupa:
    def __init__(self):
        


class Wychowawca:
    def __init__(self,imie,klasa):
        self.imie = imie
        self.klasa = klasa

    def pobor_danych(self):
        self.imie = input()
        while True:
            klasa = input()
            if not klasa:
                break
            self.klasa = klasa
            
    def wydruk(self):
    

clas Nauczyciel:
    def __init__(self):
        self.imie = ""
        self.przedmiot = ""
        self.klasa = []


class Uczen:
    def __init__(self):
        self.imie = ""
        self.klasa = ""





while True:
    typ = input()
    if typ not in operacje:
        continue
    if typ == "wychowawca":
    if typ == "nauczyciel":
    if typ == "uczen":
    if typ == "koniec":
        break 



if len(sys.argv) !=2:
    print("Nie podano funkcji programu")    
else:
    wydruk(sys.argv[1])

      
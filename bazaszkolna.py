import sys

operacje = ("wychowawca", "nauczyciel", "uczen", "koniec")

#baza={}
wychowawcy = {}
nauczyciele = {}
uczniowie = {}
grupy = {}

if len(sys.argv) !=2:
    print("Nie podano prawidłowej funkcji programu")  
    phrase = None
else:
    phrase = sys.argv[1]
    

class Grupa:
    def __init__(self,numer):
        self.numer = numer
        self.wychowawca = None
        self.nauczyciele = []
        self.uczniowie  = []
    
    def wydruk(self):
        print(f"wychowawcą klasy {phrase} jest {self.wychowawca.imie}")
        print("uczęszczają do niej uczniowie:")
        for uczen in self.uczniowie:
            print(f"- {uczen.imie}")

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
        while True:
            klasa = input()
            if not klasa:
                break    
            self.klasy.append(klasa)
            grupa = dodanie_grupy(klasa)
            grupa.wychowawca = self  

    def wydruk(self): 
        for klasa in self.klasy:
            print(
            f"\nNauczyciel {self.imie} jest wychowawcą klasy {klasa},\nuczniowie:"
            )
            for uczen in grupy[klasa].uczniowie:
                print(f"- {uczen.imie}")


class Nauczyciel:
    def __init__(self):
        self.imie = ""
        self.przedmiot = ""
        self.klasy = []

    def pobor_danych(self):
        self.imie = input()
        self.przedmiot = input()
        while True:
            klasa = input()
            if not klasa:
                break    
            self.klasy.append(klasa)
            grupa = dodanie_grupy(klasa)
            grupa.nauczyciele.append(self)

    def wydruk(self): 
        for klasa in self.klasy:
            if grupy[klasa].wychowawca:
                print(f"wychowawca klasy {klasa} - {grupy[klasa].wychowawca.imie}")
            else:
                print(f"klasa {klasa} nie ma wychowawcy")


class Uczen:
    def __init__(self):
        self.imie = ""
        self.klasa = ""

    def pobor_danych(self):
        self.imie = input()
        self.klasa = input()    
        grupa = dodanie_grupy(self.klasa)
        grupa.uczniowie.append(self)

    def wydruk(self): 
        print(f"\nUcznia {phrase} prowadzą:")
        for nauczyciel in grupy[self.klasa].nauczyciele:
            print(f"- {nauczyciel.imie} - {nauczyciele[nauczyciel.imie].przedmiot}")

while True:         #główna pętla
    typ = input()
    if typ not in operacje:
        print("blad")
        continue
    if typ == "koniec":
        break 
    if typ == "wychowawca":
        osoba = Wychowawca()
        osoba.pobor_danych()
        wychowawcy[osoba.imie]=osoba
    if typ == "nauczyciel":
        osoba = Nauczyciel()
        osoba.pobor_danych()
        nauczyciele[osoba.imie]=osoba
    if typ == "uczen":
        osoba = Uczen() 
        osoba.pobor_danych() 
        uczniowie[osoba.imie]=osoba

"""    osoba.pobor_danych()
    if not baza.get(osoba.imie):
        baza[osoba.imie]=osoba
    baza[osoba.imie+"2"]=osoba"""

if phrase in nauczyciele:
    nauczyciele[phrase].wydruk()
if phrase in wychowawcy:
    wychowawcy[phrase].wydruk()
if phrase in uczniowie:
    uczniowie[phrase].wydruk()
if phrase in grupy:
    grupy[phrase].wydruk()   
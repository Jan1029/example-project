class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto,
                 ubezpieczenie_emerytalne, ubezpieczenie_rentowe, ubezpieczenie_chorobowe, ubezpiczenie_wypadkowe,
                 miejsce_zamieszkania, ppk, stawka_podatku):
        self.imie= ""
        self.nazwisko=""
        self.wynagrodzenie_brutto=""
        self.ubezpieczenie_emerytalne=""
        self.ubezpieczenie_rentowe=""
        self.ubezpieczenie_chorobowe=""
        self.ubezpiczenie_wypadkowe=""
        self.miejsce_zamieszkania=""
        self.ppk=""
        self.stawka_podatku=""


def __str__(self):
    pass
def skladki(self):
    return self.ubezpiecznie_chorobowe * self.wynagrodzenie_brutto + self.ubezpieczenie_rentowe * self.wynagrodzenie_brutto + self.ubezpieczenie_emerytalne * self.wynagrodzenie_brutto

def wplata_ppk(self):
    return self.ppk * self.wynagrodzenie_brutto
def zaliczka_podatku(self):
    return self.wynagrodzenie_brutto - skladki(self) - self.miejsce_zamieszkania + 0.015 * self.wynagrodzenie_brutto
def obllicz_netto(self):
    return 0
def oblicz_koszty(self):
    return 0

pracownicy = [] # z csv
for pracownik in pracownicy:
    print("Pracownik Kowalski:")
    print("- pensja brutto:")
    print("- pensja netto:")
    print("- koszty pracodawcy:")
    print("- koszt całkowity:")

print("Suma kosztów wynosi:")
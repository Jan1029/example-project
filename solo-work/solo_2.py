class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.bok_a = a
        self.b = b
        self.c = c
        self.h_a = h_a
        #self.obwod = a + b + c

    def obwod(self):
        return self.bok_a + self.b + self.c

    def pole(self):
        return (self.bok_a * self.h_a)/2

trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
trojkat_jana = Trojkat(8, 6, 10, 4)
print(trojkat_rownoboczny.obwod())

class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def obwod(self):
        return 2 * self.a + 2 * self.b

    def pole(self):
        return self.a * self.b

prostokat_1 = Prostokat(8, 10)

print(prostokat_1.obwod())
print(prostokat_1.pole())

print("--------------------------------------------------")
class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.numer_indeksu}"

    def __int__(self):
        return 5

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny) / len(self.oceny)

student_jan = Student("Jan", "Gałązka", 120030)
student_jan.dodaj_ocene(4.5)
student_jan.dodaj_ocene(5)

print(student_jan)
print(student_jan.oceny)
print(student_jan.zwroc_srednia())

print("-------------------------------------------")

class Mieszkanie:
    def __init__(self, powierzchnia, wartosc, adres, pietro, wlasciciel, liczbapokoi, wartoscmebli, internet):
        self.powierzchnia = powierzchnia
        self.wartosc = wartosc
        self.adres = adres
        self.pietro = pietro
        self.wlasciciel = wlasciciel
        self.liczbapokoi = liczbapokoi
        self.wartoscmebli = wartoscmebli
        self.internet = internet
    def __str__(self):
        return self.adres
    def ubezpieczenie(self):
        return 0.05 * (self.wartosc + self.wartoscmebli)
    def czynsz(self):
        return 0.5 * (self.wartosc/self.powierzchnia)

mieszkanie_jana = Mieszkanie(50, 480000, "Konwaliowa 5", 3, "Jan Gałązka", 3, 50000, "Netia")
print(mieszkanie_jana)
print(mieszkanie_jana.ubezpieczenie())
print(mieszkanie_jana.czynsz())
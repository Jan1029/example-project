import csv
class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto, uczestniczy_w_ppk, miejscowy):
        self.imie= imie
        self.nazwisko= nazwisko
        self.wynagrodzenie_brutto= wynagrodzenie_brutto
        self.uczestniczy_w_ppk = uczestniczy_w_ppk
        self.miejscowy= miejscowy

    def __str__(self):
        pass

    def oblicz_netto(self):
        skladka_emerytalna = self.wynagrodzenie_brutto * 0.0976
        skladka_rentowa = self.wynagrodzenie_brutto * 0.015
        skladka_chorobowa = self.wynagrodzenie_brutto * 0.0245
        skladka_zdrowotna = (self.wynagrodzenie_brutto - skladka_emerytalna - skladka_rentowa - skladka_chorobowa) * 0.09
        skladka_ppk = self.wynagrodzenie_brutto * 0.015 if self.uczestniczy_w_ppk else 0
        koszt_uzyskania_przychodu = 250 if self.miejscowy else 300
        skladka_pracodawcy_ppk = self.wynagrodzenie_brutto * 0.015 if self.uczestniczy_w_ppk else 0

        podstawa_opodatkowania = self.wynagrodzenie_brutto - skladka_emerytalna - skladka_rentowa - skladka_chorobowa - skladka_zdrowotna + skladka_pracodawcy_ppk - koszt_uzyskania_przychodu

        podatek_dochodowy = self.oblicz_podatek_dochodowy(podstawa_opodatkowania)

        wynagrodzenie_netto = self.wynagrodzenie_brutto - skladka_emerytalna - skladka_rentowa - skladka_chorobowa - skladka_zdrowotna - podatek_dochodowy - skladka_ppk

        return wynagrodzenie_netto

    def oblicz_podatek_dochodowy(self, podstawa_opodatkowania):
        progi_podatkowe = [0, 120000]
        stawki_podatkowe = [0.12, 0.32]
        podatek_dochodowy = 0
        obecne_progi = zip(progi_podatkowe, progi_podatkowe[1:])
        for prog in obecne_progi:
            dolna_granica, gorna_granica = prog
            if podstawa_opodatkowania > dolna_granica:
                if podstawa_opodatkowania > gorna_granica:
                    podatek_dochodowy += (gorna_granica - dolna_granica) * stawki_podatkowe[0]
                else:
                    podatek_dochodowy += (podstawa_opodatkowania - dolna_granica) * stawki_podatkowe[0]
                    break

        return podatek_dochodowy

    def oblicz_koszty(self):
        skladka_emerytalna = self.wynagrodzenie_brutto * 0.0976
        skladka_rentowa = self.wynagrodzenie_brutto * 0.065
        skladka_wypadkowa = self.wynagrodzenie_brutto * 0.0167
        skladka_pracodawcy_ppk = self.wynagrodzenie_brutto * 0.015 if self.uczestniczy_w_ppk else 0

        calkowity_koszt_pracodawcy = self.wynagrodzenie_brutto + skladka_emerytalna + skladka_rentowa + skladka_wypadkowa + skladka_pracodawcy_ppk

        return calkowity_koszt_pracodawcy

pracownicy = []
with open('pracownicy.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        imie = row[0]
        nazwisko = row[1]
        wynagrodzenie_brutto = float(row[2])
        uczestniczy_w_ppk = row[3].lower() == "tak"
        miejscowy = row[4].lower() == "tak"
        pracownik = Pracownik(imie, nazwisko, wynagrodzenie_brutto, uczestniczy_w_ppk, miejscowy)
        pracownicy.append(pracownik)

calkowity_koszt_pracodawcy = 0
for pracownik in pracownicy:
    calkowity_koszt_pracodawcy = pracownik.oblicz_koszty()
    wynagrodzenie_netto = pracownik.oblicz_netto()

    print(f"Pracownik: {pracownik.imie} {pracownik.nazwisko}")
    print(f"Wynagrodzenie brutto: {pracownik.wynagrodzenie_brutto}")
    print(f"Całkowity koszt pracodawcy: {calkowity_koszt_pracodawcy}")
    print(f"Wynagrodzenie netto: {wynagrodzenie_netto}\n")

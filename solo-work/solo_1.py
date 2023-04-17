# zadanie 1.1
hello = "Hello"
student = "Ola"
print("{} {}".format(hello, student))

# zadanie 1.2
student = input("Wpisz swoje imie")
print("Hello", student)

# zadanie 1.3
studenci = ["Ania", "Kuba", "Piotr", "Jan"]
liczba_studentow = len(studenci)
print("Liczba studentow wynosi:", liczba_studentow)

# zadanie 1.4
studenci = ["Ania", "Kasia", "Piotr", "Tomek"]
for i in studenci:
    print("Hello ", i)

#zadanie 1.5
liczba = 3
potega = 4
wynik = liczba ** potega
print("Wynik wynosi:", wynik)

# zadanie 1.6
ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

studenci.sort()
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.8
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci_posortowani = sorted(studenci, key=lambda x: x.split()[-1])
print("Alfabetyczna lista studentow wynosi: ")
for student in studenci_posortowani:
    print(student)

# zadanie 1.9
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0
for student in studenci:
    if student.split()[-1].startswith("N"):
        liczba_n += 1
print("Liczba studentow na N wynosi:", liczba_n)
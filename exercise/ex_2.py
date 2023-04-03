#kwadrat

a=10

obwod = a * 4
pole = a * a

#Obwod kwadratu wynosi 40, a pole 100
print("obwod kwadratu wynosi" + str(obwod) + "a pole" +str(pole) +".")

#prostokat

b=5
obwod_prostokata = 2 * a + 2 * b
pole_prostokata = a * b
#Obwod prostokata wynosi 30, a pole 50
print("Obwod prostokata wynosi" + str(obwod_prostokata)+ "a pole" + str(pole_prostokata) + ".")

#trapez

a = 4
b = 13
c = 9
d = 12
h = 12

obwod_trapez = a + b + c + d
pole_trapez = ((a + c) * h) / 2
print("Obwod trapezu wynosi" + str(obwod_trapez)+ "a pole" + str(pole_trapez) + ".")

#kolo
import math
r = 3
pi_zmienna = math.pi
obwod_kolo = 2 * pi_zmienna
pole_kolo = 2 * pi_zmienna * r**2
print("Obwod kola wynosi" + str(obwod_kolo)+ "a pole" + str(pole_kolo) + ".")

#trojkat

a = 12
b = 10
c = 10
h = 8

obwod_trojkata = a + b + c
pole_trojkata = (a * h) / 2
print("Obwod trojkata wynosi" + str(obwod_trojkata)+ "a pole" + str(pole_trojkata) + ".")
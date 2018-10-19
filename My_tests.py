# a = 10 + 10 + 30
# print (a)
#
# b = 30 + 20 - 10 / 2
# c = a+b
#
# print(c)
#
# x = 9 % 2
# print(x)
#
#
#

# a = 11
# b = 11
# c = 12
#
# if a < b:
#     print("Liczba A jest mnniejsza od B")
# elif a > b:
#     print("Liczba A jest większa od B")
# if a > c:
#     print("Liczba A jest większa od C")
# elif a < c:
#     print("Liczba A jest mniejsza od C")
# elif a == c:
#     print("A i C są sobie równe")
#
# print(a,b,c)



# x = "Napis"
# otherx = x[2]
# print(x)
# print(otherx)
#
#
# print(x.lower())
# print(otherx.upper())
# print(x.upper())
# print(len(otherx))
# print(len(x))
#
# y = "To jest jakiś napis"
# print(y + " " +str(2))


# print("Napis musi być w \"apostrofach\"")
#
#
# a = "DDD123aaa!@#ddd434DDD"
# print(a.replace("DDD", "Dupa", ))
#
# x = "Zmien ten napis Zmien"
# print(x.replace("Zmien", "Nowy napis", 1))


# x = "abcdefghij"
# litery = x[0:9:2]
# print(litery)
# print(len(x))


# ulica = "kwitnącej"
# miasto = "Warszawa"
#
# x = "Witam na ulicy %s w mieście %s" % (ulica, miasto)
# print(x)
#
#
# a = "cześć co tam"
# print(a.split())


# x = ["Czarny", "Niebieski", "Zielony"]
# print(x)
# print(x[0])
# print(x[1])
# print(x[2])
#
# print("#$" * 20)
#
# x[2] = "Pomarańczowy"
# print(x)
# print(x[2])
#
# z = x[1] + " " + x[2]
# print(z)




# cars = ["Honda", "BMW", "Mercedes", "Daewoo"]
# motors = ["Suzuki", "Aprilia", "Daytona"]
#
# print(cars)
# print(motors)
#
# cars[0] = "Tesla"
# print(cars)
#
#
# print("#$" * 30)
#
# cars_and_moto = cars[:], motors[:]
# print(cars_and_moto)
# print(len(cars_and_moto))
# print("#$" * 30)
# print(len(cars) + len(motors))
# print("#$" * 30)
# print("Do wyboru masz następujące samochody : %s" % cars)
# print("Do wyboru masz takie oto motocykle : %s" % motors)




# cars = ["Mercedes", "BMW", "Audi", "Ferrari"]
# print(cars)
#
# cars.append("Tesla")
# print(cars)
#
# cars.pop(3)
# print(cars)
#
# cars.insert(4, "Tesla")
# print(cars)
#
# cars.insert(4, "Porshe")
# print(cars)
#
# cars.pop(3)
# print(cars)
#
# cars.remove("Tesla")
# print(cars)
#
# cars.append("Nowa Tesla")
# print(cars)
#
# cars.sort()
# print(cars)
#
# x = cars.count("BMW")
# print(x)
#
# cars.append("BMW")
# print(cars)
#
# x = cars.count("BMW")
# print(x)



# dictionary = {"ulica" : "Kwitnąca", "numer_bloku" : 9, "numer_mieszkania" : 91}
#
# street = dictionary["ulica"]
# block_number = dictionary["numer_bloku"]
# house_number = dictionary["numer_mieszkania"]
#
# print(street, block_number, house_number)


# motorbike_dict = {"Suzuki" : {"model" : "GSXR" , "year" : 2008} , "Yamaha" : {"model" : "R1", "year" : 2010}}
#
# print(motorbike_dict)
# one_model = motorbike_dict["Suzuki"]
# print(one_model)
#
#
# print(motorbike_dict.keys())
# print(motorbike_dict.values())
# x = motorbike_dict.values()
# print(x)


# d={}
# d["sfo"] = "San Francisco"
# d["nyc"] = "New York City"
# print(d)


# x = 10 >= 10
# z = 15 < 9
#
#
# działanie_1 = x
# działanie_2 = z
# print(x)
# print(z)
#
# print(działanie_1 and działanie_2)



# x = 15 + 30
# c = 56 - 11
# v = 49
#
# if x == c:
#     print("X jest równe C")
# elif x > c:
#     print("X jest większe od C")
# elif x < c:
#     print("X jest mniejsze od C")
# if x == c and x == v:
#     print("Wszystkie zmienne są sobie równe")



# x = 0
#
# while x < 50:
#     x += 1
#     if x < 50:
#         print("Jeszcze za mało")
#     print("This is the number : " + str(x))
# if x == 50:
#     print("Brawo")



# z = []
#
# number = 0
# while number < 13:
#     z.append(number)
#     number = number + 2
# print(z)



# x = 0
#
# while x < 60:
#     x += 5
#     print("Piszę to za każdym razem = " + str(x))
#     if x == 50:
#         print("X jest równy 50")
#     elif x > 50:
#         print("X jest większy od 50")
#         break




# def my_method(x , y):
#     if x > y:
#         print("Cyfra %s jest większa od cyfry %s" % (x, y))
#     elif x < y:
#         print("Cyfra %s jest mniejsza od cyfry %s" % (x, y))
#     elif x == y:
#         print("Cyfra %s i %s są sobie równe!" % (x, y))
#
# my_method(15, 20)




# test = 0
#
# while test < 20:
#     test += 2
#     print("Liczba : " + str(test))
# print("Na zakończenie")



# def moja_metoda(x):
#     while 0 < x:
#         x -= 5
#         print("To jest liczba :" + str(x))
#         if x == 50:
#             print("Połowa drogi :" + str(x))
#     if x > 100:
#         print("Cyfra jest większa od 100")
#     elif x <= 0:
#         print("Cyfra jest równa zero bądź mniejsza od zera")
#
# moja_metoda(100)



# def oceny():
#
#     przedmioty = ["Polski", "Angielski", "Matematyka", "W-F"]
#     ilosc_przedmiotów = 4
#
#     oceny_z_przedmiotow = [3, 5, 5, 6]
#     suma_ocen = sum(oceny_z_przedmiotow)
#
#     #Wyliczenie średniej z ocen
#     średnia = suma_ocen / ilosc_przedmiotów
#
#
#     if średnia < 4.0:
#         print("Średnia jest zbyt niska i wynosi: " + str(średnia) + " - Nie zdajesz")
#     elif średnia >= 4.0:
#         print("Średnia jest dobra i wynosi: " + str(średnia) + " - Zdajesz!")
#
# oceny()




def kalkulator_egzaminow(przedmiot, punkty):

    l = ["Polski", "Angielski", "Matematyka", "Geografia", "Fizyka"]

    # 300 pktów = 100 procent
    wynik_procentowy = (punkty * 100) / 300


    if przedmiot in l:
        print("Przedmiot znajduję się na liście i otrzymałeś z niego : " + str(int(wynik_procentowy)) + " procent")
    elif przedmiot not in l:
        print("Przedmiot nie znajduje się na liście")
        return None



    if przedmiot in l and wynik_procentowy < 50:
        print("Twój wynik to : " + str(int(wynik_procentowy)) + " procent." +" Nie zdałeś egzaminu")
    elif przedmiot in l and wynik_procentowy == 50:
        print("Jesteś na granicy, twój wynik to : " + str(int(wynik_procentowy)) + " procent."+ " Zdałeś!")
    elif przedmiot in l and wynik_procentowy > 50:
        print("Twój wynik to : " + str(int(wynik_procentowy)) + " procent. " + "Brawo, zdałeś!")

kalkulator_egzaminow("Fizyka", 299)






































































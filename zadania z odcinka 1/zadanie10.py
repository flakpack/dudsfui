# 10. Stworz gre, w ktorej wylosujesz liczbe z przedzialu
# 1- 100, zapiszesz te liczbe do zmiennej, a nastepnie poprosisz uzytkownika
# o odgadniecie tej liczby. Po kazdej probie wyswietlaj, czy mniejsza czy wieksza
# gdy odgadnie zakoncz gre
# znajdz informacje w jaki sposob losowac liczby
#calkowite w pythonie

import random
proby = 0
liczba = random.randint(1, 100)

while True:
    proby += 1
    proba = int(input("Spróbuj zgadnąć o jakiej liczbie myśle 1-100: "))

    if 100 < proba or proba < 1:
        print("podałeś liczbe poza zakresem 1-100")
    elif proba < liczba:
        print("liczba jest większa")
    elif proba > liczba:
        print("liczba jest mniejsza")
    else:
        print(f"Brawo zgadłeś w {proby} próbach!")
        break

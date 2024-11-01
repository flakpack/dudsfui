# 9. Pobierz od uzytkownika 3 liczby calkowite i uporzadkuj je
# w kolejnosci od najmniejszej do najwiekszej
while True:

    Pierwsza = int(input("Podaj liczbę: "))
    Druga = int(input("Podaj liczbę: "))
    Trzecia = int(input("Podaj liczbę: "))

    if Pierwsza <= Druga <= Trzecia:
        print(f"{Pierwsza} {Druga} {Trzecia}")
    elif Pierwsza <= Trzecia <= Druga:
        print(f"{Pierwsza} {Trzecia} {Druga}")
    elif Druga <= Pierwsza <= Trzecia:
        print(f"{Druga} {Pierwsza} {Trzecia}")
    elif Druga <= Trzecia <= Pierwsza:
        print(f"{Druga} {Trzecia} {Pierwsza}")
    elif Trzecia <= Pierwsza <= Druga:
        print(f"{Trzecia} {Pierwsza} {Druga}")
    elif Trzecia <= Druga <= Pierwsza:
        print(f"{Trzecia} {Druga} {Pierwsza}")



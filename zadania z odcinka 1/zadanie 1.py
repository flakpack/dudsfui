# 1. Napisz program, który sprawdza, czy podana przez użytkownika liczba jest parzysta,
# czy nie parzysta.
while True:
    print("Sprawdzę, czy liczba jest parzysta")
    liczba = (input("Podaj liczbę całkowitą:  lub wpisz stop "))

    if liczba == 'stop':
        print("program zatrzymany")
        break

    try:

        if int(liczba) % 2 == 0:
            print("""Podana przez Ciebie liczba jest parzysta
            """)
        else:
            print("""Podana przez Ciebie liczba jest nieparzysta
            """)

    except ValueError:
        print("To nie jest liczba całkowita!")

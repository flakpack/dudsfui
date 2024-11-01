# 2. Napisz program, który sprawdza, czy podana przez użtywkonika
# liczba jest większa od 0, mniejsza od 0, równa 0
while True:
    liczba = input("Podaj liczbę lub wpisz stop ")

    if liczba == 'stop':
        print("program zatrzymany")
        break

    elif int(liczba) == 0:
        print("Podana przez Ciebie liczba jest równa 0")
    elif int(liczba) < 0:
        print("Podana przez Ciebie liczba jest mniejsza od 0")
    elif int(liczba) > 0:
        print("Podana przez Ciebie liczba jest większa od 0")
#asugsdf
#$$
#@
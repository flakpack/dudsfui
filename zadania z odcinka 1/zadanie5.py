def czy_pierwsza(liczba):
    if liczba < 2:
        return False  # Liczby mniejsze niż 2 nie są pierwsze
    for i in range(2, liczba):  # Sprawdzamy dzielniki od 2 do liczby-1
        if liczba % i == 0:
            return False  # Jeśli znajdziemy dzielnik, to liczba nie jest pierwsza
    return True

# Pętla wypisująca liczby pierwsze od 0 do 100
print("Liczby pierwsze od 0 do 100:")
for liczba in range(101):
    if czy_pierwsza(liczba):
        print(liczba)
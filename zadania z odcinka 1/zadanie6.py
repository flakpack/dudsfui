# 6. Napisz program, który wyświetli sumę wszystkich liczb parzystych
# z przedziału 1 - 100
suma = 0

for liczba in range(2, 101):
    if liczba % 2 == 0:
        suma += liczba

print("suma wszystkich liczb parzystych 1-100 jest równa: " + str(suma))

# 8. stworz program ktory prosi uzytkownika o wpisanie teksu
# a nastepnie utworz slownik w ktorym kluczami beda slowa
# wystepujace w tym tekscie a wartosciami liczby wystapien kazdego slowa
# wyswietl zawartosc slownika

text = input("wpisz zdanie: ")

slowa = text.split()

slownik = {}

for slowo in slowa:
    if slowo in slownik:
        slownik[slowo] += 1
    else:
        slownik[slowo] = 1
print(slownik)
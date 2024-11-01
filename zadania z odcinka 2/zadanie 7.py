# 7. posortuj slownik poprzedniego cwiczenia w kolejnosci alfabetycznej

slownik = {
    'Polska' : 'Warszawa',
    'Niemcy' : 'Berlin',
    'Czechy' : 'Praga',
    'Słowacja' : 'Bratysława',
    'Ukraina' : 'Kijów',
    'Białoruś' : 'Mińsk',
    'Litwa' : 'Wilno',
    'Rosja' : 'Moskwa'
}
for kraj in sorted(slownik):
    print(f"{kraj} - {slownik[kraj]}")
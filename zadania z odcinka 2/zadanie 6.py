# stworz slownik, ktory bedzie przechowywal informacje o krajach i ich stolicach
# dodaj do niego 5 elementow. wyswietl dane ze slownika w formacie: kraj - stolica

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
for kraj, stolica in slownik.items():
    print(kraj + ' - ' + stolica)
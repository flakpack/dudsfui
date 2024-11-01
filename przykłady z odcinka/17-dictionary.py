phone_book = {
    'Michał': 100200300,
    'Kamil' : 999888777,
    'Buda' : 111222333,
    'Kamil' : 333333333
}
# print(phone_book.get('Buda'))
# print(phone_book['Michał'])

# phone_book['Paulina'] = 200200100
# phone_book['Kamil'] = 777777777
# phone_book.pop('Michał')
# print(phone_book)

# for element in phone_book.values():
# for element in phone_book.items():
#     print(element)

for name, phone_number in phone_book.items():
    print(name + ':' +str(phone_number))
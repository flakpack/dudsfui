# def hello(name, age):
#     print("Hej " + name + "! " + "Masz " + str(age) + " lat")
#
#
# # hello('Michał',34)
# # hello('Adam', 23)
#
# hello(age=45, name='Michał')

# def strip_and_uppercase(text):
#     return str(text).strip().upper()
#
# text = '   tekst do Zmiany  '
# text = strip_and_uppercase(text)
# print(text)

countries_information = {}
countries_information ['Polska'] = ('Warszawa', 38)
countries_information ['Niemcy'] = ('Berlin', 80)
countries_information ['Francja'] = ('Paryż', 57)

country = 'Niemcy'
print('Kraj: '+country)
print('Stolica: ' + countries_information[country][0])
print('Liczba mieszkancow w mln: ' + str(countries_information[country][1]))

def print_country_information(country):
    print('Kraj: ' + country)
    print('Stolica: ' + countries_information[country][0])
    print('Liczba mieszkancow w mln: ' + str(countries_information[country][1]))

print_country_information('Niemcy')
print()
print_country_information('Francja')
print()
print_country_information('Polska')


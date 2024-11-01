isskyblue = True
isPythonDifficult = False

# print(isPythonDifficult or isskyblue)
# print(isPythonDifficult and isskyblue)

a = 5
b = 2

# print(a>b and b>0)
# print(a>b and b>3)
# print(a>10 or a==5 or (b>0 and a<b) and a==5)

c = 5
print(c % 2 == 0)
#zwraca true jesli liczba parzysta
# false dla nieparzystej

print(not c % 2 == 0)
#zwraca true jesli liczba nieparzystej
# false dla parzystej

user_logged_in = True

if user_logged_in:
    print("Użytkownik zalogowany")
if not user_logged_in:
    print("Użytkownik niezalogowany")
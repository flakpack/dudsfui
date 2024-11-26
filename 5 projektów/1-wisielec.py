import string, sys

alfabet = set(string.ascii_letters)

while True:
    try:
        n_of_tries = int(input("Wybierz ilość prób: "))
        if n_of_tries >= 1:
            break
        else:
            print("Liczba całkowita musi być większa od 0")
    except ValueError:
        print("Podaj liczbę całkowitą")


word = "kajak"
used_letters = []

user_word = []

def find_indexes(word, letter):
    indexes =[]

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

def game_status():
    print("".join(user_word))
    print("Masz jeszcze", n_of_tries, "prób")
    print("Użyte litery:","".join(used_letters))
    print()
###

for _ in word:
    user_word.append("_")

while True:
    letter = input("Podaj literę: ")
    if letter in alfabet:
        used_letters.append(letter)
        used_letters.append(" ")
        found_indexes = find_indexes(word, letter)

        if len(found_indexes) == 0:
            print("Nie ma takiej litery")
            n_of_tries -= 1
            if n_of_tries == 0:
                print()
                print("Koniec gry :(")
                sys.exit(0)
        else:
            for index in found_indexes:
                user_word[index] = letter
            # print(user_word) ['w'] brzydko wyglada

            if "".join(user_word) == word:
                print(word)
                print("Zgadłeś :)")
                graj_dalej = input("Chcesz zgarać jeszcze raz? (tak/nie)")

    else:
        print(letter, "to nie litera!")

    game_status()


#zakazac powtarzania liter
#weryfikowac input uzytkownika zrobione
#lista slow do odgadywania i tak by sie nie powtarzaly
#czy chcesz dalej grac
#sprobuj ponownie

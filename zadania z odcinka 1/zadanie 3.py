# 3. Napisz program, który zapyta użytkownika o wynik na egzaminie
# (od 0 do 100) i wyświetli odpowiednią ocenę:
# 0-35 -> 1
# 36-50 -> 2
# 51-74 -> 3
# 75-90 -> 4
# 91-99 -> 5
# 100 -> 6

while True:
    procent = input("ile procent otrzymałeś z egzaminu? stop aby zatrzymac")

    if procent == 'stop':
        print("program zatrzymany")
        break


    try:
        procent = int(procent)

        if procent < 0:
            print("Nieprawidłowa wartość")
        elif procent > 100:
            print("Nieprawidlowa wartość")
        elif 0 <= procent <= 35:
            print("otrzymałeś jedynkę")
        elif 36 <= procent <= 50:
            print("otrzymałeś dwójkę")
        elif 51 <= procent <= 74:
            print("otrzymałeś trójkę")
        elif 75 <= procent <= 90:
            print("otrzymałeś czwórkę")
        elif 91 <= procent <= 99:
            print("otrzymałeś piątkę")
        elif procent == 100:
            print("otrzymałeś szóstkę :)")

    except ValueError:
        print("Wpisz liczbe lub stop")
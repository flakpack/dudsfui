# 7. Napisz program, który policzy pole prostokąta
# użytkownik podaje dlugosci bokow
while True:
    print("Policze Ci pole prostokąta")
    
    Pierwszy_bok = input("Podaj długość pierwszego boku: ")
    if int(Pierwszy_bok) <= 0:
        print("błędna wartość")
        break
    Drugi_bok = input("Podaj długość drugiego boku przyległego do pierwszego: ")
    if int(Drugi_bok) <= 0:
        print("błędna wartość")
        break
    Pole_prostokąta = int(Pierwszy_bok) * int(Drugi_bok)
    print(f"Pole wynosi:  {Pole_prostokąta}")
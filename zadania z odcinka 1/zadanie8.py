# 8. Napisz program, który sprawdzi czy podane imie jest imieniem męskim, czy zenskim
while True:
    Imie = input ("Podaj imię: ")

    if len(Imie) < 3:
        print("Takie imię nie istnieje")
        break

    if Imie.endswith("a"):
        print(f"{Imie} jest imieniem żeńskim")
    else:
        print(f"{Imie} jest imieniem męskim")

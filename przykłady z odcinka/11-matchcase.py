light = input("Jakie widzisz światło? (zielone, zolte, czerwone)")

match light:
    case 'zielone':
        print("jedz")
    case 'zolte':
        print("przygotuj sie")
    case 'czerwone':
        print("stoj")
    case _:
        print("nie znam takiego koloru")
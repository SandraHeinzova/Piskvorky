line0 = ["0","1","2","3"]
line1 = ["1"," "," "," "]
line2 = ["2"," "," "," "]
line3 = ["3"," "," "," "]
all_sets = [line0, line1, line2, line3]

def hrac1():
    print(f"Hraje {player1}:")
    while True:
        num1 = input("Zadej hodnotu x (řada): ")
        try:
            num1 = int(num1)
        except ValueError:
            print ("Špatná volba, musíš zadat číslo 1-3.")
        else:
            break
            
    while True:
        num2 = input("Zadej hodnotu y (sloupec): ")
        try:
            num2 = int(num2)
        except ValueError:
            print ("Špatná volba, musíš zadat číslo 1-3.")
        else:
            break            

    if all_sets[num1][num2] != " ":
        print("Špatná volba, zvol znovu")
        hrac1()
    else:
        all_sets[num1][num2] = "X"


def hrac2():
    print(f"Hraje {player2}:")
    while True:
        num3 = input("Zadej hodnotu x (řada): ")
        try:
            num3 = int(num3)
        except ValueError:
            print ("Špatná volba, musíš zadat číslo 1-3.")
        else:
            break
            
    while True:
        num4 = input("Zadej hodnotu y (sloupec): ")
        try:
            num4 = int(num4)
        except ValueError:
            print ("Špatná volba, musíš zadat číslo 1-3.")
        else:
            break

    if all_sets[num3][num4] != " ":
        print("Špatná volba, zvol znovu")
        hrac2()
    else:
        all_sets[num3][num4] = "O"


print("Vítejte ve hře Piškvorky junior.")
player1 = input("Jak se jmenuje první hráč?\n")
player2 = input("A jak se jmenuje protivník?\n")
print("Těší mě! Pojďme hrát!")
print("-" * 50)

while True:
    hrac1()

    print(f"{line0}\n{line1}\n{line2}\n{line3}")

    if all_sets[1][1] == "X" and all_sets[1][2] == "X" and all_sets[1][3] == "X":
        print(f"Vyhrál hráč {player1}")
        break
    elif all_sets[2][1] == "X" and all_sets[2][2] == "X" and all_sets[2][3] == "X":
        print(f"Vyhrál hráč {player1}")
        break
    elif all_sets[3][1] == "X" and all_sets[3][2] == "X" and all_sets[3][3] == "X":
        print(f"Vyhrál hráč {player1}")
        break
    elif all_sets[1][1] == "X" and all_sets[2][2] == "X" and all_sets[3][3] == "X":
        print(f"Vyhrál hráč {player1}")
        break
    elif all_sets[3][1] == "X" and all_sets[2][2] == "X" and all_sets[1][3] == "X":
        print(f"Vyhrál hráč {player1}")
        break
    elif all_sets[1][3] == "X" and all_sets[2][3] == "X" and all_sets[3][3] == "X":
        print(f"Vyhrál hráč {player1}")
        break

    hrac2()
    
    print(f"{line0}\n{line1}\n{line2}\n{line3}")


    if all_sets[1][1] == "O" and all_sets[1][2] == "O" and all_sets[1][3] == "O":
        print(f"Vyhrál hráč {player2}")
        break
    elif all_sets[2][1] == "O" and all_sets[2][2] == "O" and all_sets[2][3] == "O":
        print(f"Vyhrál hráč {player2}")
        break
    elif all_sets[3][1] == "O" and all_sets[3][2] == "O" and all_sets[3][3] == "O":
        print(f"Vyhrál hráč {player2}")
        break
    elif all_sets[1][1] == "O" and all_sets[2][2] == "O" and all_sets[3][3] == "O":
        print(f"Vyhrál hráč {player2}")
        break
    elif all_sets[3][1] == "O" and all_sets[2][2] == "O" and all_sets[1][3] == "O":
        print(f"Vyhrál hráč {player2}")
        break
    elif all_sets[1][3] == "O" and all_sets[2][3] == "O" and all_sets[3][3] == "O":
        print(f"Vyhrál hráč {player2}")
        break


print("Díky za hru!")
NBRMAGIK = 20
def demanderNbreMagique() :
    VIEDECHANCE = 3
    nbr = input("Dévinez le nombre magique :")
    while(int(nbr) != NBRMAGIK):
        VIEDECHANCE -= 1
        print(f"Il vous reste {VIEDECHANCE} vie(s)")
        if(VIEDECHANCE > 0):
            if(int(nbr) > NBRMAGIK):
                nbr = input(f"Oups... Moins grand que {nbr}. Essayez encore :")
            if(int(nbr) < NBRMAGIK):
                nbr = input(f"Oups... Plus grand que {nbr}. Essayez encore :")
            if(int(nbr) == NBRMAGIK):
                print('Félicitations :) !!!')
                break
        if(VIEDECHANCE == 0):
            print("Oups (~) vous avez plus de vie")
            break

demanderNbreMagique()
# 1 pouce = 2.54cm
VAL_CENT_FROM_PC = 2.54

# 1 cm = 0.394cm
VAL_PC_FROM_CENT = 0.394

#Convertion de pouce en centimètre
def conversionPouceInCentim(pc_nbr):
    result = float(pc_nbr) * VAL_CENT_FROM_PC
    print("")
    print("****************** RESULTAT *****************************")
    print(f"{pc_nbr} pouce = {result} centimètre")
    print("*********************************************************")
    print("")
    return result

#Convertion de centimètre en pouce
def conversionCentimInPouce(cm_nbr):
    result = float(cm_nbr) * VAL_PC_FROM_CENT
    print("")
    print("********************** RESULTAT *************************")
    print(f"Résultat: {cm_nbr} centimètre = {result} pouce")
    print("*********************************************************")
    print("")
    return result

#Vérifier si la valeur à convertir un nombre
def valVerif(val):
    is_int = False
    try:
        float(val)
        is_int =True
    except:
        print("")
        print("************* ERREUR **************")
        print("Vous devez saisir un nombre")
        print("***********************************")
        print("")
        is_int = False

    return is_int

#Processus de convertion
def convertion():
    print("")
    print("*********** MENU ****************")
    print("A- Convertir de centimètre en pouce")
    print("B- Convertir de pouce en centimètre")
    print("*********************************")
    print("")
    choise = input("Quelle opération souhaitez vous faire? ")
    while(not(choise == 'A' or choise == 'a' or choise == 'B' or choise == 'b')):
        print("")
        print("***************************** ERREUR *****************************************")
        print("Vous devez choisir la lettre (Majuscule ou Miniscule) de l'opération souhaité")
        print(">> Ou appuyez 'C' pour sortir")
        print("*****************************************************************************")
        print("")
        choise = input("Quelle opération souhaitez vous faire? ")
        if(choise == 'C' or choise == 'c'):
            print("")
            print("********** AUREVOIR *********")
            print("Merci d'avoir participé")
            print("*****************************")
            print("")
            break 

    if(choise == 'A' or choise == "a"):
        print("")
        print(">>>>>>>>>>>> OPERATION <<<<<<<<<<<<<<<")
        print("Convertir de centimètre en pouce")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("")
        choise = 'A'
        while(not(choise =='C' or choise =='c')):
            pcnbr = input("Nombre centimètre à convertir en pouce: ")
            isValid = valVerif(pcnbr)
            while(isValid == False):
                pcnbr = input("Nombre à convertir en pouce: ")
                isValid = valVerif(pcnbr)

            conversionPouceInCentim(pcnbr)
            choise = input("Appuyer une touche pour continuer ou C pour quitter ")

    if(choise == 'B' or choise == "b"):
        print("")
        print(">>>>>>>>>>>> OPERATION <<<<<<<<<<<<<<<")
        print("Convertir de pouce en centimètre")
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("")
        choise = 'B'
        while(not(choise =='C' or choise =='c')):
            cmnbr = input("Nombre de pouce à convertir en centimètre: ")
            isValid = valVerif(cmnbr)
            while(isValid == False):
                cmnbr = input("Nombre à convertir en centimètre: ")
                isValid = valVerif(cmnbr)

            conversionCentimInPouce(cmnbr)
            choise = input("Appuyer une touche pour continuer ou C pour quitter ")

convertion()

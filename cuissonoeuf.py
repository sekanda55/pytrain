import time

data_question = ( 
    {'cuisson': 'à la coque', 'minute': 3},
    {'cuisson': 'mollets', 'minute': 6},
    {'cuisson': 'durs', 'minute': 9}
)

def valVerif(val, max):
    is_int = False
    if not type(val) is int:
        is_int = False
        print("")
        print("************* ERREUR **************")
        print("Vous devez saisir un nombre correspondant à l'option")
        print("***********************************")
        print("")
    else:
        if(int(val)>=1 and int(val)<=int(max)):
            is_int =True
        else:
            is_int = False
            print("")
            print("************* ERREUR **************")
            print(f"Veuillez saisir un nombre entre 1 et {max}")
            print("***********************************")
            print("")   
    return is_int

print("")
print("************** CUISINER UN OEUF ********************")
print(">>>>>>>>> Choisir une option <<<<<<<<<<<<<<<")

ind = 0
for i in data_question:
    ind += 1  
    print(f"{ind}- Oeufs {i['cuisson']} : {i['minute']} minutes")


print("****************************************************")
print("")

nbr = input("Option: ")
verif = valVerif(nbr, ind)
"""while(verif == True):
    try:
        print (data_question[nbr]['minute'])
    except:
        nbr = input("Option: ")
"""
print(verif)
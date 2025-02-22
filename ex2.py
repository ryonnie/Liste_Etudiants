list_e=[]
while True:
    print("***Gerer une Liste Etudiants***")
    i=1
    while(i<=6):
        print(i,"-Ajouter un Etudiant")
        i+=1
        print(i,"-Modifier les informations de etudiant")
        i+=1
        print(i,"-Supprimer un Etudiant")
        i+=1
        print(i,"-Affichier la liste de etudiant")
        i+=1
        print(i,"-Rechercher un Etudiant")
        i+=1
        print(i,"-Quitter le Programme")
        break

    choix=input("saisir Votre Choix :")

    if (choix=="1"):
        Nom =input("saisir Le nom de Etudiant :")
        age=int(input("saisir Age de Etudiant :"))
        matiere_preferer=input("saisir Le Matiere preferer de Etudiant :")
        e={
            'Nom':Nom,
            'Age':age,
            'matiere':matiere_preferer
        }
        list_e.append(e)
        print("=>Ajoutez succeess!\n")

    elif (choix=="2"):
        n=input("saisir Le Nom de Etudiant pour Modifier :")
        nouv_age=int(input("saisir la Nouvelle age de Etudiant :"))
        nouv_matiere = input("saisir La Nouvelle matiere prefere :")
        for e in list_e:
            if e["Nom"]==n :
                e["Age"]=nouv_age
                e["matiere"]=nouv_matiere
            else:
                print("nom invalide!\n")


        print("=>Modification succees!\n")

    elif (choix=="3"):
        n=input("saisir Le Nom de Etudiant pour Supprimer :")

        for e in list_e:
            if e["Nom"]==n:
                list_e.remove(e)
                print("=>Supprition effectuer!\n")
                break
            else:
                print("nom invalide!\n")
        
    elif (choix=="4"):
        if list_e:
            for e in list_e:
                print(f"Nom: {e['Nom']}, Age: {e['Age']}, Matiere Preferer: {e['matiere']}")
        else:
            print("La liste est vide.")
        print("\n")


    
    elif (choix=="5"):
        n=input("saisir Le Nom de Etudiant pour Rechercher :")

        for e in list_e:
            if e["Nom"]==n:
                print(f"Age :{e["Age"]},Matiere preferer :{e["matiere"]}\n")
            else:
                print("Nom Invalide !\n")
                break
        

    elif (choix=="6"):
        print("=>Programme Terminer!\n")
        break

    else:
        print("Invalide Choix!!\n")
        continue









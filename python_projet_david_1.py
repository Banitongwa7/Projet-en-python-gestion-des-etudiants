# importation des packages

import copy
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *



# 1) création de liste_candidats(min: 20 candidats)

def creation_liste_candidats(compteur):
    f=open("candidats.txt","w")
    i = 0
    while i < compteur:
        print("Etudiant numero {}\n".format(i+1))
        num_cin=input("- numéro CIN: ")
        nom=input("- Nom: ")
        prenom=input("- Prénom: ")
        filière_candidat= input("- La filière (MP ou PC): ").upper()
        while filière_candidat != "MP" and filière_candidat != "PC":  # condition while pour obliger l'utilisateur à saisir soit MP ou PC 
            filière_candidat= input("saisir le nom de la filière (MP ou PC): ").upper()
        ligne= "- Numero cin : "+num_cin+" "+"- Nom : "+nom+" "+"- Prenom : "+prenom+" "+"- Filiere : "+filière_candidat+"\n"
        f.write(ligne)
        i = i+1
    f.close()

# option 1 tkinter

def choix1():
    nombre = int(input("veuillez saisir le nombre des candidats à enregistrer : "))
    creation_liste_candidats(nombre)





# 2) création notes des candidants

def creation_note():
    g=open("notes.txt","w")
    ajout = 'O'
    cours = ["Analyse", "Algèbre","Physique" ,"Chimie" ,"Informatique" ,"STA" ,"Français" ,"Anglais"]
    while ajout == 'O':
        f=open("candidats.txt","r")
        note = []
        num_cin = input("veuilez saisir le num_cin du candidat : ")
        recherche = False
        while recherche == False:
            a = f.readline()
            test = a.split(" ")
            for i in range(len(test)):
                if num_cin == test[i]:
                    recherche = True
            if a == "":
                break
        f.close()
        if recherche == True:
            print("\nLe candidat est enregistré dans la base des données de l'université\n")
            print("----------------------------------------------------------------------\n")
            print("veuillez remplir les notes du candidats numero cin {} : ".format(num_cin))
            print("Merci de saisir les notes du candidat : \n")
            for i in range(len(cours)):
                note.append(input("- {} : ".format(cours[i])))
            chaine = ",".join(note) + "\n"
            del note
            g.write(num_cin + "  ")
            g.write(chaine) 
        else:
            print("Desole le numero CIN saisie n'est pas enregistré dans la base des données de l'université. merci")
        ajout = input("voulez vous ajouter les notes d'un autre candidat ? (O/N) : ").upper()
        while ajout != "O" and ajout != "N":
            ajout = input("voulez vous ajouter les notes d'un autre candidat ? (O/N) : ").upper()
    g.close()


# option 2 tkinter 

def choix2():
    creation_note()




# 3 cretion filiere qui permet de creer dictionnaire filiere

def creation_filiere():
    filiere = {}
    limit = 3
    i = 0
    while i<limit:
        print("Enregistrement filiere numero {}\n".format(i+1))
        codefil = int(input("veuillez saisir le code de la filiere : "))
        codeingen = int(input("Veuillez saisir le code de l'ecole d'ingenieur : "))
        capacite = int(input("veuillez saisir la capacite de la filiere {} : ".format(codefil)))
        print("\n")
        filiere[codefil] = [codeingen,capacite]
        i = i+1
    return filiere


# option 3 tkinter
filiere = {}
def choix3():
    global filiere
    print("*********************************************************")
    print("*   L'universite dispose au maximum de 3 code filiere   *")
    print("*********************************************************")
    print("\n")
    filiere = creation_filiere().copy()





# 4 : creation rang pour calculer la FG de chaque etudiant rang.txt



def taille_candidat():
    f=open("notes.txt","r")
    recev = f.read()
    limit = recev.split("\n")
    f.close()
    return len(limit)




def creation_rang():
    h = open("rang.txt","w")
    f=open("notes.txt","r")
    compteur = taille_candidat()
    cin_score = {}
    i = 0
    while i < compteur:
        a = f.readline()
        if a == "":
            break
        a = a.replace("\n","")
        table = a.split("  ")
        note = table[1].split(",")
        scorefg = (int(note[0]))*8 + (int(note[1]))*6 + (int(note[2]))*8 + (int(note[3]))*6 + (int(note[4]))*6 + (int(note[5]))*4 + (int(note[6]))*3 +(int(note[7]))*3
        cin_score[table[0]] = scorefg
        i += 1
    j = '0'
    for k, v in sorted(cin_score.items(),key=lambda x: x[1],reverse = True):
        j = int(j) + 1
        ligne = "- Numero CIN : {} - Score FG : {} - Rang : {}\n".format(k,str(v),str(j))
        h.write(ligne)

    f.close()
    h.close()


# option 4 tkinter

def choix4():
    creation_rang()






# 5 : creation choix dictionnaire

def creation_choix(code):
    f = open("rang.txt","r")
    choix = {}
    while True:
        a = f.readline()
        if a == "":
            break
        table = a.split(" ")
        num_cin = int(table[4])
        choix[num_cin] = code
    f.close()


    return choix



# option 5 tkinter


choix_candidat = {}
def choix5():
    global choix_candidat
    code_filiere = []
    capacite_filiere = []
    for k,v in filiere.items():
        code_filiere.append(k)
        capacite_filiere.append(v[1])
    choix_code_filiere = creation_choix(code_filiere).copy()

    for k in choix_code_filiere.keys():
        print("Candidat Numero CIN {}\nVeuillez faire votre choix parmis les codes filieres sauivants :\n".format(k))
        print("1) code filiere(Place disponible {}) : {}\n2) code filire(Place disponible {}) : {}\n3) code filiere(Place disponible {}) : {}\n".format(capacite_filiere[0],choix_code_filiere[k][0],capacite_filiere[1],choix_code_filiere[k][1],capacite_filiere[2],choix_code_filiere[k][2]))

        if (capacite_filiere[0] == 0 and capacite_filiere[1] == 0 and capacite_filiere[2] == 0):
            choix_candidat[k]="Non admis a la filiere"
            continue
        else:
            choix_candidat[k] = int(input("Choix : "))
            if choix_candidat[k] == choix_code_filiere[k][0]:
                if capacite_filiere[0] >= 1:
                    capacite_filiere[0] = capacite_filiere[0] - 1
                else:
                    print("Le nombre maximale des candidats est atteint.\nMerci de choisir un autre code filiere.\n")
                    choix_candidat[k] = int(input("Choix : "))
                    if choix_candidat[k] == choix_code_filiere[k][1]:
                        if capacite_filiere[1] >= 1:
                            capacite_filiere[1] = capacite_filiere[1] - 1
                        else:
                            print("Le nombre maximale des candidats est atteint.\nMerci d'essayer la derniere filiere.\n")
                            choix_candidat[k] = int(input("Choix : "))
                            if choix_candidat[k] == choix_code_filiere[k][2]:
                                if capacite_filiere[2] >= 1:
                                    capacite_filiere[2] = capacite_filiere[2] - 1
                                else:
                                    print("Le nombre maximale des candidats est atteint.")

                    else:
                        if choix_candidat[k] == choix_code_filiere[k][2]:
                            if capacite_filiere[2] >= 1:
                                capacite_filiere[2] = capacite_filiere[2] - 1
                            else:
                                print("Le nombre maximale des candidats est atteint.\nMerci d'essayer la deuxieme filiere.\n")
                                choix_candidat[k] = int(input("Choix : "))
                                if choix_candidat[k] == choix_code_filiere[k][1]:
                                    if capacite_filiere[1] >= 1:
                                        capacite_filiere[1] = capacite_filiere[1] - 1
                                    else:
                                        print("Le nombre maximale des candidats est atteint.")
                                        

            elif choix_candidat[k] == choix_code_filiere[k][1]:
                if capacite_filiere[1] >= 1:
                    capacite_filiere[1] = capacite_filiere[1] - 1
                else:
                    print("Le nombre maximale des candidats est atteint.\nMerci de choisir un autre code filiere.\n")
                    choix_candidat[k] = int(input("Choix : "))
                    if choix_candidat[k] == choix_code_filiere[k][0]:
                        if capacite_filiere[0] >= 1:
                            capacite_filiere[0] = capacite_filiere[0] - 1
                        else:
                            print("Le nombre maximale des candidats est atteint.\nMerci d'essayer la derniere filiere.\n")
                            choix_candidat[k] = int(input("Choix : "))
                            if choix_candidat[k] == choix_code_filiere[k][2]:
                                if capacite_filiere[2] >= 1:
                                    capacite_filiere[2] = capacite_filiere[2] - 1
                                else:
                                    print("Le nombre maximale des candidats est atteint.")
                            
                    else:
                        if choix_candidat[k] == choix_code_filiere[k][2]:
                            if capacite_filiere[2] >= 1:
                                capacite_filiere[2] = capacite_filiere[2] - 1
                            else:
                                print("Le nombre maximale des candidats est atteint.Merci d'essayer la premiere filiere.")
                                choix_candidat[k] = int(input("Choix : "))  
                                if choix_candidat[k] == choix_code_filiere[k][0]:
                                    if capacite_filiere[0] >= 1:
                                        capacite_filiere[0] = capacite_filiere[0] - 1   
                                    else:
                                        print("Le nombre maximale des candidats est atteint.")
                                          
            else: 
                if choix_candidat[k] == choix_code_filiere[k][2]:
                    if capacite_filiere[2] >= 1:
                        capacite_filiere[2] = capacite_filiere[2] - 1
                    else:
                        print("Le nombre maximale des candidats est atteint.\nMerci de choisir un autre code filiere.\n")
                        choix_candidat[k] = int(input("Choix : "))
                        if choix_candidat[k] == choix_code_filiere[k][0]:
                            if capacite_filiere[0] >= 1:
                                capacite_filiere[0] = capacite_filiere[0] - 1
                            else:
                                print("Le nombre maximale des candidats est atteint.\nMerci d'essayer la deuxieme filiere\n")
                                choix_candidat[k] = int(input("Choix : "))
                                if choix_candidat[k] == choix_code_filiere[k][1]:
                                    if capacite_filiere[1] >= 1:
                                        capacite_filiere[1] = capacite_filiere[1] - 1
                                    else:
                                        print("Le nombre maximale des candidats est atteint.")
                                    
                        else:
                            if choix_candidat[k] == choix_code_filiere[k][1]:
                                if capacite_filiere[1] >= 1:
                                    capacite_filiere[1] = capacite_filiere[1] - 1
                                else:
                                    print("Le nombre maximale des candidats est atteint.\nMerci d'essayer la premiere filiere \n")
                                    choix_candidat[k] = int(input("Choix : "))
                                    if choix_candidat[k] == choix_code_filiere[k][0]:
                                        if capacite_filiere[0] >= 1:
                                            capacite_filiere[0] = capacite_filiere[0] - 1
                                        else:
                                            print("Le nombre maximale des candidats est atteint.")
                                            




# 6 : fonction creation resultat pour creer le fichier resultat.txt 


def creation_resultat(choix_candidat_exo):
    g = open("resultat.txt","w")
    for k,v in choix_candidat_exo.items():
        ligne = "- Numero CIN : {}  - Code filiere : {}\n".format(str(k),str(v))
        g.write(ligne)
        
    g.close


# option 6 tkinter

def choix6():
    creation_resultat(choix_candidat)







# 7 : fonction  qui permet de tracer une courbe

def courbe_etudiant():
    g = open("notes.txt","r")
    table_cin = []
    table_analyse = []
    table_algebre = []
    table_physique = []
    table_chimie = []
    table_informatique = []
    table_sta = []
    table_francais = []
    table_anglais = []
    while True:
        a = g.readline()
        if a == "":
            break
        a = a.replace("\n","")
        ligne = a.split("  ")
        note_etudiant = ligne[1].split(",")
        table_cin.append(int(ligne[0]))
        table_analyse.append(int(note_etudiant[0]))
        table_algebre.append(int(note_etudiant[1]))
        table_physique.append(int(note_etudiant[2]))
        table_chimie.append(int(note_etudiant[3]))
        table_informatique.append(int(note_etudiant[4]))
        table_sta.append(int(note_etudiant[5]))
        table_francais.append(int(note_etudiant[6]))
        table_anglais.append(int(note_etudiant[7]))

    x = np.linspace(1,len(table_cin),len(table_cin))
    y1 = np.array(table_analyse)
    y2 = np.array(table_algebre)
    y3 = np.array(table_physique)
    y4 = np.array(table_chimie)
    y5 = np.array(table_informatique)
    y6 = np.array(table_sta)
    y7 = np.array(table_francais)
    y8 = np.array(table_anglais)
    chaine_cin = str(table_cin)
    chaine_cin = chaine_cin.replace("[","")
    chaine_cin = chaine_cin.replace("]","")
    plt.plot(x,y1,marker='o', color ='blue', label = 'Analyse') 
    plt.plot(x,y2,marker='o', color ='red', label = 'Algebre')
    plt.plot(x,y3,marker='o', color ='black', label = 'Physique')
    plt.plot(x,y4,marker='o', color ='pink', label = 'Chimie')
    plt.plot(x,y5,marker='o', color ='yellow', label = 'Informatique')
    plt.plot(x,y6,marker='o', color ='cyan', label = 'STA')
    plt.plot(x,y7,marker='o', color ='magenta', label = 'Francais')
    plt.plot(x,y8,marker='o', color ='orange', label = 'Anglais')
    plt.title("Courbe resultat\n(CIN : {})".format(chaine_cin))
    plt.xlabel("Etudiant par CIN")
    plt.ylabel("Notes")
    plt.ylim(0,20)
    plt.xlim(0,len(table_cin)+1)
    plt.xticks(np.linspace(0,len(table_cin)+1,len(table_cin)+2,endpoint=True))
    plt.yticks(np.linspace(0,20,21,endpoint=True))
    plt.legend()
    plt.grid()
    plt.show()
    plt.close()




# option 7 tkinter

def choix7():
    courbe_etudiant()





# creation fenetre

fenetre = Tk()



# personnaliser fenetre

fenetre.title("Capp")
fenetre.geometry("700x500")
fenetre.resizable(width=False,height=False)
#fenetre.iconbitmap("Nouveaulogo.xbm")
fenetre.config(background='#007F7F')


# ajouter texte
titre = Label(fenetre, text = "Bienvenue sur l'application Capp", font = ("georgia", 20), bg = '#007F7F', fg = '#F4FFC5')
titre.place(relx=0.23)


# ajouter bouton

#option 1 
option1 = Button(fenetre, text="1- Creer liste des candidats",anchor='w' ,border=0,font= ("georgia", 15), bg = '#FFB27F', fg= 'black',command=choix1)
option1.place(y=80,x=0,relwidth=0.5)

#option 2
option2 = Button(fenetre, text="2- Remplir le fichier des notes",anchor='w' , font= ("georgia", 15), bg = '#FFB27F', fg= 'black', command=choix2)
option2.place(x=0,y=130,relwidth=0.5)

#option 3 
option3 = Button(fenetre, text="3- creer le dictionnaire des filières",anchor='w' , font= ("georgia", 15), bg = '#FFB27F', fg= 'black',command=choix3)
option3.place(y=180,x=0,relwidth=0.5)

#option 4 
option4 = Button(fenetre, text="4- Trier les candidats",anchor='w' , font= ("georgia", 15), bg = '#FFB27F', fg= 'black',command=choix4)
option4.place(y=230,x=0,relwidth=0.5)

#option 5 
option5 = Button(fenetre, text="5- Creer le dictionnaire choix",anchor='w' , font= ("georgia", 15), bg = '#FFB27F', fg= 'black',command=choix5)
option5.place(y=280,x=0,relwidth=0.5)

#option 6 
option6 = Button(fenetre, text="6- Creer le fichier resultats",anchor='w' , font= ("georgia", 15), bg = '#FFB27F', fg= 'black',command=choix6)
option6.place(y=330,x=0,relwidth=0.5)

#option 7 
option7 = Button(fenetre, text="7- Afficher les statistiques",anchor='w' , font= ("georgia", 15), bg = '#FFB27F', fg= 'black',command=choix7)
option7.place(y=380,x=0,relwidth=0.5)

#option 8 
option8 = Button(fenetre, text="0- Quitter",anchor='w' , font= ("georgia", 15), bg = '#7F0000', fg= 'black',command=fenetre.destroy)
option8.place(y=430,x=0,relwidth=0.5)




# afficher fenetre

fenetre.mainloop()

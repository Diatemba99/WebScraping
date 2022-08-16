from datetime import datetime
import sys
import os
import colorama
import random


couleur = list(vars(colorama.Fore).values())

matriculeEtudiant="ESTM"
now = datetime.now()
matEtudiant = now.strftime("%H%M%S")
date = now.strftime("%Y%m%d")




class Section:
    def __init__(self, numSection, nomSection):
        self.__numSection = numSection
        self.__nomSection = nomSection

    def getNumSection(self):
        return self.__numSection

    def getNomSection(self):
        return self.__nomSection

    # setters

class Projet:
    def __init__(self, numProjet, theme):
        self.__numProjet = numProjet
        self.__theme = theme

    def getNumProjet(self):
        return self.__numProjet

    def getTheme(self):
        return self.__theme

    # setters

class Etudiant:
    def __init__(self, numEtudiant, nom, prenom, section, projet):
        self.__numEtudiant = numEtudiant
        self.__nom = nom
        self.__prenom = prenom
        self.__section = section
        self.__projet = projet

    def getNumEtudiant(self):
        return self.__numEtudiant

    def getNom(self):
        return self.__nom

    def getPrenom(self):
        return self.__prenom

    def getSection(self):
        return self.__section

    def getProjet(self):
        return self.__projet

    # setters

def mainProgram():
    choix = 0
    listeSection = []
    listeProjet = []
    liste = []

    while choix == 0:
        print("▒▒"*50)
        print("▒▒ 1. Creer une section                                                                           ▒▒")
        print("▒▒"*50)
        print("▒▒ 2. Creer un projet                                                                             ▒▒")
        print("▒▒"*50)
        print("▒▒ 3. Creer un etudiant                                                                           ▒▒")
        print("▒▒"*50)
        print("▒▒ 4. Lister les sections                                                                         ▒▒")
        print("▒▒"*50)
        print("▒▒ 5. Lister les projets                                                                          ▒▒")
        print("▒▒"*50)
        print("▒▒ 6. Lister les etudiants                                                                        ▒▒")
        print("▒▒"*50)
        print("▒▒ 7. Afficher les etudiants d'une section donnee                                                 ▒▒")
        print("▒▒"*50)
        print("▒▒ 8. Afficher les etudiants qui travaillent dans un projet donnee                                ▒▒")
        print("▒▒"*50)
        print("▒▒ 9. Afficher pour chaque projet les etudiants qui y travaillent et leurs sections respectives   ▒▒")
        print("▒▒"*50)
        print("▒▒ 10. Sortie                                                                                     ▒▒")
        print("▒▒"*50)

        choix = int(input("Votre choix ? "))

        if choix == 1:
            nomSection = input("Nom section ? ")
            # numSection = int(input("Numero section ?"))
            numSection = "ST" + now.strftime("%H%M%S") + nomSection[:2]
            section = Section(numSection, nomSection)

            listeSection.append(section)
            choix = 0
        else:
            if choix == 2:
                # numProjet = int(input("Numero projet ? "))
                theme = input("Theme ? ")
                numProjet = "PR" + now.strftime("%H%M%S") + theme[:2]
                projet = Projet(numProjet, theme)

                listeProjet.append(projet)
                choix = 0
            else:
                if choix == 3:
                    section = None
                    projet = None

                    nom = input("Nom ? ")
                    prenom = input("Prenom ? ")
                    numEtudiant = "ET" + now.strftime("%H%M%S") + nom[:2]


                    while section == None:
                        # SECTION CONTENTS
                        numSectionCol = "NUMERO_SECTION"
                        nomSectionCol = "NOM SECTION"
                        print("------------------------------------------------------")
                        print("--------------   AFFICHAGE DES DONNEES  --------------")
                        print("------------------------------------------------------")
                        print("{0:20s} {1:20s}".format(numSectionCol,nomSectionCol))
                        print("-" * 60)
                        for i in range(len(listeSection)):
                            print(f"|{listeSection[i].getNumSection():20}",f"|{listeSection[i].getNomSection():19}")
                            print("-" * 60)

                        numSection = input("Numero de la section de l'etudiant ? ")

                        for i in range(len(listeSection)):
                            if listeSection[i].getNumSection() == numSection:
                                section = listeSection[i]
                                break
                        if section == None:
                            print("Section inexsitante")

                    while projet == None:
                        numProjetCol = "NUMERO_PROJET"
                        nomThemeCol = "NOM THEME"
                        print("------------------------------------------------------")
                        print("--------------   AFFICHAGE DES DONNEES  --------------")
                        print("------------------------------------------------------")
                        print("{0:20s} {1:20s}".format(numProjetCol,nomThemeCol))
                        print("-" * 60)
                        for i in range(len(listeProjet)):
                            print(f"|{listeProjet[i].getNumProjet():20}",f"|{listeProjet[i].getTheme():19}")
                            print("-" * 60)
                        numProjet = input("Numero du projet de l'etudiant ? ")

                        for i in range(len(listeProjet)):
                            if listeProjet[i].getNumProjet() == numProjet:
                                projet = listeProjet[i]
                                break
                        if projet == None:
                            print("Projet inexsitant")

                    etudiant = Etudiant(numEtudiant, nom, prenom, section, projet)

                    liste.append(etudiant)

                    choix = 0
                else:
                    if choix == 4:
                        numSectionCol = "NUMERO_SECTION"
                        nomSectionCol = "NOM SECTION"
                        print("------------------------------------------------------")
                        print("--------------   AFFICHAGE DES DONNEES  --------------")
                        print("------------------------------------------------------")
                        print("{0:20s} {1:20s}".format(numSectionCol,nomSectionCol))
                        print("-" * 60)
                        for i in range(len(listeSection)):
                            print(f"|{listeSection[i].getNumSection():20}",f"|{listeSection[i].getNomSection():19}")
                            print("-" * 60)
                            
                        choix = 0
                    else:
                        if choix == 5:
                            numProjetCol = "NUMERO_PROJET"
                            nomThemeCol = "NOM THEME"
                            print("------------------------------------------------------")
                            print("--------------   AFFICHAGE DES DONNEES  --------------")
                            print("------------------------------------------------------")
                            print("{0:20s} {1:20s}".format(numProjetCol,nomThemeCol))
                            print("-" * 60)
                            for i in range(len(listeProjet)):
                                print(f"|{listeProjet[i].getNumProjet():20}",f"|{listeProjet[i].getTheme():19}")
                                print("-" * 60)
                           
                            choix = 0
                        else:
                            if choix == 6:
                                numETUDIANTCol = "NUMERO"
                                nomETUDIANTCol = "NOM"
                                prenomETUDIANTCol = "PRENOM"
                                numSectionCol = "NUM_SECTION"
                                nomSectionCol = "NOM_SECTION"
                                numProjetCol = "NUM_PROJET"
                                themeCol = "THEME"
                                
                                # print("{0:20s} {1:20s} {2:20s} {3:20s} {4:20s} {5:20s} {6:20s}".format(numETUDIANTCol,nomETUDIANTCol,
                                # prenomETUDIANTCol,numSectionCol,nomSectionCol,numProjetCol,themeCol))

                                print("{:20} {:20} {:20} {:20} {:15} {:20} {:16}".format(numETUDIANTCol,nomETUDIANTCol,prenomETUDIANTCol,numSectionCol,nomSectionCol,numProjetCol,themeCol))
                                
                                print("-" * 130)

                                for i in range(len(liste)):
                                    print(f"|{liste[i].getNumEtudiant():20}",f"|{liste[i].getNom():19}",
                                     f"|{liste[i].getPrenom():18}", f"|{liste[i].getSection().getNumSection():17}",
                                     f"|{liste[i].getSection().getNomSection():16}",f"|{liste[i].getProjet().getNumProjet():15}",
                                     f"|{liste[i].getProjet().getTheme():14}")
                                    print("-" * 130)
                                
                                
                                choix = 0
                            else:
                                if choix == 7:
                                    section = None

                                    while section == None:
                                        numSectionCol = "NUMERO_SECTION"
                                        nomSectionCol = "NOM SECTION"
                                        print("------------------------------------------------------")
                                        print("--------------   AFFICHAGE DES DONNEES  --------------")
                                        print("------------------------------------------------------")
                                        print("{0:20s} {1:20s}".format(numSectionCol,nomSectionCol))
                                        print("-" * 60)
                                        for i in range(len(listeSection)):
                                            print(f"|{listeSection[i].getNumSection():20}",f"|{listeSection[i].getNomSection():19}")
                                            print("-" * 60)

                                        numSection = input("Numero section ? ")
                                        for i in range(len(listeSection)):
                                            if (listeSection[i].getNumSection() == numSection):
                                                section = listeSection[i]
                                                break
                                        if section == None:
                                            print("Section inexistant")


                                    # ======================================================
                                    numeTCol = "NUMERO_ETUDIANT"
                                    NOMeTtCol = "NOM"
                                    prenomEtCol = "PRENOM"

                                    print("{0:20s} {1:20s} {2:20s}".format(numeTCol,NOMeTtCol,prenomEtCol))
                                    print("-" * 60)
                                    for i in range(len(liste)):
                                        if section.getNumSection() == liste[i].getSection().getNumSection():
                                            print(f"|{liste[i].getNumEtudiant():20}",f"|{liste[i].getNom():19}",f"|{liste[i].getPrenom():18}")
                                            print("-" * 60)    
                                    
                                    choix = 0

                                else:
                                    if choix == 8:
                                        projet = None

                                        while projet == None:
                                            numProjetCol = "NUMERO_PROJET"
                                            nomThemeCol = "NOM THEME"
                                            print("------------------------------------------------------")
                                            print("--------------   AFFICHAGE DES DONNEES  --------------")
                                            print("------------------------------------------------------")
                                            print("{0:20s} {1:20s}".format(numProjetCol,nomThemeCol))
                                            print("-" * 60)
                                            for i in range(len(listeProjet)):
                                                print(f"|{listeProjet[i].getNumProjet():20}",f"|{listeProjet[i].getTheme():19}")
                                                print("-" * 60)

                                            numProjet = input("Numero projet ? ")

                                            for i in range(len(listeProjet)):
                                                if (listeProjet[i].getNumProjet() == numProjet):
                                                    projet = listeProjet[i]
                                                    break
                                            if projet == None:
                                                print("Projet inexistant")


                                        # ======================================================
                                        numeTCol = "NUMERO_ETUDIANT"
                                        NOMeTtCol = "NOM"
                                        prenomEtCol = "PRENOM"

                                        print("{0:20s} {1:20s} {2:20s}".format(numeTCol,NOMeTtCol,prenomEtCol))
                                        print("-" * 60)
                                        for i in range(len(liste)):
                                            if projet.getNumProjet() == liste[i].getProjet().getNumProjet():
                                                print(f"|{liste[i].getNumEtudiant():20}",f"|{liste[i].getNom():19}",f"|{liste[i].getPrenom():18}")
                                                print("-" * 60)    

                                        choix = 0
                                    else:
                                        if choix == 9:
                                            projet = None

                                            while projet == None:
                                                numProjetCol = "NUMERO_PROJET"
                                                nomThemeCol = "NOM THEME"
                                                print("------------------------------------------------------")
                                                print("--------------   AFFICHAGE DES DONNEES  --------------")
                                                print("------------------------------------------------------")
                                                print("{0:20s} {1:20s}".format(numProjetCol,nomThemeCol))
                                                print("-" * 60)
                                                for i in range(len(listeProjet)):
                                                    print(f"|{listeProjet[i].getNumProjet():20}",f"|{listeProjet[i].getTheme():19}")
                                                    print("-" * 60)

                                                numProjet = input("Numero projet ? ")
                                                for i in range(len(listeProjet)):
                                                    if (listeProjet[i].getNumProjet() == numProjet):
                                                        projet = listeProjet[i]
                                                        break
                                                if projet == None:
                                                    print("Projet inexistant")


                                            # ===================================================
                                            numeTCol = "NUMERO_ETUDIANT"
                                            NOMeTtCol = "NOM"
                                            prenomEtCol = "PRENOM"
                                            numSectionCol = "NUMERO_SECTION"
                                            nomSectionCol = "PRENOM"

                                            print("{0:20s} {1:20s} {2:20s} {3:20s}{4:20s}".format(numeTCol,NOMeTtCol,prenomEtCol,numSectionCol,nomSectionCol))
                                            print("-" * 130)
                                            for i in range(len(liste)):
                                                if projet.getNumProjet() == liste[i].getProjet().getNumProjet():
                                                    print(f"|{liste[i].getNumEtudiant():20}",f"|{liste[i].getNom():19}",f"|{liste[i].getPrenom():18}",
                                                    f"|{liste[i].getSection().getNumSection():17}",f"|{liste[i].getSection().getNomSection():16}",)
                                                    print("-" * 130)   
                                           
                                            choix = 0
                                        else:
                                            if choix == 10:
                                                break
    print("""\  
███████████████████████
█▄─▄▄─█▄─▄█▄─▀█▄─▄███░█
██─▄████─███─█▄▀─████▄█
▀▄▄▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▀
        """)

mainProgram()

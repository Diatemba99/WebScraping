from datetime import datetime
now = datetime.now()
import sys
import os
prenomEt="ESTM"
matEtudiant = prenomEt[:3] + now.strftime("%H%M%S")




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

def main():
    choix = 0
    listeSection = []
    listeProjet = []
    liste = []

    while choix == 0:
        print("1. Creer une section")
        print("2. Creer un projet")
        print("3. Creer un etudiant")
        print("4. Lister les sections")
        print("5. Lister les projets")
        print("6. Lister les etudiants")
        print("7. Afficher les etudiants d'une section donnee")
        print("8. Afficher les etudiants qui travaillent dans un projet donnee")
        print("9. Afficher pour chaque projet les etudiants qui y travaillent et leurs sections respectives")
        print("10. Sortie")
        choix = int(input("Votre choix ? "))

        if choix == 1:
            numSection = int(input("Numero section ?"))
            nomSection = input("Nom section ? ")
            section = Section(numSection, nomSection)

            listeSection.append(section)
            choix = 0
        else:
            if choix == 2:
                numProjet = int(input("Numero projet ? "))
                theme = input("Theme ? ")

                projet = Projet(numProjet, theme)

                listeProjet.append(projet)
                choix = 0
            else:
                if choix == 3:
                    section = None
                    projet = None

                    numEtudiant = int(input("Numero etudiant ? "))
                    nom = input("Nom ? ")
                    prenom = input("Prenom ? ")
                    while section == None:
                        numSection = int(input("Numero de la section de l'etudiant ? "))

                        for i in range(len(listeSection)):
                            if listeSection[i].getNumSection() == numSection:
                                section = listeSection[i]
                                break
                        if section == None:
                            print("Section inexsitante")

                    while projet == None:
                        numProjet = int(input("Numero de la projet de l'etudiant ? "))

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
                        for i in range(len(listeSection)):
                            print("______________________________________")
                            print("Numero section: ",listeSection[i].getNumSection())
                            print("Nom section: ",listeSection[i].getNomSection())
                        print("______________________________________")
                        choix = 0
                    else:
                        if choix == 5:
                            for i in range(len(listeProjet)):
                                print("______________________________________")
                                print("Numero projet: ", listeProjet[i].getNumProjet())
                                print("Theme: ", listeProjet[i].getTheme())
                            print("______________________________________")
                            choix = 0
                        else:
                            if choix == 6:
                                for i in range(len(liste)):
                                    print("______________________________________")
                                    print("Numero etudiant: ", liste[i].getNumEtudiant())
                                    print("Nom: ", liste[i].getNom())
                                    print("Prenom: ", liste[i].getPrenom())
                                    print("- Section -")
                                    print("Numero section: ", liste[i].getSection().getNumSection())
                                    print("Nom section: ", liste[i].getSection().getNomSection())
                                    print("- Projet -")
                                    print("Numero projet: ", liste[i].getProjet().getNumProjet())
                                    print("Theme: ", liste[i].getProjet().getTheme())
                                print("______________________________________")
                                choix = 0
                            else:
                                if choix == 7:
                                    section = None

                                    while section == None:
                                        numSection = int(input("Numero section ? "))
                                        for i in range(len(listeSection)):
                                            if (listeSection[i].getNumSection() == numSection):
                                                section = listeSection[i]
                                                break
                                        if section == None:
                                            print("Section inextante")

                                    for i in range(len(liste)):
                                        if section.getNumSection() == liste[i].getSection().getNumSection():
                                            print("______________________________________")
                                            print("Numero etudiant: ", liste[i].getNumEtudiant())
                                            print("Nom: ", liste[i].getNom())
                                            print("Prenom: ", liste[i].getPrenom())
                                    print("______________________________________")
                                    choix = 0

                                else:
                                    if choix == 8:
                                        projet = None

                                        while projet == None:
                                            numProjet = int(input("Numero projet ? "))
                                            for i in range(len(listeProjet)):
                                                if (listeProjet[i].getNumProjet() == numProjet):
                                                    projet = listeProjet[i]
                                                    break
                                            if projet == None:
                                                print("Projet inextante")

                                        for i in range(len(liste)):
                                            if projet.getNumProjet() == liste[i].getProjet().getNumProjet():
                                                print("______________________________________")
                                                print("Numero etudiant: ", liste[i].getNumEtudiant())
                                                print("Nom: ", liste[i].getNom())
                                                print("Prenom: ", liste[i].getPrenom())
                                        print("______________________________________")
                                        choix = 0
                                    else:
                                        if choix == 9:
                                            projet = None

                                            while projet == None:
                                                numProjet = int(input("Numero projet ? "))
                                                for i in range(len(listeProjet)):
                                                    if (listeProjet[i].getNumProjet() == numProjet):
                                                        projet = listeProjet[i]
                                                        break
                                                if projet == None:
                                                    print("Projet inextante")

                                            for i in range(len(liste)):
                                                if projet.getNumProjet() == liste[i].getProjet().getNumProjet():
                                                    print("______________________________________")
                                                    print("Numero etudiant: ", liste[i].getNumEtudiant())
                                                    print("Nom: ", liste[i].getNom())
                                                    print("Prenom: ", liste[i].getPrenom())
                                                    print("- Section -")
                                                    print("Numero section: ", liste[i].getSection().getNumSection())
                                                    print("Nom section: ", liste[i].getSection().getNomSection())
                                            print("______________________________________")
                                            choix = 0
                                        else:
                                            if choix == 10:
                                                break
    print("FIN DU PROGRAMME :) BISOU MES LOVE")

main()

from urllib import response


class Section : 
    def __init__(self, numero_section, nom_section) :
        self.__numero_section  = numero_section
        self.__nom_section = nom_section

    def getNomSection(self): 
        return self.__nom_section

    def getNumeroSection(self) : 
        return self.__numero_section

class Projet :
    def __init__(self, numero_projet, theme) :
        self.__numero_projet = numero_projet
        self.__theme = theme

    def getNumeroProjet(self) : 
        return self.__numero_projet

    def getTheme(self) : 
        return self.__theme

class Etudiant : 
    def __init__(self,numero, nom, prenom, section , projet ) :
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__projet = projet
        self.__section = section

    def getNumero(self) : 
        return self.__numero
    def getNom(self) : 
        return self.__nom
    def getPrenom(self) : 
        return self.__prenom
    def getSection(self) : 
        return self.__section
    def getProjet(self) :
        return self.__projet

def main() : 
    choix = 0
    reponse = 1
    listeSections = []
    listeProjets = []
    listeEtudiants = []
    
    while choix != 10 : 
        print("\t############## Bienvenue ####################### \n Taper :")
        print("\t1 Pour creer une section")
        print("\t2 Pour creer un projet")
        print("\t3 Pour creer un etudiant")
        print("\t4 Pour lister les sections")
        print("\t5 Pour lister les projets")
        print("\t6 Pour lister les étudiants")
        print("\t7 Pour afficher les étudiants d'une section donnée")
        print("\t8 Pour afficher les étudiants qui travaillent dans un projet donnée")
        print("\t9 Pour afficher pour chaque projet les étudiants qui y travaillent et leurs sections respective")
        print("\t10 Pour quitter")
        choix = int(input())

        if choix == 1 : 
            print("\t--------------Vous allez creer une section--------------")
            numero_section = int(input("Donnez le numéro de la section \n"))
            nom_section = input("Donnez le nom de la section \n")
            section =  Section(numero_section, nom_section) 
            listeSections.append(section)

        elif choix == 2 :
            print("\t--------------Vous allez creer un projet --------------")
            numero_projet = int(input("Donnez le numéro du projet \n"))
            theme = input("Donnez le theme  \n")
            projet = Projet(numero_projet, theme)
            listeProjets.append(projet)
        elif choix == 3 :
            print("\t--------------Vous allez creer un etudiant --------------")
            numero = int(input("Donnez le numéro de l'étudiant  \n"))
            nom = input("Donnez le nom  \n")
            prenom = input("Donnez le prenom \n")
            print("De quelle section est l'étudiant ? \n Taper : ")

            for i in range(len(listeSections)) :
                print(i + 1," Pour la section : ",listeSections[i].getNomSection())

            reponse = int(input())
            section = listeSections[reponse - 1]
            print("\nSur quel projet travail l'étudiant ? \n Taper : ")

            for i in range(len(listeProjets)) :
                print(i + 1," Pour la section : ",listeProjets[i].getTheme())

            reponse = int(input())
            projet = listeProjets[reponse - 1]
            etudiant = Etudiant(numero, nom, prenom, section, projet)
            listeEtudiants.append(etudiant)

        elif choix == 4 : 
            print("-------------------- Liste des sections ----------------------")
            for i in range(len(listeSections)) : 
                print("\t Numéro section : ", listeSections[i].getNumeroSection())
                print("\t Nom section : ", listeSections[i].getNomSection())
                print("\n")

        elif choix == 5  :
            print("-------------------- Liste des projets ----------------------")
            for i in range(len(listeProjets)) : 
                print("\t Numéro projet : ", listeProjets[i].getNumeroProjet())
                print("\t Theme projet : ", listeProjets[i].getTheme())
                print("\n")

        elif choix == 6 :
            print("-------------------- Liste des etudiants ----------------------")
            for i in  range(len(listeEtudiants)) : 
                print("\t Numéro : ", listeEtudiants[i].getNumero())
                print("\t Nom : ", listeEtudiants[i].getNom())
                print("\t Prenom : ", listeEtudiants[i].getPrenom())
                print("\t______Section de l'étudiant")
                print("\t\t Numéro :", listeEtudiants[i].getSection().getNumeroSection())
                print("\t\t Nom :", listeEtudiants[i].getSection().getNomSection())
                print("\t______Projet de l'étudiant ")
                print("\t\t Numéro : ", listeEtudiants[i].getProjet().getNumeroProjet())
                print("\t\t Theme : ", listeEtudiants[i].getProjet().getTheme())

        elif choix == 7 : 
            print("-------------------- Liste des etudiants d'une section----------------------")
            print("Veillez choisir la section \n Taper : ")
            for i in range(len(listeSections)) : 
                print("\t",i+1, " pour la section : ", listeSections[i].getNomSection())
            
            reponse = int(input())
            print("\t########## Liste des étudiants de la section : ", listeSections[reponse - 1].getNomSection())
            for i in range(len(listeEtudiants)) : 
                if listeEtudiants[i].getSection() == listeSections[reponse - 1] :
                    print("\t Numéro : ", listeEtudiants[i].getNumero())
                    print("\t Nom : ", listeEtudiants[i].getNom())
                    print("\t Prenom : ", listeEtudiants[i].getPrenom())
                    print("\t______Projet de l'étudiant ")
                    print("\t\t Numéro : ", listeEtudiants[i].getProjet().getNumeroProjet())
                    print("\t\t Theme : ", listeEtudiants[i].getProjet().getTheme())
        elif choix == 8 : 
            print("-------------------- Liste des etudiants d'un projet ----------------------")
            print("Veillez choisir le projet \n Taper : ")
            for i in range(len(listeProjets)) : 
                print("\t",i+1, " pour la section : ", listeProjets[i].getTheme())

            reponse = int(input())
            print("\t########## Liste des étudiants du projet : ", listeProjets[reponse - 1].getTheme())
            for i in range(len(listeEtudiants)) : 
                if listeEtudiants[i].getProjet() == listeProjets[reponse - 1] :
                    print("\t Numéro : ", listeEtudiants[i].getNumero())
                    print("\t Nom : ", listeEtudiants[i].getNom())
                    print("\t Prenom : ", listeEtudiants[i].getPrenom())
                    print("\t______Section de l'étudiant ")
                    print("\t\t Numéro :", listeEtudiants[i].getSection().getNumeroSection())
                    print("\t\t Nom :", listeEtudiants[i].getSection().getNomSection())

        elif choix == 9 : 
            print("-------------------- Liste des etudiants pour chaque projet ----------------------")
            for i in range(len(listeProjets)) : 
                print("\t################## Projet : ", listeProjets[i].getTheme(), " #####################")
                for j in range(len(listeEtudiants)) :
                    print("\t Numéro : ", listeEtudiants[j].getNumero())
                    print("\t Nom : ", listeEtudiants[j].getNom())
                    print("\t Prenom : ", listeEtudiants[j].getPrenom())
                    print("\t______Section de l'étudiant ")
                    print("\t\t Numéro :", listeEtudiants[j].getSection().getNumeroSection())
                    print("\t\t Nom :", listeEtudiants[j].getSection().getNomSection())


main()
        


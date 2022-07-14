#Class creation
class voiture:
    #Creation of class attributes
    POIDS = 1500
    MOTORISATION = 2.5
    RESERVOIRE = 60

    #creation of attributes
    def __init__(self, usure_pneus, niveau_essence, nb_de_personnes):
        self.usure_pneus = usure_pneus
        self.niveau_essence = niveau_essence
        self.nb_de_personne = nb_de_personnes

    #create our first private method
    def __allumer_voyant_essence(self):
        print('Attention il essence en manque')
    
    #create public method
    def demarrer_voiture(self):
        if self.niveau_essence <= 5:
            self.__allumer_voyant_essence()
        print('vroumm vroum')    

#create and init objet voiture
maVoiture = voiture("normal",5,4)

#using method on objet
maVoiture.demarrer_voiture()













### 1) Debuggez cette erreur et expliquer brievement le problème en commentaire
"""
Nom = 'Sebastien'
print('mon nom est ',Nom)

"""


#2) Faites en sorte que la cellule ci-dessous retourne 'J'apprends le Python' à partir des variables à disposition

"""
debutPhrase = 'J\'apprends '
finPhrase = 'le Python'
print(debutPhrase+finPhrase)

"""

#3) Debugguez le code ci-dessous en modifiant uniquement ce qu'il se trouve dans print(...)
"""
heuresPassees = 2
debutPhrase = 'j\'apprends Python depuis '
finPhrase = ' heures.'

print(debutPhrase+str(heuresPassees)+finPhrase)
"""

#4) quelle sera la valeur de varAge dans le code ci-dessous ? Expliquez en commentaire la raison
"""
varAge = 28
varAge = 30
print(varAge)
#la valeur de la variable serait égale à 30, la premiere valeur sera écrasée pour
#stocker la seconde variable
"""


#5) a) A partir des variables mises à disposition, calculez le taux de conversion et stockez le dans la variable "tauxConversion"

nombreDeVisites = 26736352
nombredeConversions = 973520
tauxConversion = nombredeConversions /nombreDeVisites
print(tauxConversion)

#b) Verifiez le type de la variable en l'imprimant à l'execution de la cellule
print(type(tauxConversion))

#c) faites en sorte que le taux soit en base 100 plutôt qu'en base 1 (ex : avoir 62 plutot que 0.62)
tauxEnPourcentage = tauxConversion*100
print(tauxEnPourcentage)

#d) Imprimez la phrase suivante "Le taux de conversion est (valeur tauxConversion) %"
print("Le taux de conversion est ", tauxEnPourcentage, " %")


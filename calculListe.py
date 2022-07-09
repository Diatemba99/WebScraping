produit = ['Sneackers', 'Boots', 'Pick-Up', 'Rolex']
prix= [12854, 55048, 9896, 5500]
AllProducts = [['Usb',1250], ['Charger',2580], ['Sofware',9875], ['QWANT', 9634]]

#valeur = input("Saisir la valeur à chercher :")

#Looking specified product on liste

"""if valeur in produit:
    print(produit.index(valeur))
else:
    print("Produit manquant")  """  

#Printing length of list

print(len(prix))
print(len(AllProducts[0]))

#Count the accurance of value on list:
dicoLetter = ['a', 'b', 'a', 'c', 'b','e', 'p']

print('This value is present ', dicoLetter.count('a'), 'times')


#Sorting list
print(dicoLetter)
print("dicoLetter after sorting")

dicoLetter.sort()
print(dicoLetter)


#Calculate sum
print("Affichage de la somme")
print(sum(prix))



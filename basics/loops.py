#While loop testing
"""
i=1

while i<=10:
    print(i)
    i=i+1
"""

#For loop 
"""
produit = ['Sneackers', 'Boots', 'Pick-Up', 'Rolex']
prix= [12854, 55048, 9896, 5500]

for pd in produit:
    print(pd)


AllProducts = {'Usb':1250, 'Charger':2580, 'Sofware':9875, 'QWANT': 9634}

for pd,price in AllProducts.items():
    print(pd,price)
    print('*******************')
    print(f'le prix du {pd} est de {price} ')


for i in range(1,10,3):
    print(i)

for j in range(5,-15,-1):
    print(j)
"""

produit = ['Sneackers', 'Boots', 'Pick-Up', 'Rolex']

nbrElement = len(produit)

for i in range(nbrElement):
    print(produit[i])

for i in range(1,15,2):
    print(i)    
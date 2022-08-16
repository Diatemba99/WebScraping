from art import *
import colorama
import time
import random
import os
import time
from tqdm import tqdm


#setting randow color 
couleur = list(vars(colorama.Fore).values())

def imagesAnimated():
    ESTM=text2art("ESTM",font='block',chr_ignore=True)
    print(ESTM)
                                                        

#function permettant d'afficher le contenu de cette 
def affichage():
    for i in range(50):   
        time.sleep(0.001)
        #j'affiche et je change la couleur du contenu
        print(random.choice(couleur),"▒▒"*54)
    #le systeme patiente 3 secondes avant d'effacer l'écran avec cls
    time.sleep(2)    
    os.system('cls')

    for i in range(5):
        #j'affiche et je change la couleur du contenu de la fonction pr214
        print(random.choice(couleur),imagesAnimated())   
        time.sleep(1)
        os.system('cls')

def loading():
    print("""\
        
███████╗░██████╗████████╗███╗░░░███╗   
██╔════╝██╔════╝╚══██╔══╝████╗░████║
█████╗░░╚█████╗░░░░██║░░░██╔████╔██║
██╔══╝░░░╚═══██╗░░░██║░░░██║╚██╔╝██║
███████╗██████╔╝░░░██║░░░██║░╚═╝░██║
╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝
                    """)  

    for _ in tqdm(range(100), desc="Chargement..."):
        time.sleep(0.05)
        


loading()
affichage()






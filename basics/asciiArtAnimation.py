import colorama
import time
import random
import os

#setting randow color 
couleur = list(vars(colorama.Fore).values())

def imagesAnimated():
    print("""\
**********************************SSSSSSSSSSSS**********************************
******************************SSSSSSSSSSSSSSSSSSSS******************************
****************************SSSSSSSSSSSSSSSSSSSSSSSS****************************
***************************SSSSSSSSSSSSSSSSSSSSSSSSSS***************************
**************************SSSSSSSSSSSSSSSSSSSSSSSSSSSS**************************
*************************SSSSSSSSSSSSSSSSSSSSSSSSSSSSSS*************************
********************SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS********************
***************SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS***************
***********SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS***********
********SSSSSSSSSSSSSSSSSSSSS######&&&&&&&&&&######SSSSSSSSSSSSSSSSSSSSS********
******SSSSSSSSSSSSSSSSSSS##&&@@@@@@@@@@@@@@@@@@@@@@&&##SSSSSSSSSSSSSSSSSSS******
*****SSSSSSSSSSSSSSSSSSS#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&SSSSSSSSSSSSSSSSSSS*****
****SSSSSSSSSSSSSSSSSSS#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#SSSSSSSSSSSSSSSSSSS****
***SSSSSSSSSSSSSSSSSSSS&@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@&SSSSSSSSSSSSSSSSSSSS***
***SSSSSSSSSSSSSSSSSSSS@@@@@&######&@@@@@@@@@@@@@@@@@@@@@SSSSSSSSSSSSSSSSSSSS***
***SSSSSSSSSSSSSSSSSSSS####SSS#######&@@@@&##############SSSSSSSSSSSSSSSSSSSS***
****SSSSSSSSSSSSSSSSSSSSS#&&&&&&&&&#SSSSSSSS#&&&&&&#S##SSSSSSSSSSSSSSSSSSSSS****
*****SSSSSSSSSSSSSSS&##S&@@@@&&&&&@@&S####S&@@&&&&&@@@@&S##&SSSSSSSSSSSSSSS*****
*******SSSSSSSSSSSS#@@&S&@@@&&&SSS&@@S&@@&S@@&&&#SS#@@@&S&@@#SSSSSSSSSSSS*******
*********SSSSSSSSSS#@@&S#@@@@@@&##@@&#@@@@S&@@@@@##&@@@#S&@@#SSSSSSSSSS*********
************SSSSSSSS@@&###&@@@@@@@&##&@@@@&#&&@@@@@@&&###&@@SSSSSSSS************
****************SSSS#@&#@&########&&@@@@@@@@&########&&@#&@#SSSS****************
*********************SS#&@@@@@@@@@&&#######&&&&@@@@@@@@&#SS*********************
***********************S#&@@@@@@#######&&#######@@@@@@&#S***********************
***********************S##&&@@@##&@@########@@&##@@@&&##S***********************
************************S########@@@#SSSSSS#@@@########S************************
*************************S#######@@@@&####&@@@@#######S*************************
**************************S#######&@@@@&&@@@@&#######S**************************
****************************S#######&######&#######S****************************
*******************************S################SS******************************
*********************************&&&&######&&&&*********************************
*******************************S@@@@@@@@@@@@@@@@S*******************************
*****************************S@:!@@@@@@@@@@@@@@!:@S*****************************
**********************SS#####@:.!@@@@@@@@@@@@@@!.:@#####S***********************
*******************S###&#####%.:!@@@@@@@@@@@@@@!:.%#####&###S*******************
*****************S#&#########@:::!$@@@@@@@@@@$!:::@#########&#S*****************
***************S#&############@!..!%@@@@@@@@%!..!@############&#S***************
**************#&##############S#$@#SS######SS#@$#S##############&#**************
************S#################SSSSSSSSSSSSSSSSSSSS#################S************
***********S##################SSSSSSSSSSSSSSSSSSSS##################S***********
***********####################SSSSSSSSSSSSSSSSSS########&@&#########***********
**********#&###################SSSSSSSSSSSSSSSSSS######&%*!*@#######&#**********
**********#####################SSSSSSSSSSSSSSSSSS######&&&&&&#########**********
**********#####################SSSSSSSSSSSSSSSSSS####################&**********
**********######################SSSSSSSSSSSSSSSS######################**********
**********######################SSSSSSSSSSSSSSSS######################**********
                    """)                           


#function permettant d'afficher le contenu de cette 
def affichage():
    for i in range(100):   
        time.sleep(0.001)
        #j'affiche et je change la couleur du contenu
        print(random.choice(couleur),"❤️"*65)
    #le systeme patiente 3 secondes avant d'effacer l'écran avec cls
    time.sleep(3)    
    os.system('cls')

    for i in range(20):
        #j'affiche et je change la couleur du contenu de la fonction pr214
        print(random.choice(couleur),imagesAnimated())   
        time.sleep(2)
        os.system('cls')

affichage()

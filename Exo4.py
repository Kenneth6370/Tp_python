import math
import time

class Prog:

    def Read(self,valeur):
        fich = open(valeur,"r")
        return int(fich.read())

    def Syracuse(self,number):
        valeur = "Etapes de Sycaruse : \n"
        while(number !=1):
            valeur+=str(number)+"\n"
            if (number % 2) == 0:
                number =number /2
            else:
                number =  number*3+1
        return valeur
    
    def Write(self,str,fichier):
        fich = open(fichier,"w")
        fich.write(str)
        fich.close

classe = Prog()
valeurRead = classe.Read("FichierIn.txt")
valeurWrite = classe.Syracuse(valeurRead)
classe.Write(valeurWrite,"FichierWrite.txt")
from pgn_parser import pgn, parser
import numpy as np
from abc import ABC

"""
Classe instanziamento della scacchiera
e metodi utilizzati per le chiamate ai pezzi
"""

class scacchiera():
    
    def __init__(self):
        self.posizioni = np.chararray((8,8), unicode = True)

    """
    Metodo che riceve in ingresso il nome di una casella e ne restituisce le
    coordinate relative all'array dei char della scacchiera'
    """
    def get_casa(self,casa,giocatore):
        posizione = [0,0]
        temp = []   
        for ch in casa:
            temp.append(ch)           
        file = temp[0]  #Lettera sulla scacchiera (colonna)
        rank = temp[1]  #Numero sulla scacchiera (fila)
        
        if giocatore == 0:
             posizione[0] = ord(file)-ord('a') 
             posizione[1] = int(rank)-1
        else:
             posizione[0] = ord(file)-ord('A')
             posizione[1] = int(rank)-1
             
        return tuple(posizione)






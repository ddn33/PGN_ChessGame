import numpy as np
from pedone import pedone
from cavallo import cavallo
from torre import torre
from alfiere import alfiere
from king import king
from regina import regina
from pezzi import color

"""
Classe instanziamento della scacchiera
e metodi utilizzati per le chiamate ai pezzi
"""


class board():

    def __init__(self):
        self.scacchiera = np.chararray((8, 8), unicode=True)
        self.file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.rank = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.pedoni_bianco = []
        self.cavalli_bianco = []
        self.torri_bianco = []
        self.alfieri_bianco = []
        self.pedoni_nero = []
        self.cavalli_nero = []
        self.torri_nero = []
        self.alfieri_nero = []
        self.regina_bianco = []
        self.king_bianco = []
        self.regina_nero = []
        self.king_nero = []
        self.caselle_occupate = []
        for i in range(8):
            self.pedoni_bianco.append(pedone(color.BIANCO.name, self.file[i]+self.rank[1] , self))

        self.cavalli_bianco.append(cavallo(color.BIANCO.name, 'b1', self))
        self.torri_bianco.append(torre(color.BIANCO.name, 'a1', self))
        self.alfieri_bianco.append(alfiere(color.BIANCO.name, 'c1', self))
        self.cavalli_bianco.append(cavallo(color.BIANCO.name, 'g1', self))
        self.torri_bianco.append(torre(color.BIANCO.name, 'h1', self))
        self.alfieri_bianco.append(alfiere(color.BIANCO.name, 'f1', self))
        self.regina_bianco.append(regina(color.BIANCO.name, 'd1', self))
        self.king_bianco.append(king(color.BIANCO.name, 'e1', self))

        for i in range(8):
            self.pedoni_nero.append(pedone(color.NERO.name, self.file[i]+self.rank[6], self))

        self.cavalli_nero.append(cavallo(color.NERO.name, 'c8', self))
        self.torri_nero.append(torre(color.NERO.name, 'a8', self))
        self.alfieri_nero.append(alfiere(color.NERO.name, 'c8', self))
        self.cavalli_nero.append(cavallo(color.NERO.name, 'g8', self))
        self.torri_nero.append(torre(color.NERO.name, 'h8', self))
        self.alfieri_nero.append(alfiere(color.NERO.name, 'f8', self))
        self.regina_nero.append(regina(color.NERO.name, 'd8', self))
        self.king_nero.append(king(color.NERO.name, 'e8', self))
        
        "lista dei pezzi presenti nella scacchiera"
        self.pezzi_bianchi = self.pedoni_bianco + self.cavalli_bianco + self.alfieri_bianco + self.torri_bianco + self.king_bianco + self.regina_bianco
        self.pezzi_neri = self.pedoni_nero + self.cavalli_nero + self.alfieri_nero + self.torri_nero + self.king_nero + self.regina_nero
        self.pezzi = self.pezzi_bianchi + self.pezzi_neri
        
        for pezzo in self.pezzi:
            self.caselle_occupate.append(pezzo.casa)
    
    def aggiorna_scacchiera(self):
         for pezzo in self.pezzi:
            self.caselle_occupate.append(pezzo.casa)
        
        
    def is_free_la_casella(self,posizione):
        casa = self.get_casa(posizione)
        if casa in self.caselle_occupate:
             return False
        else:
             return True
         
    def get_posizione_casa(self,casa):
        posizione = [0, 0]
        temp = []
        for ch in casa:
            temp.append(ch)
        file = temp[0]  # Lettera sulla scacchiera (colonna)
        rank = temp[1]  # Numero sulla scacchiera (fila)
    
        posizione[0] = ord(file) - ord('a')
        posizione[1] = int(rank) - 1
    
        return tuple(posizione)

    def get_casa(self,posizione):
    
        a = chr(posizione[0]+ord('a'))
        b = str(posizione[1]+1)
        
        return str(a+b)



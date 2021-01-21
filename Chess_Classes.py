from pgn_parser import pgn, parser

import numpy as np


"""
Classe che contiene i comandi utilizzabili dal main per il proseguimento della partita e 
il controllo dello stato dei pezzi sulla scacchiera relativa ad una determinata partita
"""


class partita():
    
    """"
    al momento di inzio di una nuova partita crea una nuova istanza della classe scacchiera
    contenente tutte le caselle di una scacchiera
    """
    def __init__(self,lista_mosse=[]):
        self.scacchiera = scacchiera()
        self.lista_mosse = lista_mosse
        
        
    def get_scacchiera(self):
        for pezzo in self.scacchiera.pezzi:
            self.scacchiera.posizioni[pezzo.casella]= pezzo.simbolo
        print(self.scacchiera.posizioni)
        return 

    def muovi(self):
       pass

class scacchiera():

    def __init__(self):
        self.posizioni = np.chararray((8,8), unicode = True)
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
        "istanziamento pezzi bianchi(0 = white)"
        for i in range(8):
            self.pedoni_bianco.append(pedone(0,(i,1)))
        for i in range(2):
            self.cavalli_bianco.append(cavallo(0,((i*5)+1,0)))
            self.torri_bianco.append(torre(0,(i*7,0)))
            self.alfieri_bianco.append(alfiere(0,((i*3)+2,0)))
        self.regina_bianco.append(regina(0,(3,0)))
        self.king_bianco.append(king(0,(4,0)))
       
        "istanziamento pezzi neri(1 = black)"
        for i in range(8):
            self.pedoni_nero.append(pedone(1,(i,6)))
        for i in range(2):
            self.cavalli_nero.append(cavallo(1,((i*5)+1,7)))
            self.torri_nero.append(torre(1,(i*7,7)))
            self.alfieri_nero.append(alfiere(1,((i*3)+2,7)))
        self.regina_nero.append(regina(1,(3,7)))
        self.king_nero.append(king(1,(4,7)))
        
        "lista dei pezzi presenti nella scacchiera"
        self.pezzi_bianchi = self.pedoni_bianco + self.cavalli_bianco + self.alfieri_bianco + self.torri_bianco + self.king_bianco + self.regina_bianco
        self.pezzi_neri = self.pedoni_nero + self.cavalli_nero + self.alfieri_nero + self.torri_nero + self.king_nero + self.regina_nero
        self.pezzi = self.pezzi_bianchi + self.pezzi_neri
        

       

# class casella():
#     def __init__(self, nomecasella):
#         self.nome = nomecasella


class pezzo():
    
    def __init__(self, colore, casella):
        self.colore = colore
        self.casella = casella

    def get_posizione(self):
        return self.casella  
    
    def mossa(self, colore, casella):
        pass


    def get_mossa(self):
        pass




class pedone(pezzo):
    def __init__(self, colore, casella):
        if colore == 0:
            self.simbolo = 'P'
        else:
            self.simbolo = 'p'
        super().__init__(colore, casella)


class king(pezzo):
    def __init__(self, colore, casella):
        if colore == 0:
            self.simbolo = 'K'
        else:
            self.simbolo = 'k'
        super().__init__(colore, casella)


class cavallo(pezzo):
    def __init__(self, colore, casella):
        if colore == 0:
            self.simbolo = 'C'
        else:
            self.simbolo = 'c'
        super().__init__(colore, casella)


class alfiere(pezzo):
    def __init__(self, colore, casella):
        if colore == 0:
            self.simbolo = 'A'
        else:
            self.simbolo = 'a'
        super().__init__(colore, casella)


class torre(pezzo):
    def __init__(self, colore, casella):
        if colore == 0:
            self.simbolo = 'T'
        else:
            self.simbolo = 't'
        super().__init__(colore, casella)


class regina(pezzo):
    def __init__(self, colore, casella):
        if colore == 0:
            self.simbolo = 'Q'
        else:
            self.simbolo = 'q'
        super().__init__(colore, casella)

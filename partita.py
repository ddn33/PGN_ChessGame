import scacchiera
from Arbitro import arbitro
"""
Classe che contiene i comandi utilizzabili dal main per il proseguimento della partita e 
il controllo dello stato dei pezzi sulla scacchiera relativa ad una determinata partita
"""


class partita():
    """"
    al momento di inzio di una nuova partita crea una nuova istanza della classe scacchiera
    contenente tutte le caselle di una scacchiera
    """

    def __init__(self, lista_mosse=[]):
        self.scacchiera = scacchiera.board()
        self.lista_mosse = lista_mosse
        self.arbitro = arbitro(self,self.scacchiera)

    def muovi(self,mossa):
        if mossa.cattura == True:
            if self.arbitro.cattura_valida(mossa):
                "MUOVI"
            else:
                "MOSSA NON VALIDA"
        else:    
            if self.arbitro.mossa_valida(mossa):
                "MUOVI"
            else:
                "MOSSA NON VALIDA"
        
            
        



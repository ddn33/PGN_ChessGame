import scacchiera
from Arbitro import arbitro
from mossa import mossa

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
        if mossa.arrocco_corto == True or mossa.arrocco_lungo == True:
            mossa.arrocco(self.scacchiera,mossa)
            
        elif mossa.cattura == True:
            if self.arbitro.cattura_valida(mossa):
                pezzo_da_muovere = self.scacchiera.quale_pezzo_si_muove(mossa)
                
                for pezzo in self.scacchiera.pezzi:
                    if pezzo.casa == mossa.casa:
                        self.scacchiera.pezzi.remove(pezzo)
                        # break                
                pezzo_da_muovere.casa = mossa.casa
                
            else:
                print("MOSSA NON VALIDA")
        else:    
            if self.arbitro.mossa_valida(mossa):
                pezzo_da_muovere = self.scacchiera.quale_pezzo_si_muove(mossa)
                pezzo_da_muovere.casa = mossa.casa
            else:
                "MOSSA NON VALIDA"
        
        
        
        
        self.scacchiera.aggiorna_scacchiera()
            
        



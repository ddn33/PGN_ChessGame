import scacchiera
from Arbitro import arbitro
from mossa import mossa
from pezzi import color
from pedone import pedone
from cavallo import cavallo
from torre import torre
from alfiere import alfiere
from king import king
from regina import regina
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
        
        elif mossa.promozione == True:
            if self.arbitro.mossa_valida(mossa):
                pezzo_da_muovere = self.scacchiera.quale_pezzo_si_muove(mossa)
                self.scacchiera.pezzi.remove(pezzo_da_muovere)
        
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
        
        return
    
    
    "Metodo che crea il nuovo pezzo da promuovere" 
    def crea_pezzo_promozione(self,mossa):
        
        if mossa.colore == color.BIANCO.name:
        
            if mossa.pezzo_promozione == 'Q':
                self.scacchiera.pezzi.append(regina(color.BIANCO.name, mossa.casa, self.scacchiera))
            elif mossa.pezzo_promozione == 'R':
                self.scacchiera.pezzi.append(torre(color.BIANCO.name, mossa.casa, self.scacchiera))
            elif mossa.pezzo_promozione == 'N':
                self.scacchiera.pezzi.append(cavallo(color.BIANCO.name, mossa.casa, self.scacchiera))
            elif mossa.pezzo_promozione == 'B':
                self.scacchiera.pezzi.append(alfiere(color.BIANCO.name, mossa.casa, self.scacchiera))
        else:
            
            if mossa.pezzo_promozione == 'Q':
                self.scacchiera.pezzi.append(regina(color.NERO.name, mossa.casa, self.scacchiera))
            elif mossa.pezzo_promozione == 'R':
                self.scacchiera.pezzi.append(torre(color.NERO.name, mossa.casa, self.scacchiera))
            elif mossa.pezzo_promozione == 'N':
                self.scacchiera.pezzi.append(cavallo(color.NERO.name, mossa.casa, self.scacchiera))
            elif mossa.pezzo_promozione == 'B':
                self.scacchiera.pezzi.append(alfiere(color.NERO.name, mossa.casa, self.scacchiera))
        
        return
            
        



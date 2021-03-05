import numpy as np
import scacchiera
from Arbitro import arbitro
from pezzi import color
from cavallo import cavallo
from torre import torre
from alfiere import alfiere
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
        self.immagine = np.chararray((8, 8), unicode=True)
        self.scacchiera = scacchiera.board()
        self.lista_mosse = lista_mosse
        self.arbitro = arbitro(self,self.scacchiera)

    def muovi(self,mossa):
        if mossa.arrocco_corto == True or mossa.arrocco_lungo == True:
            self.scacchiera.arrocco(self.scacchiera,mossa)
        
        elif mossa.promozione == True:
            if mossa.cattura == True:
                if self.arbitro.cattura_valida(mossa):
                    self.cattura(mossa)
                    pezzo_da_muovere = self.scacchiera.quale_pezzo_si_muove(mossa)
                    self.scacchiera.pezzi.remove(pezzo_da_muovere)
                    self.crea_pezzo_promozione(mossa)
                    
            else:                                  
                if self.arbitro.mossa_valida(mossa):
                    pezzo_da_muovere = self.scacchiera.quale_pezzo_si_muove(mossa)
                    self.scacchiera.pezzi.remove(pezzo_da_muovere)
                    self.crea_pezzo_promozione(mossa)
        
        elif mossa.cattura == True:
            if self.arbitro.cattura_valida(mossa):
                self.cattura(mossa)
                pezzo_da_muovere = self.scacchiera.quale_pezzo_si_muove(mossa)
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
          
    def cattura(self,mossa):
        for pezzo in self.scacchiera.pezzi:
            if pezzo.casa == mossa.casa:
                self.scacchiera.pezzi.remove(pezzo)    
        return
     
    def get_scacchiera(self):
        self.immagine = np.chararray((8, 8), unicode=True)
        for pezzo in self.scacchiera.pezzi:
            self.immagine[self.scacchiera.get_posizione_casa(pezzo.casa)]= pezzo.simbolo
        print(self.immagine)
        return 


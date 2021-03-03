from pezzi import pezzo, color
from alfiere import alfiere
from torre import torre

class regina(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'Q'
        else:
            self.simbolo = 'q'
        self.nome = 'Q'
        super().__init__(colore, casa, scacchiera)

    def puoi_andare_in(self,mossa):
        mosse_possibili = self.lista_mosse_possibili_regina()
        
        if mossa.casa in mosse_possibili:
            return True
        else:
            return False


    def lista_mosse_possibili_regina(self):
        
        
        """
        le mosse che può effettuare la regina sono la somma delle mosse
        che potrebbe effettuare un alfiere e quelle che potrebbe effettuare una
        torre, quindi unendo i metodi lista_mosse_possibili relativi ad alfiere
        e torre possiamo ricavare tutte le mosse che può effettuare una regina
        """
        
        mosse_diagonali = alfiere.lista_mosse_possibili_alfiere(self)
        mosse_parallele = torre.lista_mosse_possibili_torre(self)
        case_possibili = mosse_diagonali+mosse_parallele

        return case_possibili
        
        
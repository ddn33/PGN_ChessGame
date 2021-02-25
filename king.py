from pezzi import pezzo, color

class king(pezzo):
    
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO:
            self.simbolo = 'K'
        else:
            self.simbolo = 'k'
        super().__init__(colore, casa, scacchiera)

    def puoi_andare_in(self):
        pass


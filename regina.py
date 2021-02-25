from pezzi import pezzo, color

class regina(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO:
            self.simbolo = 'Q'
        else:
            self.simbolo = 'q'
        super().__init__(colore, casa, scacchiera)

    def puoi_andare_in(self):
        pass

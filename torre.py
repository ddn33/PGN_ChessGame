from pezzi import pezzo, color

class torre(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO:
            self.simbolo = 'T'
        else:
            self.simbolo = 't'
        super().__init__(colore, casa, scacchiera)

    def puoi_andare_in(self):
        pass
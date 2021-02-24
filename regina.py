from pezzi import pezzo, color

class regina(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'Q'
        else:
            self.simbolo = 'q'
        super().__init__(colore, casa, scacchiera)



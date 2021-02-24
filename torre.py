from pezzi import pezzo, color

class torre(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'T'
        else:
            self.simbolo = 't'
        super().__init__(colore, casa, scacchiera)


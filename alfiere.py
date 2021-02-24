from pezzi import pezzo, color

class alfiere(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'A'
        else:
            self.simbolo = 'a'
        super().__init__(colore, casa, scacchiera)



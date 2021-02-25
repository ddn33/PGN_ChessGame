from pezzi import pezzo, color

class cavallo(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'C'
        else:
            self.simbolo = 'c'
        super().__init__(colore, casa, scacchiera)

    def puoi_andare_in(self):
        pass
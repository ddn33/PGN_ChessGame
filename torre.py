from pezzi import pezzo, color

class torre(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'T'
        else:
            self.simbolo = 't'
        self.nome = 'R'
        super().__init__(colore, casa, scacchiera)

    def puoi_andare_in(self):
        pass
from abc import ABC
from Partita import color

class pezzo(ABC):

    def __init__(self, colore, casa, scacchiera):
        self.colore = colore
        self.casella = casa
        self.scacchiera = scacchiera

    def get_posizione(self):
        return self.casella

    def puoi_andare_in(self, casella):
        risposta = True
        risposta = False
        return risposta

    def get_mossa(self):
        pass


class pedone(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'P'
        else:
            self.simbolo = 'p'
        super().__init__(colore, casa, scacchiera)


class king(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'K'
        else:
            self.simbolo = 'k'
        super().__init__(colore, casa, scacchiera)


class cavallo(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'C'
        else:
            self.simbolo = 'c'
        super().__init__(colore, casa, scacchiera)


class alfiere(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'A'
        else:
            self.simbolo = 'a'
        super().__init__(colore, casa, scacchiera)


class torre(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'T'
        else:
            self.simbolo = 't'
        super().__init__(colore, casa, scacchiera)


class regina(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'Q'
        else:
            self.simbolo = 'q'
        super().__init__(colore, casa, scacchiera)





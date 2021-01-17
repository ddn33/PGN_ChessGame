from pgn_parser import pgn, parser

class partita():
    """"
    al momento di inzio di una nuova partita crea una nuova istanza della classe scacchiera
    contenente tutte le caselle di una scacchiera
    """
    def __init__(self):
        self.scacchieranew = scacchiera()

class scacchiera():

    def __init__():
        self.posizioni = {}


class casella():
    pass


class pezzo():
    def __init__(self,colore,casella):
        self.colore = colore
        self.posizione = casella

    
    def mossa(self,colore,casella):
        pass

class pedone(pezzo):
    pass

class re (pezzo):
    pass

class cavallo(pezzo):
    pass

class alfiere(pezzo):
    pass

class torre(pezzo):
    pass

class regina(pezzo):
    pass


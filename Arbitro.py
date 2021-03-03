from pezzi import color


class arbitro():
    
    
    def __init__(self,partita,scacchiera):
        self.partita = partita
        self.scacchiera = scacchiera
        
    def mossa_valida(self,mossa):
        if mossa.colore == color.BIANCO.name:
                if mossa.casa in self.scacchiera.caselle_occupate_bianco:
                    return False
                else:
                    return True
        elif mossa.colore == color.NERO.name:
                if mossa.casa in self.scacchiera.caselle_occupate_nero:
                    return False
                else:
                    return True
    
    def cattura_valida(self,mossa):
        if mossa.colore == color.BIANCO.name:
                if mossa.casa in self.scacchiera.caselle_occupate_nero:
                    return True
                else:
                    return False
        elif mossa.colore == color.NERO.name:
                if mossa.casa in self.scacchiera.caselle_occupate_bianco:
                    return True
                else:
                    return False
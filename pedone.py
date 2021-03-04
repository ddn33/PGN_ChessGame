from pezzi import pezzo, color


class pedone(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'P'
        else:
            self.simbolo = 'p'
        self.nome = 'P'
        super().__init__(colore, casa, scacchiera)
        
        
    def puoi_andare_in(self,mossa):
        
        if self.colore == color.BIANCO.name:
            mosse_possibili = self.lista_mosse_possibili_pedone_bianco(mossa)
        else:
            mosse_possibili = self.lista_mosse_possibili_pedone_nero(mossa)
        
        return mossa.casa in mosse_possibili
        
      
    def lista_mosse_possibili_pedone_bianco(self,mossa):
        mosse_possibili = []
        #identifico la posizione del pedone sulla scacchiera
        casa_attuale = self.scacchiera.get_posizione_casa(self.casa)
        
        #identificazione delle varie casistiche che possono presentarsi nel
        #muovere un pedone:
            
        #se la mossa è di cattura il pedone deve muoversi in diagonale
        if mossa.cattura == True: 
            mosse_possibili.append((casa_attuale[0]+1,casa_attuale[1]+1)) 
            mosse_possibili.append((casa_attuale[0]-1,casa_attuale[1]+1))
        
        #la prima mossa del pedone può essere di 1 o 2 passi in avanti
        #e deve essere verificato che le caselle siano vuote per permettere al
        #pezzo di muoversi
        elif self.prima_mossa == True and self.scacchiera.is_free_la_casella((casa_attuale[0],casa_attuale[1]+1)):           
            newposizione1 = (casa_attuale[0],casa_attuale[1]+1)
            mosse_possibili.append(newposizione1)
            if self.scacchiera.is_free_la_casella((casa_attuale[0],casa_attuale[1]+2)):
                newposizione2 = (casa_attuale[0],casa_attuale[1]+2)
                mosse_possibili.append(newposizione2)
        
        # se non è la prima mossa e non è una mossa di cattura il pedone può
        # solamente fare 1 passo in avanti 
        elif self.scacchiera.is_free_la_casella((casa_attuale[0],casa_attuale[1]+1)):
            newposizioni = (casa_attuale[0],casa_attuale[1]+1)
            mosse_possibili.append(newposizioni)
        
        #si ritrasformano le posizioni nel nome delle caselle
        case_possibili = []
        for i in range(len(mosse_possibili)):
            case_possibili.append(self.scacchiera.get_casa(tuple(mosse_possibili[i])))
                                                        
        return case_possibili
    
    def lista_mosse_possibili_pedone_nero(self,mossa):
        #i passaggi logici sono gli stessi usati per il pedone bianco
        mosse_possibili = []
        casa_attuale = self.scacchiera.get_posizione_casa(self.casa)
        if mossa.cattura == True:
            mosse_possibili.append((casa_attuale[0]-1,casa_attuale[1]-1))        
            mosse_possibili.append((casa_attuale[0]+1,casa_attuale[1]-1))
        elif self.prima_mossa == True and self.scacchiera.is_free_la_casella((casa_attuale[0],casa_attuale[1]-1)):           
            newposizione1 = (casa_attuale[0],casa_attuale[1]-1)
            mosse_possibili.append(newposizione1)
            if self.scacchiera.is_free_la_casella((casa_attuale[0],casa_attuale[1]-2)):
                newposizione2 = (casa_attuale[0],casa_attuale[1]-2)
                mosse_possibili.append(newposizione2)
        elif self.scacchiera.is_free_la_casella((casa_attuale[0],casa_attuale[1]-1)):
            newposizioni = (casa_attuale[0],casa_attuale[1]-1)
            mosse_possibili.append(newposizioni)
        
        case_possibili = []
        for i in range(len(mosse_possibili)):
            case_possibili.append(self.scacchiera.get_casa(tuple(mosse_possibili[i])))
        
        return case_possibili
        



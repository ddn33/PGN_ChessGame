from pezzi import pezzo, color


class pedone(pezzo):
    def __init__(self, colore, casa, scacchiera):
        self.prima_mossa = True
        if colore == color.BIANCO.name:
            self.simbolo = 'P'
        else:
            self.simbolo = 'p'
        super().__init__(colore, casa, scacchiera)
        
        
    def puoi_andare_in(self,mossa):
        
        if self.colore == color.BIANCO.name:
            mosse_possibili = self.lista_mosse_possibili_pedone_bianco(mossa)
        else:
            mosse_possibili = self.lista_mosse_possibili_pedone_nero(mossa)
        if mossa.casa in mosse_possibili:
            return True
        else:
            return False
        
      
    def lista_mosse_possibili_pedone_bianco(self,mossa):
        mosse_possibili = []
        casa_attuale = self.scacchiera.get_posizione_casa(self.casa)
        if mossa.cattura == True:
            mosse_possibili.append((casa_attuale[0]+1,casa_attuale[1]+1)) 
            mosse_possibili.append((casa_attuale[0]-1,casa_attuale[1]+1))
        elif self.prima_mossa == True:           
            newposizione1 = (casa_attuale[0],casa_attuale[1]+1)
            newposizione2 = (casa_attuale[0],casa_attuale[1]+2)
            mosse_possibili.append(newposizione1)
            mosse_possibili.append(newposizione2)
        else:
            newposizioni = (casa_attuale[0],casa_attuale[1]+1)
            mosse_possibili.append(newposizioni)
          
        case_possibili = []
        for i in range(len(mosse_possibili)):
            case_possibili.append(self.scacchiera.get_casa(tuple(mosse_possibili[i])))
                                                        
        return case_possibili
    
    def lista_mosse_possibili_pedone_nero(self,mossa):
        mosse_possibili = []
        casa_attuale = self.scacchiera.get_posizione_casa(self.casa)
        if mossa.cattura == True:
            mosse_possibili.append((casa_attuale[0]-1,casa_attuale[1]-1))        
            mosse_possibili.append((casa_attuale[0]+1,casa_attuale[1]-1))
        elif self.prima_mossa == True:           
            newposizione1 = (casa_attuale[0],casa_attuale[1]-1)
            newposizione2 = (casa_attuale[0],casa_attuale[1]-2)
            mosse_possibili.append(newposizione1)
            mosse_possibili.append(newposizione2)
        else:
            newposizioni = (casa_attuale[0],casa_attuale[1]-1)
            mosse_possibili.append(newposizioni)
        
        case_possibili = []
        for i in range(len(mosse_possibili)):
            case_possibili.append(self.scacchiera.get_casa(tuple(mosse_possibili[i])))
        
        return case_possibili
        



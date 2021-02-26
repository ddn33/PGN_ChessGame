from pezzi import pezzo, color


class pedone(pezzo):
    def __init__(self, colore, casa, scacchiera):
        self.prima_mossa = True
        if colore == color.BIANCO.name:
            self.simbolo = 'P'
        else:
            self.simbolo = 'p'
        super().__init__(colore, casa, scacchiera)
        
        
    def puoi_andare_in(self,casa_nuova):
        
        if self.colore == color.BIANCO.name:
            mosse_possibili = self.lista_mosse_possibili_pedone_bianco()
        else:
            mosse_possibili = self.lista_mosse_possibili_pedone_nero()
        if casa_nuova in mosse_possibili:
            return True
        else:
            return False
        
      
    def lista_mosse_possibili_pedone_bianco(self):
        mosse_possibili = []
        casa_attuale = self.scacchiera.get_posizione_casa(self.casa)
        if self.prima_mossa == True:           
            newposizione1 = (casa_attuale[0],casa_attuale[1]+1)
            newposizione2 = (casa_attuale[0],casa_attuale[1]+2)
            mosse_possibili.append(newposizione1)
            mosse_possibili.append(newposizione2)
        else:
            newposizioni = (casa_attuale[0],casa_attuale[1]+1)
            mosse_possibili.append(newposizioni)
        
        if self.scacchiera.is_free_la_casella((casa_attuale[0]+1,casa_attuale[1]+1)) == False:
            mosse_possibili.append((casa_attuale[0]+1,casa_attuale[1]+1))
        if self.scacchiera.is_free_la_casella((casa_attuale[0]-1,casa_attuale[1]+1)) == False:
            mosse_possibili.append((casa_attuale[0]-1,casa_attuale[1]+1))
        
        print(mosse_possibili)
        case_possibili = []
        for i in range(len(mosse_possibili)):
            case_possibili.append(self.scacchiera.get_casa(tuple(mosse_possibili[i])))
           
                                              
        return case_possibili
    
    def lista_mosse_possibili_pedone_nero(self):
        mosse_possibili = []
        casa_attuale = self.scacchiera.get_posizione_casa(self.casa)
        if self.prima_mossa == True:           
            newposizione1 = (casa_attuale[0],casa_attuale[1]-1)
            newposizione2 = (casa_attuale[0],casa_attuale[1]-2)
            mosse_possibili.append(newposizione1)
            mosse_possibili.append(newposizione2)
        else:
            newposizioni = (casa_attuale[0],casa_attuale[1]-1)
            mosse_possibili.append(newposizioni)
        
        if self.scacchiera.is_free_la_casella((casa_attuale[0]-1,casa_attuale[1]-1)) == False:
            mosse_possibili.append((casa_attuale[0]-1,casa_attuale[1]-1))
        if self.scacchiera.is_free_la_casella((casa_attuale[0]+1,casa_attuale[1]-1)) == False:
            mosse_possibili.append((casa_attuale[0]+1,casa_attuale[1]-1))
        
        print(mosse_possibili)
        case_possibili = []
        for i in range(len(mosse_possibili)):
            case_possibili.append(self.scacchiera.get_casa(tuple(mosse_possibili[i])))
           
                                              
        return case_possibili
        



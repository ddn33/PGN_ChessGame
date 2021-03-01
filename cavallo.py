from pezzi import pezzo, color

class cavallo(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'C'
        else:
            self.simbolo = 'c'
        super().__init__(colore, casa, scacchiera)

    def puoi_andare_in(self,mossa):
        
        mosse_possibili = self.lista_mosse_possibili_cavallo()
        
        if mossa.casa in mosse_possibili:
            return True
        else:
            return False
        
        
    def lista_mosse_possibili_cavallo(self):
        mosse_possibili = []
        casa_attuale = self.scacchiera.get_posizione_casa(self.casa)
        
        if casa_attuale[0]-1 >=0 and casa_attuale[1]-2 >=0:
            mosse_possibili.append((casa_attuale[0]-1,casa_attuale[1]-2))
        if casa_attuale[0]-2 >=0 and casa_attuale[1]-1 >=0:  
            mosse_possibili.append((casa_attuale[0]-2,casa_attuale[1]-1))
        if casa_attuale[0]-2 >=0 and casa_attuale[1]+1 <=7:
            mosse_possibili.append((casa_attuale[0]-2,casa_attuale[1]+1))
        if casa_attuale[0]+1 <=7 and casa_attuale[1]-2 >=0:    
            mosse_possibili.append((casa_attuale[0]+1,casa_attuale[1]-2))
        if casa_attuale[0]-1 >=0 and casa_attuale[1]+2 <=7:
            mosse_possibili.append((casa_attuale[0]-1,casa_attuale[1]+2))
        if casa_attuale[0]+2 <=7 and casa_attuale[1]-1 >=0:
            mosse_possibili.append((casa_attuale[0]+2,casa_attuale[1]-1))
        if casa_attuale[0]+1 <=7 and casa_attuale[1]+2 <=7:
            mosse_possibili.append((casa_attuale[0]+1,casa_attuale[1]+2))
        if casa_attuale[0]+2 <=7 and casa_attuale[1]+1 <=7:
            mosse_possibili.append((casa_attuale[0]+2,casa_attuale[1]+1))
            
        case_possibili = []
        for i in range(len(mosse_possibili)):
            case_possibili.append(self.scacchiera.get_casa(tuple(mosse_possibili[i])))
        print(case_possibili)     
                                          
        return case_possibili
            
            
            
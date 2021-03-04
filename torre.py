from pezzi import pezzo, color

class torre(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'T'
        else:
            self.simbolo = 't'
        self.nome = 'R'
        super().__init__(colore, casa, scacchiera)

    def puoi_andare_in(self,mossa):
                
        mosse_possibili = self.lista_mosse_possibili_torre()
        
        return mossa.casa in mosse_possibili
        
    def lista_mosse_possibili_torre(self):
        mosse_possibili = []
        casa_attuale = self.scacchiera.get_posizione_casa(self.casa)
        
        """
        la costruzione delle mosse possibili della torre è uguale a quella 
        dell'alfiere, l'unica differenza è la direzione di movimento
        coerentemente con le regole del gioco è parallela agli assi della 
        scacchiera (e non in diagonale)
        """
        
        stop = False
        i = 1
        while stop == False:
            if stop == False and casa_attuale[0]+i<=7:
                mosse_possibili.append((casa_attuale[0]+i,casa_attuale[1]))
            else:
                stop = True
            if self.scacchiera.is_free_la_casella((casa_attuale[0]+i,casa_attuale[1])) == False:
                stop = True
            i = i+1
            
        stop = False
        i = 1
        while stop == False:
            if stop == False and casa_attuale[0]-i>=0:
                mosse_possibili.append((casa_attuale[0]-i,casa_attuale[1]))
            else:
                stop = True
            if self.scacchiera.is_free_la_casella((casa_attuale[0]-i,casa_attuale[1])) == False:
                stop = True
            i = i+1
            
        stop = False
        i = 1
        while stop == False:
            if stop == False and casa_attuale[1]-i>=0:
                mosse_possibili.append((casa_attuale[0],casa_attuale[1]-i))
            else:
                stop = True
            if self.scacchiera.is_free_la_casella((casa_attuale[0],casa_attuale[1]-i)) == False:
                stop = True
            i = i+1
            
        stop = False
        i = 1
        while stop == False:
            if stop == False and casa_attuale[1]+i<=7:
                mosse_possibili.append((casa_attuale[0],casa_attuale[1]+i))
            else:
                stop = True
            if self.scacchiera.is_free_la_casella((casa_attuale[0],casa_attuale[1]+i)) == False:
                stop = True
            i = i+1
                 
        case_possibili = []
        for i in range(len(mosse_possibili)):
            case_possibili.append(self.scacchiera.get_casa(tuple(mosse_possibili[i])))
      
            
        return case_possibili
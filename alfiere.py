from pezzi import pezzo, color

class alfiere(pezzo):
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO:
            self.simbolo = 'A'
        else:
            self.simbolo = 'a'
        self.nome = 'B'
        super().__init__(colore, casa, scacchiera)

    def puoi_andare_in(self,mossa):
        
        mosse_possibili = self.lista_mosse_possibili_alfiere()
        
        if mossa.casa in mosse_possibili:
            return True
        else:
            return False
        
    def lista_mosse_possibili_alfiere(self):
        mosse_possibili = []
        casa_attuale = self.scacchiera.get_posizione_casa(self.casa)
        
        #lungo tutte le direzioni diagonali che può prendere l'alfiere viene 
        #controllata la prima volta che si incontra un pezzo o che si superano i 
        #bordi della scacchiera cosicchè il ciclo che include le caselle possibili 
        #si ferma in modo da non permettere al pezzo di 'saltare' altri pezzi o
        #di uscire dalla scacchiera.
        
        #la casella con il primo pezzo incontrato viene inclusa nelle caselle possibili
        #perchè nel caso della cattura l'alfiere prenderà il posto del pezzo
        #mentre se la casella è occupata da un pezzo dello stesso colore, la classe
        #arbitro non permetterebbe di compiere quella mossa
        stop = False
        i = 1
        while stop == False:
            if stop == False and casa_attuale[0]+i<=7 and casa_attuale[1]+i <= 7:
                mosse_possibili.append((casa_attuale[0]+i,casa_attuale[1]+i))
            else:
                stop = True
            if self.scacchiera.is_free_la_casella((casa_attuale[0]+i,casa_attuale[1]+i)) == False:
                stop = True
            i = i+1
            
        stop = False
        i = 1
        while stop == False:
            if stop == False and casa_attuale[0]+i<=7 and casa_attuale[1]-i >= 0:
                mosse_possibili.append((casa_attuale[0]+i,casa_attuale[1]-i))
            else:
                stop = True
            if self.scacchiera.is_free_la_casella((casa_attuale[0]+i,casa_attuale[1]-i)) == False:
                stop = True
            i = i+1
                
        stop = False
        i = 1
        while stop == False:
            if stop == False and casa_attuale[0]-i>=0 and casa_attuale[1]-i >= 0:
                mosse_possibili.append((casa_attuale[0]-i,casa_attuale[1]-i))
            else:
                stop = True
            if self.scacchiera.is_free_la_casella((casa_attuale[0]-i,casa_attuale[1]-i)) == False:
                stop = True
            i = i+1
                
        stop = False
        i = 1
        while stop == False:
            if stop == False and casa_attuale[0]-i>=0 and casa_attuale[1]+i <= 7:
                mosse_possibili.append((casa_attuale[0]-i,casa_attuale[1]+i))
            else:
                stop = True
            if self.scacchiera.is_free_la_casella((casa_attuale[0]-i,casa_attuale[1]+i)) == False:
                stop = True
            i = i+1
                    
        case_possibili = []
        for i in range(len(mosse_possibili)):
            case_possibili.append(self.scacchiera.get_casa(tuple(mosse_possibili[i])))
        print(case_possibili) 
        
        return case_possibili


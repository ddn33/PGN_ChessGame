from pezzi import pezzo, color

class king(pezzo):
    
    def __init__(self, colore, casa, scacchiera):
        if colore == color.BIANCO.name:
            self.simbolo = 'K'
        else:
            self.simbolo = 'k'
        self.nome = 'K'
        super().__init__(colore, casa, scacchiera)

    def puoi_andare_in(self,mossa):
        mosse_possibili = self.lista_mosse_possibili_king()
        
        if mossa.casa in mosse_possibili:
            self.prima_mossa = False
            return True
        else:
            return False
    
    def lista_mosse_possibili_king(self):
        
        mosse_possibili = []
        casa_attuale = self.scacchiera.get_posizione_casa(self.casa)
        """
        le mosse del re sono uguali alla regina (alfiere+torre) ma può effettuare
        lo spostamento solo per una distanza pari a 1 casella.
        si verifica che il re non esca dalla scacchiera, mentre la presenza di un
        pezzo dello stesso colore che blocca il re viene controllata dalla classe
        Arbitro (come per tutti gli altri pezzi)
        """
          
    
        #direzioni parallele agli assi della scacchiera
        if casa_attuale[0]+1<=7:
            mosse_possibili.append((casa_attuale[0]+1,casa_attuale[1]))
                      
        if casa_attuale[0]-1>=0:
            mosse_possibili.append((casa_attuale[0]-1,casa_attuale[1]))
                        
        if casa_attuale[1]-1>=0:
            mosse_possibili.append((casa_attuale[0],casa_attuale[1]-1))
            
        if casa_attuale[1]+1<=7:
            mosse_possibili.append((casa_attuale[0],casa_attuale[1]+1))
            
         
        #direzioni diagonali 
        if casa_attuale[0]+1<=7 and casa_attuale[1]+1 <= 7:
            mosse_possibili.append((casa_attuale[0]+1,casa_attuale[1]+1))
         
        if casa_attuale[0]+1<=7 and casa_attuale[1]-1 >= 0:
            mosse_possibili.append((casa_attuale[0]+1,casa_attuale[1]-1))

        if casa_attuale[0]-1>=0 and casa_attuale[1]-1 >= 0:
            mosse_possibili.append((casa_attuale[0]-1,casa_attuale[1]-1))

        if casa_attuale[0]-1>=0 and casa_attuale[1]+1 <= 7:
            mosse_possibili.append((casa_attuale[0]-1,casa_attuale[1]+1))

        case_possibili = []
        for i in range(len(mosse_possibili)):
            case_possibili.append(self.scacchiera.get_casa(tuple(mosse_possibili[i])))
     
        
        return case_possibili 
            
            
            
            
            
            
            
            
            
            
            



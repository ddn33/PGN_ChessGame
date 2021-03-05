
from partita import partita
from sottoprogrammi import pgn_parser
from sottoprogrammi import get_features_mosse


FILENAME = 'Partita-9060.pgn'

lista_mosse = pgn_parser(FILENAME)

p = partita()
a = get_features_mosse(lista_mosse)

"""
Metodo che esegue una partita completa
"""
def gioca_partita_completa():
        p = partita()
        a = get_features_mosse(lista_mosse)
        for mossa in a[0]:
            p.muovi(mossa)
            
        p.get_scacchiera()
    
"""
metodo che esegue le mosse di una partita fino 
al numero indicato in input
"""
def esegui_fino_alla_mossa_numero(num):
        p = partita()
        a = get_features_mosse(lista_mosse)
        i = 0
        while i <= num:
            p.muovi(a[0][i])
            i = i+1
        
        p.get_scacchiera()
        
"""
Metodo che esegue una mosse selezionata da una lista mosse con il quale
è stata instanziata una partita
"""    
def esegui_la_mossa(partita,lista_mosse,num):
       
       partita.muovi(lista_mosse[0][num])
       partita.get_scacchiera
       
       
       
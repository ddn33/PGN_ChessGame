
from partita import partita
from sottoprogrammi import pgn_parser
from sottoprogrammi import get_features_mosse


FILENAME = 'Partita-9060.pgn'

lista_mosse = pgn_parser(FILENAME)

p = partita()
a = get_features_mosse(lista_mosse)

def gioca_partita_completa():
        i = 0
        for mossa in a[0]:
            p.muovi(mossa)
            i = i+1
            print(i)
    
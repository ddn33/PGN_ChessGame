
from partita import partita
from sottoprogrammi import pgn_parser
from sottoprogrammi import get_features_mosse


FILENAME = 'Partita-9060.pgn'

lista_mosse = pgn_parser(FILENAME)

p = partita()
a = get_features_mosse(lista_mosse)

p.scacchiera.pedoni_bianco[2].casa = 'c4'
p.scacchiera.aggiorna_scacchiera()
p.muovi(a[0][6])
    
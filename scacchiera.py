from pezzi import pedone, cavallo, torre, alfiere, king, regina
import metodi
from Partita import color
from pgn_parser import pgn, parser
import numpy as np
from abc import ABC

"""
Classe instanziamento della scacchiera
e metodi utilizzati per le chiamate ai pezzi
"""


class board():

    def __init__(self):
        self.scacchiera = np.chararray((8, 8), unicode=True)
        self.file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.rank = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in range(8):
            pedone(color.BIANCO, self.rank[1] + self.file[i], self)

        cavallo(color.BIANCO, 'b1', self)
        torre(color.BIANCO, 'a1', self)
        alfiere(color.BIANCO, 'c1', self)
        cavallo(color.BIANCO, 'g1', self)
        torre(color.BIANCO, 'h1', self)
        alfiere(color.BIANCO, 'f1', self)
        regina(color.BIANCO, 'd1', self)
        king(color.BIANCO, 'e1', self)

        for i in range(8):
            pedone(1, self.rank[6] + self.file[i], self)

        cavallo(color.NERO, 'c8', self)
        torre(color.NERO, 'a8', self)
        alfiere(color.NERO, 'c8', self)
        cavallo(color.NERO, 'g8', self)
        torre(color.NERO, 'h8', self)
        alfiere(color.NERO, 'f8', self)
        regina(color.NERO, 'd8', self)
        king(color.NERO, 'e8', self)

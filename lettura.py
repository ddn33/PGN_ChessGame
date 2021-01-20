# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:52:01 2021

@author: geomc
"""
# import pgn

# from pgn2bitboard.main import choosePositions
# from pgn2bitboard.main import winner
# from pgn2bitboard.main import pgn2fen
# from pgn2bitboard.main import fen2bitboard
# from pgn2bitboard.main import pgn2bitboard
import chess.pgn
import numpy as np


pgnFile = open('./World Team Championship 2010/Partita-9059.pgn')
game = chess.pgn.read_game(pgnFile)

node = game
positions = []
moves = []
# All positions and moves until the game ends
while not node.is_end():
        nextNode = node.variation(0)
        move = node.board().san(nextNode.move)
        position = nextNode.board().fen()
        moves.append(move)
        positions.append(position)
        node = nextNode


# -----------------------------------------------------------ALtro metodo------------------------------
bitboards = np.zeros((8, 8))
# labels = np.ndarray((0, 1))
# count = 0

# Mosse eseguite Restityuisce le FEN e le posizioni
# posizioni = pgn2fen(game)

#Permette di leggere le FEN
# posizioni1 = fen2bitboard()

# while game is not None:
#         win = winner(game)
#         if win in ['w', 'b']:
#             positions, moves = pgn2fen(game)
#             positions = choosePositions(positions, moves)
#             for position in positions:
#                 bitboard = fen2bitboard(position)
#                 label = 1 if win == 'w' else 0
#                 label = np.array([[label]])
#                 bitboards = np.append(bitboards, bitboard, axis=0)
#                 labels = np.append(labels, label, axis=0)
#                 count += 1

#         game = chess.pgn.read_game(pgnFile)
        
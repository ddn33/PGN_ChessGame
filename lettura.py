# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:52:01 2021

@author: geomc
"""
import pgn
# from pgn2bitboard.main import choosePositions
# from pgn2bitboard.main import winner
# from pgn2bitboard.main import pgn2fen
# from pgn2bitboard.main import fen2bitboard
# from pgn2bitboard.main import pgn2bitboard
# import chess
# import numpy as np

pgn_text = open('./World Team Championship 2010/Partita-9060.pgn').read()
pgn_game = pgn.PGNGame()
# Returns a list of PGNGame
print (pgn.loads(pgn_text))
print (pgn.dumps(pgn_game)) # Returns a string with a pgn game

# pgnFile = open('./World Team Championship 2010/Partita-9059.pgn')
# game = chess.pgn.read_game(pgnFile)
# bitboards = np.ndarray((0, 773))
# labels = np.ndarray((0, 1))
# count = 0

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
        
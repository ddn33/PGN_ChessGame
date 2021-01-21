# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:52:01 2021

@author: geomc
"""


def pgn_parser(filename):
    
    import chess.pgn 
    pgn=open(('./World Team Championship 2010/'+ filename),'r')
    
    game = chess.pgn.read_game(pgn)
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
        
    return moves
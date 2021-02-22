# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:52:01 2021

@author: geomc
"""


def pgn_parser(filename):
    
    import chess.pgn
    import pandas as pd
    pgn=open(('./World Team Championship 2010/'+ filename),'r')
    
    game = chess.pgn.read_game(pgn)
    node = game
    moves = []
    # All positions and moves until the game ends
    while not node.is_end():
        nextNode = node.variation(0)
        move = node.board().san(nextNode.move)
        moves.append(move)
        node = nextNode
        list_df = pd.DataFrame(moves)
        list_df = list_df.rename(columns= {0: 'mosse'} )
                
    return list(list_df['mosse'])


def get_features_mosse(lista_mosse):
    """
    IL SEGUENTE DATAFRAME CONTIENE TUTTE LE INFORMAZIONI NECESSARIE PER IDENTIFICARE
    UNIVOCAMENTE LA MOSSA RELATIVA AD UN PEZZO SULLA SCACCHIERA, OGNI COLONNA è RICAVATA
    ANALIZZANDO LA LISTA DELLE MOSSE ESTRATTA DAL FILE PGN
    """
    mossa_feature = []
    for i in range(len(lista_mosse)):
        mossa_feature[i] = {'pezzo':'0','casa':0,'cattura':False, 'arrocco_corto':False, 'arrocco_lungo':False, 'promozione':False,'pezzo_promozione': None,}
    
    for mossa in lista_mosse:
        for ch in mossa:
            if ch.isupper():
                mossa_feature[mossa]['pezzo'] = ch
    return mossa_feature
    
    
    
    
    
    
    
    
    




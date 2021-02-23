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
    
    "creazione lista delle informazioni necessarie per ogni mossa da effettuare"
    mossa_feature = []
    for i in range(len(lista_mosse)):
        mossa_feature.append({'pezzo':'0','colore':0,'casa':0,'cattura':False, 'arrocco_corto':False, 'arrocco_lungo':False, 'promozione':False,'pezzo_promozione': None})
    
    
    "parte 1: identificazione del pezzo da muovere, mosse di arrocco e cattura dei pezzi"
    count = 0
    for mossa in lista_mosse:
        for ch in mossa:
            if ch.isupper() and ch != 'O':
                mossa_feature[count]['pezzo'] = ch
                lista_mosse[count] = lista_mosse[count].replace(ch,'')
            elif ch == 'x':
                mossa_feature[count]['cattura'] = True
                lista_mosse[count] = lista_mosse[count].replace(ch,'')
            elif lista_mosse[count] == 'O-O' :
                mossa_feature[count]['pezzo'] = 'K'
                mossa_feature[count]['arrocco_corto'] = True
            elif lista_mosse[count] == 'O--O' :
                mossa_feature[count]['pezzo'] = 'K'
                mossa_feature[count]['arrocco_lungo'] = True              
        count +=1
        
    count = 0
    for mossa in lista_mosse:
        if mossa_feature[count]['pezzo'] == '0':
             mossa_feature[count]['pezzo'] = 'P'
        count +=1
        
    "parte 2: identificazione del colore del pezzo che deve effettuare la mossa"
    count = 0
    for mossa in range(len(mossa_feature)):
        if mossa%2 == 0:
            mossa_feature[count]['colore'] = 'BIANCO'
        else:
            mossa_feature[count]['colore'] = 'NERO'
        count +=1
    
    "parte 3: identificazione della casa verso la quale deve muoversi il pezzo"
    
    print(lista_mosse)
    
    return mossa_feature
    
    
    
    
    


def get_posizione_casa(casa):
    posizione = [0, 0]
    temp = []
    for ch in casa:
        temp.append(ch)
    file = temp[0]  # Lettera sulla scacchiera (colonna)
    rank = temp[1]  # Numero sulla scacchiera (fila)

    posizione[0] = ord(file) - ord('a')
    posizione[1] = int(rank) - 1

    return tuple(posizione)

    
    
    
    
    




from mossa import mossa


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
        mossa_feature.append({'pezzo':'0','colore':0,'casa':0,'cattura':False, 'arrocco_corto':False, 'arrocco_lungo':False, 'promozione':False,'pezzo_promozione': None, 'scacco':False, 'conflitto':False, 'conflitto_posizione': None})
    
    
    lista_mosse1=lista_mosse[:]
    
    "parte 1: identificazione del pezzo che deve essere promosso"
    count = 0
    for m in lista_mosse1:
        i=0
        for ch in m:
            if ch == '=':
                mossa_feature[count]['promozione'] = True
                lista_mosse1[count] = lista_mosse1[count].replace(ch,'')
                mossa_feature[count]['pezzo_promozione'] = m[i+1]
                lista_mosse1[count] = lista_mosse1[count].replace(m[i+1],'')            
            i +=1        
                
        count +=1
 
    "parte 2: identificazione del pezzo da muovere, mosse di arrocco e cattura dei pezzi"
    count = 0
    for m in lista_mosse1:
        for ch in m:
            if ch.isupper() and ch != 'O':
                mossa_feature[count]['pezzo'] = ch
                lista_mosse1[count] = lista_mosse1[count].replace(ch,'')
            elif ch == 'x':
                mossa_feature[count]['cattura'] = True
                lista_mosse1[count] = lista_mosse1[count].replace(ch,'')
            elif lista_mosse1[count] == 'O-O' :
                mossa_feature[count]['pezzo'] = 'K'
                mossa_feature[count]['arrocco_corto'] = True
            elif lista_mosse1[count] == 'O--O' :
                mossa_feature[count]['pezzo'] = 'K'
                mossa_feature[count]['arrocco_lungo'] = True

        count +=1
                
    count = 0
    for m in lista_mosse1:
        if mossa_feature[count]['pezzo'] == '0':
             mossa_feature[count]['pezzo'] = 'P'
        count +=1
        
    "parte 3: identificazione del colore del pezzo che deve effettuare la mossa"
    count = 0
    for m in range(len(mossa_feature)):
        if m%2 == 0:
            mossa_feature[count]['colore'] = 'BIANCO'
        else:
            mossa_feature[count]['colore'] = 'NERO'
        count +=1
    
    "parte 4: identificazione dello scacco"
    count=0
    for m in lista_mosse1:
        for ch in m:
            if ch == '+':
                mossa_feature[count]['scacco'] = True
                lista_mosse1[count] = lista_mosse1[count].replace(ch,'')

        count +=1
    
    
    "parte 5: identificazione dei conflitti"
    count=0
    for m in lista_mosse1:
        if len (m) >= 3 :
            mossa_feature[count]['conflitto'] = True
            mossa_feature[count]['conflitto_posizione'] = m[0]
            lista_mosse1[count] = lista_mosse1[count].replace(m[0],'')
        count +=1

    "parte 6: identificazione della casa"
    count=0
    for m in lista_mosse1:
            mossa_feature[count]['casa'] = (m)
            count +=1
    
    
    print(lista_mosse)
    
    
    mosse = []
    for m in mossa_feature:
        mosse.append(mossa(m))
    
    return mosse, mossa_feature, lista_mosse1

    







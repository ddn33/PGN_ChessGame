README:
- PGN_ChessGame, Program for Chess games simulation (From PGN)

TRACCIA:
- Gruppo 4 (Prof. Marcello Esposito Studenti: Camarda Nicola-Di Noto Daniele)
  Realizzare un applicativo che riceva in input il tracciato di una partita di scacchi codificata in formato PGN (Portable Game Notation) e mostri in output la situazione finale dei pezzi sulla scacchiera.
  Estensione: estendere il programma per verificare se il tracciato contiene mosse illegali o impossibili.

INTRO:
- Questa repository fornisce un algoritmo che simula una partita di scacchi in formato PGN.

PREREQUISITI:
- E' necessario aver installato i seguenti software sulla macchina prima di eseguire l'applicazione:
1. Python 3: https://www.python.org/downloads/
2. Anaconda: Installerà la maggior parte delle librerie necessarie https://www.anaconda.com/download/

LIBRERIE:
- Chess			: Libreria utilizzata per la lettura del file PGN.
- Numpy			: Libreria usata per la descrizione delle coordinate della scacchiera.

STRUTTURA DEL FILE:
- |-- Readme.md
- |-- World Team Championship 2010	: Dataset delle partite in formato PGN
- |-- main.py				: Interfaccia per l'utilizzo utente
- |-- alfiere.py				
- |-- cavallo.py				
- |-- king.py				
- |-- pedone.py	
- |-- regina.py				
- |-- Torre.py				
- |-- Arbitro.py				
- |-- mossa.py				
- |-- partita.py				
- |-- pezzi.py					
- |-- scacchiera.py
- |-- sottoprogrammi.py

ISTRUZIONI:
1. Scaricare la repository dal link di GitHub https://github.com/ddn33/PGN_ChessGame

2. Aprire il file Main.py

3. Inserire il nome della partita da assegnare a FILENAME. La lista delle partite si trova all'interno della cartella World Team Championship 2010.
   (Esempio: FILENAME='Partita-9060.pgn')	

4. Scegliere l'opportuno comando di gioco
	- gioca_partita_completa()		: Metodo che effettua tutte le mosse della partita selezionata
	- esegui_fino_alla_mossa_numero(num)	: Metodo che effettua tutte le mosse della partita selezionata fino al num inserito in input  
  

OUTPUT:
- L'utente riceverà in output lo stato finale dei pezzi sulla scacchiera.

ESEMPIO:
- L'esempio che si vuole riportare fa riferimento alla 'Partita-9060':

1. FILENAME = 'Partita-9060.pgn'
2. Precedere con la compilazione del programma
3. Sulla Console digitare gioca_partita_completa()
4. Compilare nuovamente
5. L'utente riceverà in output la seguente immagine

- ['' 'P' '' '' '' '' '' '']
- ['' ''  '' '' '' '' '' '']
- ['' ''  '' '' '' '' '' '']
- ['' ''  '' '' '' '' '' '']
- ['' 't' '' '' '' '' '' '']
- ['' '' '' '' 'T' '' 'p' '']
- ['' 'P' 'K' '' '' '' '' 'k']
- ['' '' 'P' '' '' '' 'p' '']

LEGENDA:
- lettera maiuscola: pezzo bianco
- lettera minuscola: pezzo nero
- t/T: Torre
- a/A: Alfiere
- c/C: Cavallo
- k/K: Re
- q/Q: Regina
- p/P: Pedone

- La parte sinistra della scacchiera indica la zona del giocatore bianco, la parte destra la zona del giocatore nero

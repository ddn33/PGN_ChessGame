# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 16:49:43 2021

@author: geomc
"""

class mossa():
    
    def __init__(self,mossa):
        self.pezzo = mossa['pezzo']
        self.colore = mossa['colore']
        self.cattura = mossa['cattura']
        self.casa = mossa['casa']
        self.arrocco_corto = mossa['arrocco_corto']
        self.arrocco_lungo = mossa['arrocco_lungo']
        self.promozione = mossa['promozione']
        self.pezzo_promozione = mossa['pezzo_promozione']
        self.scacco = mossa['scacco']
        self.conflitto = mossa['conflitto']
        self.conflitto_posizione = mossa['conflitto_posizione']
        
        
         
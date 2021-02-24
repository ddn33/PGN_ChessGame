from abc import ABC, abstractmethod
from enum import Enum



class pezzo(ABC):

    def __init__(self, colore, casa, scacchiera):
        self.colore = colore
        self.casa = casa
        self.scacchiera = scacchiera

    def dove_sei(self):
        return self.casa

    
    @abstractmethod
    
    def puoi_andare_in(self):
        pass


class color(Enum):
    
    BIANCO = 1
    NERO = 2


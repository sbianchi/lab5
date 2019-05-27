import math
import random
from copy import deepcopy
import os
import time

from damaschinas import *

#Funcion que llama un jugador para mover una pieza del tablero

def move(estado,jugador,tipo,weights):
    def qLearning(estado,jugador):
        result = [1,1,1,1,random.randint(0,100)]
        return result
    def smartSearch(estado,jugador,weights):
        return estado.evalFunction(jugador,weights)

    bestMove = None
    maxval = -10000000
    for successor in estado.getSuccessors():
        if tipo == 'smart':
            score = smartSearch(successor,jugador,weights)
        else:
            score = randomSearch(successor,jugador)
        if (score[4] > maxval):
            maxval, bestMove = score[4],successor
    return bestMove

#Clase jugador

class player():
    def __init__(self,ws,jugador,tipo):
        self.jugador = jugador
        self.tipo = tipo
        self.weights = ws
        
    def play(self,estado):
        return move(estado,self.jugador,self.tipo,self.weights)
        
    def weights(self,ws):
        self.weights = ws    
import math
import random
from copy import deepcopy
import os
import time
import sklearn

from damaschinas import *
from jugador import *

# 100 PARTIDAS ENTRE LOS DOS JUGADORES ENTRENADOS 
maxIter=50

#Pesos del jugador entrenado con version previa
weightsPrev = [1, 0.9, 0.09, 0.09]

resultados = open("resultados.csv", "w")

for i in range(1,101):
    fichas = 10
    lado = 4
    grilla = deepcopy([[1,1,1,1,0,0,0,0,0],[1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,2],[0,0,0,0,0,0,0,2,2],[0,0,0,0,0,0,2,2,2],[0,0,0,0,0,2,2,2,2]])
    estado_juego = DamasChinasEstado(grilla,lado,fichas,1,[])
    jugador1=player(weightsPrev,1,'smart')
    jugador2=player(weightsRandom,2,'smart')
   
    j=1
    iter = 0
    while (iter < maxIter):
        iter+=1
        if (j==1):
            estado_juego=jugador1.play(estado_juego)
            j=2
        else:
            estado_juego=jugador2.play(estado_juego)
            j=1    
        
        if (estado_juego.whoWins()):
            for fila in estado_juego.grilla:
                print(fila)
            break

    resultados.write("Juego"+str(i)+","+estado_juego.whoWins()+"\n")   

resultados.close() 
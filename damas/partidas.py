import math
import random
from copy import deepcopy
import os
import time

from damaschinas import *
from jugador import *
from redneuronal import *

# 100 PARTIDAS ENTRE LOS DOS JUGADORES ENTRENADOS 
maxIter=1000

#Pesos del jugador entrenado con version previa
weights = [1, 0.9, 0.09, 0.09]

#resultados = open("resultados.csv", "w")
red = RedNeuronal()

for i in range(1,2):
    fichas = 10
    lado = 4
    grilla = deepcopy([[1,1,1,1,0,0,0,0,0],[1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,2],[0,0,0,0,0,0,0,2,2],[0,0,0,0,0,0,2,2,2],[0,0,0,0,0,2,2,2,2]])
    estado_juego = DamasChinasEstado(grilla,lado,fichas,1,[],red)
    jugador1=player(weights,1,'smart')
    jugador2=player(weights,2,'q')
   
    j=1
    iter = 0
    while (iter < maxIter):
        os.system('clear')
        for fila in estado_juego.grilla:
            print(fila)
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

    
    #resultados.write("Juego"+str(i)+","+estado_juego.whoWins()+"\n")   

#resultados.close() 
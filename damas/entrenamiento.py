import math
import random
from copy import deepcopy
import os
import time    

from damaschinas import *
from jugador import *

#ENTREMANIEMTO

w0 = 1
w1 = .99
w2 = .09
w3 = .09
alpha = 0.000000001
maxIter = 200

prev_weights = [w0, w1, w2, w3]
weights = [w0, w1, w2, w3]
weights2 = [w0, w1, w2, w3]
history1 = []
history2 = []


resultados_random = open("resultados_random.csv", "w")

partidas = 0
while (partidas < 25) :
    partidas += 1
    fichas = 10
    lado = 4
    if (fichas == 10):
        grilla = [[1,1,1,1,0,0,0,0,0],[1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,2],[0,0,0,0,0,0,0,2,2],[0,0,0,0,0,0,2,2,2],[0,0,0,0,0,2,2,2,2]]
    if (fichas == 6):
        grilla = [[1,1,1,0,0,0],[1,1,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,2],[0,0,0,0,2,2],[0,0,0,2,2,2]]
    if (fichas == 3):
        grilla = [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,2],[0,0,0,2,2]]
    estado_juego = DamasChinasEstado(grilla,lado,fichas,1,[])
    
    jugador1=player(weights2,1,'smart')
    jugador2=player(weights2,2,'random')
    
    history2 = [estado_juego]
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
        history2.append(deepcopy(estado_juego))

        if (estado_juego.whoWins() != "empate..."):
            break

    resultados_random.write("Entrenamiento"+str(partidas)+","+estado_juego.whoWins()+"\n")        

    training_examples = []
    #print(estado_juego.whoWins())
    #time.sleep(1)
    for i in range(2,len(history2)-3):
        if (i % 2 == 0):
            v_op = history2[i-2].evalFunction(1,weights2)
            v_ent = history2[i].evalFunction(1,weights2)
            training_examples.append([v_op, v_ent])


    for t in training_examples:
        for index,w in enumerate(weights2):
            weights2[index] += alpha*(t[1][4]-t[0][4])*t[0][index]
            # print(index)
            # print(vop)
            # print(t[1])
        #print(t[1][4], t[0][4])
    ##    print()
    """   
        print("Pesos:")
        print("w0: ", weights2[0])
        print("w1: ", weights2[1])
        print("w2: ", weights2[2])
        print("w3: ", weights2[3])
    ##    print("Coef: ", t[0])
        print()
    """

resultados_random.close()   
print(weights2)

resultados_prev = open("resultados_prev.csv", "w")

partidas = 0
while (partidas < 25) :
    partidas += 1
    fichas = 10
    lado = 4
    if (fichas == 10):
        grilla = [[1,1,1,1,0,0,0,0,0],[1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,2],[0,0,0,0,0,0,0,2,2],[0,0,0,0,0,0,2,2,2],[0,0,0,0,0,2,2,2,2]]
    if (fichas == 6):
        grilla = [[1,1,1,0,0,0],[1,1,0,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,2],[0,0,0,0,2,2],[0,0,0,2,2,2]]
    if (fichas == 3):
        grilla = [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,2],[0,0,0,2,2]]
    estado_juego = DamasChinasEstado(grilla,lado,fichas,1,[])
    jugador1=player(weights,1,'smart')
    jugador2=player(prev_weights,2,'smart')
    
    history1 = [estado_juego]
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
        history1.append(deepcopy(estado_juego))
        if (estado_juego.whoWins() != "empate..."):
            break

    resultados_prev.write("Entrenamiento"+str(partidas)+","+estado_juego.whoWins()+"\n")        

    training_examples = []
    #print(estado_juego.whoWins())
    #time.sleep(1)
    for i in range(2,len(history1)-3):
        if (i % 2 == 0):
            v_op = history1[i-2].evalFunction(1,weights)
            v_ent = history1[i].evalFunction(1,weights)
            training_examples.append([v_op, v_ent])

    prev_weights = deepcopy(weights)
    
    for t in training_examples:
        for index,w in enumerate(weights):
            weights[index] += alpha*(t[1][4]-t[0][4])*t[0][index]
            # print(index)
            # print(vop)
            # print(t[1])
        #print(t[1][4], t[0][4])
    ##    print()
    """    
        print("Pesos:")
        print("w0: ", weights[0])
        print("w1: ", weights[1])
        print("w2: ", weights[2])
        print("w3: ", weights[3])
        print("Coef: ", t[0])
        print()
    """

resultados_prev.close()   
print(weights)




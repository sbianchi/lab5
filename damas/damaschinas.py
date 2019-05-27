import math
import random
from copy import deepcopy
import os
import time

# Clase DamasChinasEstado que representa al tablero, los posibles movimientos, y la evaluacion de cada tablero

class DamasChinasEstado:  

    def __init__(self,grilla,lado,fichas,jugador,movimientos):
        self.grilla = grilla
        self.lado = lado
        self.fichas = fichas
        self.largo = len(self.grilla)
        self.jugador = jugador
        self.movimientos = movimientos

    def esFinal(self):
        gano1 = 0
        gano2 = 0
        for x in range(0,self.lado):
            for y in range(0,self.lado-x):
                if (self.grilla[x][y]==2):
                    gano2+=1
        for x in range(len(self.grilla)-self.lado,len(self.grilla)):
            for y in range(len(self.grilla)+(self.lado-x),len(self.grilla)):
                if (self.grilla[x][y]==1):
                    gano1+=1

        if (gano1 == self.fichas) or (gano2 == self.fichas):
            return True
        return False
        
    def whoWins(self):
        gano1 = 0
        gano2 = 0
        for x in range(0,self.lado):
            for y in range(0,self.lado-x):
                if (self.grilla[x][y]==2):
                    gano2+=1
        for x in range(len(self.grilla)-self.lado,len(self.grilla)):
            for y in range(len(self.grilla)+(self.lado-x),len(self.grilla)):
                if (self.grilla[x][y]==1):
                    gano1+=1

        if (gano1 == self.fichas):
            return 1
        if (gano2 == self.fichas):
            return 2

        # os.system('clear')
        # for fila in self.grilla:
        #     print(fila)

        #time.sleep(0.0005)
        return 0

    def getSuccessors(self):

        def getSteps(cell):
            Steps1 = [(0, 1), (1, 0), (-1, 1), (1, -1)]   #(-1, 0), (0,-1)
            Steps2 = [(-1, 0), (0, -1), (-1, 1), (1, -1)] # (1, 0), (0, 1)
            steps = []
            if cell != 1: steps.extend(Steps2)
            if cell != 2: steps.extend(Steps1)
            return steps

        def generateMoves(tablero, i, j, successors):
            for step in getSteps(tablero[i][j]):
                x, y = i + step[0], j + step[1]
                if x >= 0 and x < self.largo and y >= 0 and y < self.largo and tablero[x][y] == 0:
                    boardCopy = deepcopy(tablero)
                    boardCopy[x][y], boardCopy[i][j] = boardCopy[i][j], 0
                    successors.append(DamasChinasEstado(boardCopy,self.lado,self.fichas, int(not self.jugador), [(i, j), (x, y)]))

        def generateJumps(tablero,i, j, moves, successors,anteriores):
            jumpEnd = True
            anteriores.append((i,j))
            for step in getSteps(tablero[i][j]):
                x, y = i + step[0], j + step[1]
                if x >= 0 and x < self.largo and y >= 0 and y < self.largo and tablero[x][y] != 0:
                    xp, yp = x + step[0], y + step[1]
                    if  ((xp,yp) not in anteriores) and xp >= 0 and xp < self.largo and yp >= 0 and yp < self.largo and tablero[xp][yp] == 0:
                        tablero[xp][yp], save = tablero[i][j], tablero[x][y]
                        tablero[i][j] = 0
                        previous = tablero[xp][yp]
                        moves.append((xp, yp))
                        generateJumps(tablero, xp, yp, moves, successors,anteriores)
                        moves.pop()
                        tablero[i][j], tablero[x][y], tablero[xp][yp] = previous, save, 0
                        jumpEnd = False
            if jumpEnd and len(moves) > 1:
                    successors.append(DamasChinasEstado(deepcopy(tablero),self.lado,self.fichas, int(not self.jugador), deepcopy(moves)))

        player = 1 if self.jugador == 1 else 2
        successors = []

    # generate jumps
        for i in range(self.largo):
            for j in range(self.largo):
                if self.grilla[i][j] == player:
                    generateJumps(self.grilla,i, j, [(i, j)], successors,[])


    # generate moves
        for i in range(self.largo):
            for j in range(self.largo):
                if self.grilla[i][j] == player:
                    generateMoves(self.grilla, i, j, successors)
        return successors


    def qFunction(self,jugador,weights):

            def rsa(self,successors):
                winner = self.whoWins()
                if (jugador.jugador == winner):
                    return 1
                else if (winner == 0):
                    return 0
                else return -1 

            def maxQ(self,successors):
                winner = self.whoWins()
                if (jugador.jugador == winner):
                    return 1
                else if (winner == 0):
                    return 0
                else return -1     
                             

    def evalFunction(self,jugador,weights):

        def distanciaAZona(i, j, jugador):
            if (jugador == 1):
                res = (self.largo-i-1)+(self.largo-j-1)#(self.lado-1)
                if (res < 0):
                    return 0
                else:
                    return res
            if (jugador == 2):
                res = i+j#(self.lado-1)
                if (res < 0):
                    return 0
                else:
                    return res


        def distanciaAVertical(i,j):
            if (i==j):
                return 0
            if (abs(i-j) == 1):
                return 1
            if (abs(i-j) > 1):
                if (i>j):
                    return distanciaAVertical(i-1,j+1)+1
                else:
                    return distanciaAVertical(i+1,j-1)+1

        def maxAvanceFicha(i,j):
            def getSteps(cell):
                Steps1 = [(0, 1), (1, 0), (-1, 1), (1, -1)]   #(-1, 0), (0,-1)
                Steps2 = [(-1, 0), (0, -1), (-1, 1), (1, -1)] # (1, 0), (0, 1)
                steps = []
                if cell != 1: steps.extend(Steps2)
                if cell != 2: steps.extend(Steps1)
                return steps

            def maxAvanceMoves(tablero, i, j):
                for step in getSteps(tablero[i][j]):
                    if abs(step[0]-step[1])==1:
                        x, y = i + step[0], j + step[1]
                        if x >= 0 and x < self.largo and y >= 0 and y < self.largo and tablero[x][y] == 0:
                            return 1
                return 0

            def maxAvanceJumps(tablero,i, j, anteriores):
                jumpEnd = True
                anteriores.append((i,j))
                avanceMax = 0
                for step in getSteps(tablero[i][j]):
                    x, y = i + step[0], j + step[1]
                    if x >= 0 and x < self.largo and y >= 0 and y < self.largo and tablero[x][y] != 0:
                        xp, yp = x + step[0], y + step[1]
                        if  ((xp,yp) not in anteriores) and xp >= 0 and xp < self.largo and yp >= 0 and yp < self.largo and tablero[xp][yp] == 0:
                            avanceStep = 0 if abs(step[0]-step[1])==0 else 2
                            tablero[xp][yp], save = tablero[i][j], tablero[x][y]
                            tablero[i][j] = 0
                            previous = tablero[xp][yp]
                            avance = avanceStep + maxAvanceJumps(tablero, xp, yp,anteriores)
                            if avance > avanceMax:
                                avanceMax = avance
                            tablero[i][j], tablero[x][y], tablero[xp][yp] = previous, save, 0
                            jumpEnd = False
                return avanceMax

            maxAvance = 0
            maxAvance = maxAvanceJumps(deepcopy(self.grilla),i,j,[])
            #if maxAvance > 0:
             #   print(str(i)+'-'+str(j)+'-'+str(maxAvance))

            if maxAvance < 2:
               maxAvance = maxAvanceMoves(deepcopy(self.grilla),i,j)

            return maxAvance


        A1,A2,B1,B2,C1,C2 = 0,0,0,0,0,0
        score = 0
        if self.esFinal():
            score = 2000
            result = [1,A2-A1,B2-B1,C1-C2,score]
            return result
        for i in range(self.largo):
            for j in range(self.largo):
                if self.grilla[i][j] == 1:
                    A1 += distanciaAZona(i, j, 1)
                    B1 += distanciaAVertical(i,j)
                    C1 += maxAvanceFicha(i,j)
                if self.grilla[i][j] == 2:
                    nextA2 = i+j-(self.lado-1)
                    A2 += distanciaAZona(i, j, 2)
                    B2 += distanciaAVertical(i,j)
                    C2 += maxAvanceFicha(i,j)

        A1 = math.pow(A1,2)
        A2 = math.pow(A2,2)
        B1 = math.pow(B1,2)
        B2 = math.pow(B2,2)
        #print(A1,A2)
        #print(B1,B2)
        #print(C1,C2)
        #print()
        if jugador == 1:
            score += weights[0] + weights[1]*(A2 - A1) + weights[2]*(B2 - B1) + weights[3]*(C1-C2)
            result = [1,A2-A1,B2-B1,C1-C2,score]
        if jugador == 2:
            score += weights[0] + weights[1]*(A1 - A2) + weights[2]*(B1 - B2) + weights[3]*(C2 - C1)
            result = [1,A1-A2,B1-B2,C2-C1,score]
    
        return result
from turtle import width
import numpy as np
import pygame
import time

pygame.init()

width, height = 1000, 1000 #ancho y alto de la interfaz
screen = pygame.display.set_mode((height, width)) #comando para crear la pantalla

bg= 25, 25, 25 #color de fondo, oscuro
screen.fill(bg) # rellena la pantalla con el color elegido 


nxC, nyC = 25, 25   #nxc= la cordenada x de la celda  nyC coordenada y de la celda 
dimCW = width / nxC  #DimcW = dimension cell width ancho 
dimCH = height/ nyC  # dimCH = dimension cell height alto

gameState= np.zeros((nxC, nyC)) #estado de las celdas vivas 1 muertas 0
gameState[5, 3]=1
gameState[5, 4]=1
gameState[5, 5]=1


gameState[21, 21]=1
gameState[22, 22]=1
gameState[22, 23]=1
gameState[21, 23]=1
gameState[20, 23]=1


pauseExect=False


while True: # loop de ejecucion 

    newGameState= np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.1)


    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect= not pauseExect

        mouseClick= pygame.mouse.get_pressed()
        
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int (np.floor(posX / dimCW)), int (np.floor(posY / dimCH))
            newGameState [celX, celY] = not mouseClick[2]



    for y in range (0, nxC):
        for x in range (0, nyC):

            if not pauseExect:
 


                n_neigh = gameState [(x-1) % nxC,(y-1) % nyC] + \
                        gameState [(x)   % nxC,(y-1) % nyC] + \
                        gameState [(x+1) % nxC,(y-1) % nyC] + \
                        gameState [(x-1) % nxC,(y)   % nyC] + \
                        gameState [(x+1) % nxC,(y)   % nyC] + \
                        gameState [(x-1) % nxC,(y+1) % nyC] + \
                        gameState [(x)   % nxC,(y+1) % nyC] + \
                        gameState [(x+1) % nxC,(y+1) % nyC]  
        #1 condicion 
                if gameState[x, y]==0 and n_neigh==3:
                    newGameState[x, y]=1
        #2 condicion 
                elif gameState [x, y] ==1 and (n_neigh <2 or n_neigh>3):
                    newGameState[x, y]=0


            poly =[((x) * dimCW, y     * dimCH),
                  ((x+1)* dimCW, y     * dimCH),
                  ((x+1)* dimCW, (y+1) * dimCH),
                  ((x)  * dimCW, (y+1) * dimCH),]



            if newGameState[x, y] == 0:

                pygame.draw.polygon(screen, (128, 128, 128), poly,1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly,0)
   
    gameState= np.copy(newGameState)
   
    pygame.display.flip()


    

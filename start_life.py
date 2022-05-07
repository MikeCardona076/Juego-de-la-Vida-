import pygame
import numpy as np
import time
import random






class DiosMike(object):

    def __init__(self, width, height, bg_color):

        pygame.init()

        self.width = width
        self.height = height
        self.bg = bg_color
        # bg = 25, 25 ,25

        
        
        self.screen  = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Mike Cardona, Juego de la vida")
        self.screen.fill(self.bg)

        # Tamaño de nuestra matriz
        self.nxC = 90
        self.nyC = 90

        self.gameState = np.zeros((self.nxC, self.nyC))
        
        #dimensiones de cada celda individual
        self.dimCW = self.width / self.nxC
        self.dimCH = self.height / self.nyC
        
    def getGameState(self):
        
        for x in range(random.randint(10, 90)):
            self.gameState[random.randint(0, self.nxC - 1), random.randint(0, self.nyC - 1)] = 1
            print("Celda: ", x, " creada")

        return self.gameState


    def create_life(self):

        pauseExect = False

        # Bucle de ejecución
        while True:

            # Copiamos la matriz del estado anterior
            # #para representar la matriz en el nuevo estado
            newGameState = np.copy(self.getGameState())

            # Ralentizamos la ejecución a 0.1 segundos
            time.sleep(0.1)

            # Limpiamos la pantalla
            self.screen.fill(self.bg)

            # Registramos eventos de teclado y ratón.
            ev = pygame.event.get()

            # Cada vez que identificamos un evento lo procesamos
            for event in ev:
                # Detectamos si se presiona una tecla.
                if event.type == pygame.KEYDOWN:
                    pauseExect = not pauseExect

                # Detectamos si se presiona el ratón.
                mouseClick = pygame.mouse.get_pressed()

                if sum(mouseClick) > 0:
                    posX, posY = pygame.mouse.get_pos()
                    celX, celY = int(np.floor(posX / self.dimCW)), int(np.floor(posY / self.dimCH))
                    newGameState[celX, celY] = 1

            for y in range(0, self.nxC):
                for x in range (0, self.nyC):

                    if not pauseExect:

                        # Calculamos el número de vecinos cercanos.
                        n_neigh =   self.gameState[(x - 1) % self.nxC, (y - 1)  % self.nyC] + \
                                    self.gameState[(x)     % self.nxC, (y - 1)  % self.nyC] + \
                                    self.gameState[(x + 1) % self.nxC, (y - 1)  % self.nyC] + \
                                    self.gameState[(x - 1) % self.nxC, (y)      % self.nyC] + \
                                    self.gameState[(x + 1) % self.nxC, (y)      % self.nyC] + \
                                    self.gameState[(x - 1) % self.nxC, (y + 1)  % self.nyC] + \
                                    self.gameState[(x)     % self.nxC, (y + 1)  % self.nyC] + \
                                    self.gameState[(x + 1) % self.nxC, (y + 1)  % self.nyC]

                        # Regla #1 : Una celda muerta con exactamente 3 vecinas vivas, "revive".

                        if self.gameState[x, y] == 0 and n_neigh == 3:
                            newGameState[x, y] = 1

                        # Regla #2 : Una celda viva con menos de 2 o más 3 vecinas vinas, "muere".

                        elif self.gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                            newGameState[x, y] = 0

                    # Calculamos el polígono que forma la celda.
                    poly = [((x)   * self.dimCW, y * self.dimCH),
                            ((x+1) * self.dimCW, y * self.dimCH),
                            ((x+1) * self.dimCW, (y+1) * self.dimCH),
                            ((x)   * self.dimCW, (y+1) * self.dimCH)]

                    # Si la celda está "muerta" pintamos un recuadro con borde gris
                    if newGameState[x, y] == 0:
                        pygame.draw.polygon(self.screen, (40, 40, 40), poly, 1)
                # Si la celda está "viva" pintamos un recuadro relleno de color
                    else:
                        pygame.draw.polygon(self.screen, (200, 100, 100), poly, 0)

  

            # Mostramos el resultado
            pygame.display.flip()




if __name__ == "__main__":
    game = DiosMike(800, 800, (25, 25, 25))
    game.create_life()


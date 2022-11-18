import pygame
from Pieza import Pieza
BROWN = (200, 100, 0)
WHITE = (255, 255, 255)
 
class Peon (Pieza):
    def __init__(self, size, row, column, color):
        # Call the parent class (Sprite) constructor
        super().__init__(size, row, column, color)

        self.first_move = True

        if color == 0:
            pieza = pygame.image.load('img/peon_negro.png').convert_alpha()
        else:
            pieza = pygame.image.load('img/peon_blanco.png').convert_alpha()
        pieza = pygame.transform.scale(pieza, (size,size))
        self.image = pieza
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect() 
    
    def valid_move(self, casilla):
        if self.color == 0:
            if casilla.row == self.row + 1:
                if casilla.column == self.column and casilla.pieza == None:
                    return True
                elif (casilla.column == self.column + 1) or (casilla.column == self.column - 1):
                    if casilla.pieza != None:
                        return True
            if self.first_move:
                if (casilla.row == self.row + 2):
                    if casilla.column == self.column and casilla.pieza == None:
                        return True
        if self.color == 1:
            if casilla.row == self.row - 1:
                if casilla.column == self.column and casilla.pieza == None:
                    return True
                elif (casilla.column == self.column + 1) or (casilla.column == self.column - 1):
                    if casilla.pieza != None:
                        return True
            if self.first_move:
                if (casilla.row == self.row - 2):
                    if casilla.column == self.column and casilla.pieza == None:
                        return True
        print('Casilla no valida')
        return False
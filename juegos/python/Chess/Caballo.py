import pygame
from Pieza import Pieza
BROWN = (200, 100, 0)
WHITE = (255, 255, 255)
 
class Caballo (Pieza):
    def __init__(self, size, row, column, color):
        # Call the parent class (Sprite) constructor
        super().__init__(size, row, column, color)

        if color == 0:
            pieza = pygame.image.load('img/caballo_negro.png').convert_alpha()
        else:
            pieza = pygame.image.load('img/caballo_blanco.png').convert_alpha()
        pieza = pygame.transform.scale(pieza, (size,size))
        self.image = pieza
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect() 
    
    def valid_move(self, casilla):
        if (casilla.row == self.row + 2) or (casilla.row == self.row - 2):
            if (casilla.column == self.column +1) or (casilla.column == self.column -1):
                return True
        if (casilla.column == self.column + 2) or (casilla.column == self.column - 2):
            if (casilla.row == self.row +1) or (casilla.row == self.row -1):
                return True
        else:
            return False
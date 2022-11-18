import pygame
from Pieza import Pieza
BROWN = (200, 100, 0)
WHITE = (255, 255, 255)
 
class Reina (Pieza):
    def __init__(self, size, row, column, color):
        # Call the parent class (Sprite) constructor
        super().__init__(size, row, column, color)

        if color == 0:
            pieza = pygame.image.load('img/reina_negro.png').convert_alpha()
        else:
            pieza = pygame.image.load('img/reina_blanco.png').convert_alpha()
        pieza = pygame.transform.scale(pieza, (size,size))
        self.image = pieza
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect() 
    
    def valid_move(self, casilla):
        if ((casilla.row - self.row) == (casilla.column - self.column)):
            return True
        if ((self.row - casilla.row) == (casilla.column - self.column)):
            return True
        if self.row == casilla.row:
            if self.column != casilla.column:
                return True
        elif self.column == casilla.column:
            if self.row != casilla.row:
                return True
        return False
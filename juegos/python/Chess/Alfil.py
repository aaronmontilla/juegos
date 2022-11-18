import pygame
from Pieza import Pieza
BROWN = (200, 100, 0)
WHITE = (255, 255, 255)
 
class Alfil (Pieza):
    def __init__(self, size, row, column, color):
        # Call the parent class (Sprite) constructor
        super().__init__(size, row, column, color)

        if color == 0:
            pieza = pygame.image.load('img/alfil_negro.png').convert_alpha()
        else:
            pieza = pygame.image.load('img/alfil_blanco.png').convert_alpha()
        pieza = pygame.transform.scale(pieza, (size,size))
        self.image = pieza
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect() 
    
    def valid_move(self, casilla):
        if ((casilla.row - self.row) == (casilla.column - self.column)):
            return True
        if ((self.row - casilla.row) == (casilla.column - self.column)):
            return True
        else:
            return False
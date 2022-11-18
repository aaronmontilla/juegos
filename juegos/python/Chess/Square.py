import pygame
from Pieza import Pieza
BROWN = (200, 100, 0)
WHITE = (220, 160, 40)
RED = (255, 0, 0)
GREEN = (20, 255, 140)
SCREENWIDTH=800
SCREENHEIGHT=600
 
class Square (pygame.sprite.Sprite):
    def __init__(self, size, row, column):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.image = pygame.Surface([size, size])

        #Initialise attributes of the car.
        self.width = size
        self.height = size
        self.row = row
        self.column = column
        self.selected = 0
        self.pieza = None

        if (row + column)%2 == 0:
            self.color = WHITE
        else:
            self.color = BROWN
        
        self.posx = ((column-1) * 50) + (SCREENWIDTH/2 - 200)
        self.posy = (row-1)*50 + (SCREENHEIGHT/2 - 200)

        pygame.draw.rect(self.image, self.color, [0, 0, size, size])
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect() 
        self.rect.x = self.posx
        self.rect.y = self.posy

    def is_pressed(self, escoge_pieza, selected):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed:
            if (mouse_pos[0] > self.rect.x and mouse_pos[0] < (self.rect.x + self.width)) and (mouse_pos[1] > self.rect.y and mouse_pos[1] < (self.rect.y + self.height)):
                if self.pieza != None and escoge_pieza:
                    print(f'Pieza en {self.row}{self.column} seleccionada')
                    return True
                elif self.pieza == None and escoge_pieza:
                    print('No contiene ninguna pieza, escoge otra')
                    return False
                elif not escoge_pieza and self.pieza == None:
                    return True
                elif not escoge_pieza and self.pieza != None:
                    if selected.pieza.color == self.pieza:
                        print('Esta casilla ya contiene una pieza')
                        return False
                    else:
                        return True

    def contiene_pieza(self, pieza):
        if self.row == pieza.row and self.column == pieza.column:
            self.pieza = pieza
    
    def check_color(self, validas):
        if self.selected == 1:
            pygame.draw.rect(self.image, RED, [0, 0, self.width, self.height])
        elif self in validas:
            pygame.draw.rect(self.image, GREEN, [0, 0, self.width, self.height])
        else:
            pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        self.rect = self.image.get_rect() 
        self.rect.x = self.posx
        self.rect.y = self.posy



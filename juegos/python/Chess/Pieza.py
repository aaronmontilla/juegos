import pygame
BROWN = (200, 100, 0)
WHITE = (255, 255, 255)
 
class Pieza (pygame.sprite.Sprite):
    def __init__(self, size, row, column, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.image = pygame.Surface([size, size])

        #Initialise attributes of the car.
        self.width = size
        self.height = size
        self.row = row
        self.column = column
        self.selected = False
        self.color = color

    def check_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed:
            if (mouse_pos[0] > self.rect.x and mouse_pos[0] < (self.rect.x + self.width)) and (mouse_pos[1] > self.rect.y and mouse_pos[1] < (self.rect.y + self.height)):
                if self.selected == False:
                    self.selected = True
                    print(f'Pieza in {self.row} {self.column} selected')
                    return True
                else:
                    self.selected = False
                    return False

    def move(self, casilla):
        self.row = casilla.row
        self.column = casilla.column
        self.rect.x = casilla.rect.x
        self.rect.y = casilla.rect.y
        self.selected = False

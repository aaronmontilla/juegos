import pygame
WHITE = (255, 255, 255)
 
class Player(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])

        #Initialise attributes of the car.
        self.width=width
        self.height=height
        self.CollitionCount = 0
        self.pos = 0
        self.roads_complete = 0

        picture = pygame.image.load("frog.png").convert_alpha()
        picture = pygame.transform.scale(picture, (width,height))
        self.image = picture.convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect() 

    def decrease_pos(self):
        if self.pos==0:
            return
        self.pos -= 1

    def increase_pos(self):
        if self.pos == 5:
            self.pos = 0
            self.roads_complete += 1
            return self.pos
        self.pos += 1
        return self.pos
    
    def updatepos(self, initial):
        self.rect.x = self.pos * 100 + initial


from curses import KEY_MAX
import pygame, random, math, time
from car import Car
from Player import Player
from wood import Wood
pygame.init()

def checkCollisions(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
        return (a_x + a_width > b_x) and (a_x < b_x + b_width) and (a_y + a_height > b_y) and (a_y < b_y + b_height)

    

font_small = pygame.font.Font('font.otf', 32)
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BROWN = (200, 100, 0)
        
speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE, BROWN)
 
 
SCREENWIDTH=800
SCREENHEIGHT=600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Crossy road")
a = pygame.image.load('frog.png')
retry_button = pygame.image.load('retry_button.png')
game_over = pygame.image.load('game-over.png')
logo = pygame.image.load('logo.png')
pygame.display.set_icon(a)

flapfx = pygame.mixer.Sound("flap.wav")
game_overfx = pygame.mixer.Sound("game-over.wav")
 


while True:
        #This will be a list that will contain all the sprites we intend to use in our game.
        all_sprites_list = pygame.sprite.Group()
        player = Player(60, 80)
        initialx = SCREENWIDTH/4 - 75
        player.rect.x = SCREENWIDTH/4 - 25
        player.rect.y = SCREENHEIGHT/2
        
        car1 = Car(PURPLE, 60, 80, random.randint(50,100))
        car1.rect.x = initialx + 100
        car1.rect.y = -100
        
        car2 = Car(YELLOW, 60, 80, random.randint(50,100))
        car2.rect.x = initialx + 200
        car2.rect.y = -600
        
        car3 = Car(CYAN, 60, 80, random.randint(50,100))
        car3.rect.x = initialx + 300
        car3.rect.y = -300
 
        car4 = Car(BLUE, 60, 80, random.randint(50,100))
        car4.rect.x = initialx + 400
        car4.rect.y = -900

        wood = Wood(60, 80, random.randint(50,100))
        wood.rect.x = initialx + 500
        wood.rect.y = -300
        
        
        # Add the car to the list of objects

        all_sprites_list.add(car1)
        all_sprites_list.add(car2)
        all_sprites_list.add(car3)
        all_sprites_list.add(car4)
        all_sprites_list.add(wood)
        all_sprites_list.add(player)
        
        all_coming_cars = pygame.sprite.Group()
        all_coming_cars.add(car1)
        all_coming_cars.add(car2)
        all_coming_cars.add(car3)
        all_coming_cars.add(car4)
        go = 0
        ts = 0
        #Allowing the user to close the window...
        carryOn = True
        clock=pygame.time.Clock()
        titleScreen = True
        # title screen
        pygame.mixer.Sound.play(flapfx)
        while titleScreen:
                # get the position of the mouse
                mouseX,mouseY = pygame.mouse.get_pos()  
                # getting the keys pressed
                clicked = False
                keys = pygame.key.get_pressed()
                # checking events
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                clicked = True
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                                pygame.quit()
                # if the player quits
                if event.type==pygame.QUIT:
                        pygame.quit()
                # so the user clicked, and by any change the mouse's position was on the buttons
                if (clicked and checkCollisions(mouseX, mouseY, 3, 3, screen.get_width()/2 - retry_button.get_width()/2, 500, retry_button.get_width(), retry_button.get_height())):
                        clicked = False
                        titleScreen = False
                #Drawing on Screen
                screen.fill(GREEN)
                #Draw The Road
                pygame.draw.rect(screen, GREY, [SCREENWIDTH/4,0, 400,SCREENHEIGHT])
                #Draw Line painting on the road
                pygame.draw.line(screen, WHITE, [(SCREENWIDTH/4)+100,0],[(SCREENWIDTH/4)+100,SCREENHEIGHT],5)
                #Draw Line painting on the road
                pygame.draw.line(screen, WHITE, [(SCREENWIDTH/4)+200,0],[(SCREENWIDTH/4)+200,SCREENHEIGHT],5)
                #Draw Line painting on the road
                pygame.draw.line(screen, WHITE, [(SCREENWIDTH/4)+300,0],[(SCREENWIDTH/4)+300,SCREENHEIGHT],5)
                screen.blit(logo, (screen.get_width()/2 - logo.get_width()/2, screen.get_height()/2 - logo.get_height()/2 + math.sin(time.time()*5)*5 - 25)) 
                screen.blit(retry_button, (screen.get_width()/2 - retry_button.get_width()/2, 500))
                startMessage = font_small.render("START", True, (0, 0, 0))
                screen.blit(startMessage, (screen.get_width()/2 - startMessage.get_width()/2, 500))

                pygame.display.update()
                pygame.time.delay(10)
        while carryOn:
                
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                carryOn=False
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                        while True: #Infinite loop that will be broken when the user press the space bar again
                                                font = pygame.font.Font("font.otf", 100)
                                                PauseDisplay = font.render("PAUSED", True, (0,0,0))
                                                screen.blit(PauseDisplay, (270,200))
                                                pygame.display.flip()
                                                event = pygame.event.wait()
                                                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                                        break #Exit infinite loop
                                                if (event.type == pygame.KEYDOWN and event.key == pygame.K_x) or event.type==pygame.QUIT:
                                                        pygame.quit() #Exit infinite loop
                                elif event.key==pygame.K_x:
                                        carryOn=False
                                elif event.key==pygame.K_RIGHT:
                                        player.increase_pos()
                                elif event.key==pygame.K_LEFT:
                                        player.decrease_pos()
                                        if player.pos == 5:
                                                player.rect.y = wood.rect.y
                                                
                
                player.updatepos(initialx)
                        
                #Game Logic
                for car in all_coming_cars:
                        if (checkCollisions(player.rect.x, player.rect.y, player.width, player.height, car.rect.x, car.rect.y, car.width, car.height)):
                                go = 1
                        car.moveForward(speed)
                        if car.rect.y > SCREENHEIGHT:
                                car.changeSpeed(random.randint(50,100))
                                car.rect.y = -200
                wood.moveForward(speed)
                if wood.rect.y > SCREENHEIGHT:
                                wood.changeSpeed(random.randint(50,100))
                                wood.rect.y = -200
                if player.pos == 5:
                        if checkCollisions(player.rect.x, player.rect.y, player.width, player.height, wood.rect.x, wood.rect.y, wood.width, wood.height):   
                                player.rect.x = wood.rect.x
                                player.rect.y = wood.rect.y
                        else:
                                go = 1
                if player.rect.y > SCREENHEIGHT:
                                go = 1
                if go == 1:
                        break

                
                all_sprites_list.update()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        while True: #Infinite loop that will be broken when the user press the space bar again
                                event = pygame.event.wait()
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                        break #Exit infinite loop
        
                #Drawing on Screen
                screen.fill(GREEN)
                #Draw The Road
                pygame.draw.rect(screen, GREY, [SCREENWIDTH/4,0, 400,SCREENHEIGHT])
                #Draw Line painting on the road
                pygame.draw.line(screen, WHITE, [(SCREENWIDTH/4)+100,0],[(SCREENWIDTH/4)+100,SCREENHEIGHT],5)
                #Draw Line painting on the road
                pygame.draw.line(screen, WHITE, [(SCREENWIDTH/4)+200,0],[(SCREENWIDTH/4)+200,SCREENHEIGHT],5)
                #Draw Line painting on the road
                pygame.draw.line(screen, WHITE, [(SCREENWIDTH/4)+300,0],[(SCREENWIDTH/4)+300,SCREENHEIGHT],5)
                pygame.draw.rect(screen, BLUE, [(SCREENWIDTH/4)+400,0, 100,SCREENHEIGHT])
                RoadsComDisplay = font_small.render("Completed roads: " + str(player.roads_complete).zfill(3), True, (0,0,0))
                screen.blit(RoadsComDisplay, (500, 40))
                #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
                all_sprites_list.draw(screen)
        
                #Refresh Screen
                pygame.display.flip()
        
                #Number of frames per secong e.g. 60
                clock.tick(60)
        if go == 1:
                screen.blit(game_over, (screen.get_width()/2 - game_over.get_width()/2, screen.get_height()/2 - game_over.get_height()/2 + math.sin(time.time()*5)*5 - 25)) 
                pygame.display.flip()
                pygame.mixer.Sound.play(game_overfx)
                pygame.time.delay(3000)
                ts = 1
        
pygame.quit()


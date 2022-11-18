from curses import KEY_MAX
import pygame, random, math, time
from Square import Square
from Pieza import Pieza
from Torre import Torre
from Caballo import Caballo
from Alfil import Alfil
from Reina import Reina
from Rey import Rey
from Peon import Peon
import inspect
pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BROWN = (92,51,23)
OUTSIDE = (50,50,10)
BLACK = (10, 10, 10)
        
speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE, BROWN)
font_small = pygame.font.Font('font.otf', 32)
 
SCREENWIDTH=800
SCREENHEIGHT=600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess")

def matar_pieza(casilla,selected):
        if isinstance(casilla.pieza,Rey):
                if casilla.pieza.color == 0:
                        print('Blancos ganan')
                else:
                        print('Negros ganan')
        casilla.pieza.kill()
        casilla.pieza = selected.pieza
        


def check_obstacles(casilla,selected):
        fn = 0
        cn = 0
        filas = casilla.row - selected.row
        if filas < 0:
                fn = 1
                filas = 0 - filas
        columnas = casilla.column - selected.column
        if columnas < 0: 
                cn = 1
                columnas = 0 - columnas
        if filas == 0:
                for pasos_h in range(1,columnas):
                        for c in tablero:
                                if cn:
                                        if c.row == selected.row and c.column == selected.column - (pasos_h):
                                                if c.pieza != None and c.pieza.color == selected.pieza.color:

                                                        print('No puedes saltar fichas {c.row}{c.column}')
                                                        return False
                                else:
                                        if c.row == selected.row and c.column == selected.column + pasos_h+1:
                                                if c.pieza != None and c.pieza.color == selected.pieza.color:
                                                        print('No puedes saltar fichas')
                                                        return False
                return True
        elif columnas == 0:
                for pasos_v in range(filas):
                        for c in tablero:
                                if fn:
                                        if c.column == selected.column and c.row == selected.row - (pasos_v+1):
                                                if c.pieza != None and c.pieza.color == selected.pieza.color:
                                                        print(f'No puedes saltar fichas {c.row}{c.column}')
                                                        return False
                                else:
                                        if c.column == selected.column and c.row == selected.row + pasos_v+1:
                                                if c.pieza != None and c.pieza.color == selected.pieza.color:
                                                        print('No puedes saltar fichas')
                                                        return False
                return True
        elif columnas == filas:
                for pasos_d in range(filas):
                        for c in tablero:
                                if fn and cn:
                                        if c.column == selected.column - (pasos_d+1) and c.row == selected.row - (pasos_d+1):
                                                if c.pieza != None and c.pieza.color == selected.pieza.color:
                                                        print('No puedes saltar fichas ')
                                                        return False
                                elif fn and not cn:
                                        if c.column == selected.column + (pasos_d+1) and c.row == selected.row - (pasos_d+1):
                                                if c.pieza != None and c.pieza.color == selected.pieza.color:
                                                        print('No puedes saltar fichas ')
                                                        return False
                                elif not fn and cn:
                                        if c.column == selected.column - (pasos_d+1) and c.row == selected.row + (pasos_d+1):
                                                if c.pieza != None and c.pieza.color == selected.pieza.color:
                                                        print('No puedes saltar fichas ')
                                                        return False
                                elif not fn and not cn:
                                        if c.column == selected.column + (pasos_d+1) and c.row == selected.row + (pasos_d+1):
                                                if c.pieza != None and c.pieza.color == selected.pieza.color:
                                                        print('No puedes saltar fichas ')
                                                        return False
                return True
        else:
                return True


 

def añadir_piezas_negras(piezas):
        #peones negros
        for y in range(8):
                if y == 0 or y == 7:
                        torre = Torre(50, 1, y+1, 0)
                        torre.rect.x = (y * 50) + (SCREENWIDTH/2 - 200)
                        torre.rect.y = (SCREENHEIGHT/2 - 200)
                        piezas.add(torre)
                if y == 1 or y == 6:
                        caballo = Caballo(50, 1, y+1, 0)
                        caballo.rect.x = (y * 50) + (SCREENWIDTH/2 - 200)
                        caballo.rect.y = (SCREENHEIGHT/2 - 200)
                        piezas.add(caballo)
                if y == 2 or y == 5:
                        alfil = Alfil(50, 1, y+1, 0)
                        alfil.rect.x = (y * 50) + (SCREENWIDTH/2 - 200)
                        alfil.rect.y = (SCREENHEIGHT/2 - 200)
                        piezas.add(alfil)
                if y == 3:
                        rey = Rey(50, 1, y+1, 0)
                        rey.rect.x = (y * 50) + (SCREENWIDTH/2 - 200)
                        rey.rect.y = (SCREENHEIGHT/2 - 200)
                        piezas.add(rey)
                if y == 4:
                        reina = Reina(50, 1, y+1, 0)
                        reina.rect.x = (y * 50) + (SCREENWIDTH/2 - 200)
                        reina.rect.y = (SCREENHEIGHT/2 - 200)
                        piezas.add(reina)
                
        for x in range(8):
                peon = Peon(50, 2, x+1, 0)
                peon.rect.x = (x * 50) + (SCREENWIDTH/2 - 200)
                peon.rect.y = 1*50 + (SCREENHEIGHT/2 - 200)
                piezas.add(peon)   

def añadir_piezas_blancas(piezas):
        for y in range(8):
                if y == 0 or y == 7:
                        torre = Torre(50, 8, y+1, 1)
                        torre.rect.x = (y * 50) + (SCREENWIDTH/2 - 200)
                        torre.rect.y = (7*50) + (SCREENHEIGHT/2 - 200)
                        piezas.add(torre)
                if y == 1 or y == 6:
                        caballo = Caballo(50, 8, y+1, 1)
                        caballo.rect.x = (y * 50) + (SCREENWIDTH/2 - 200)
                        caballo.rect.y = (7*50) + (SCREENHEIGHT/2 - 200)
                        piezas.add(caballo)
                if y == 2 or y == 5:
                        alfil = Alfil(50, 8, y+1, 1)
                        alfil.rect.x = (y * 50) + (SCREENWIDTH/2 - 200)
                        alfil.rect.y = (7*50) + (SCREENHEIGHT/2 - 200)
                        piezas.add(alfil)
                if y == 3:
                        rey = Rey(50, 8, y+1, 1)
                        rey.rect.x = (y * 50) + (SCREENWIDTH/2 - 200)
                        rey.rect.y = (7*50) + (SCREENHEIGHT/2 - 200)
                        piezas.add(rey)
                if y == 4:
                        reina = Reina(50, 8, y+1, 1)
                        reina.rect.x = (y * 50) + (SCREENWIDTH/2 - 200)
                        reina.rect.y = (7*50) + (SCREENHEIGHT/2 - 200)
                        piezas.add(reina)
                
        for x in range(8):
                peon = Peon(50, 7, x+1, 1)
                peon.rect.x = (x * 50) + (SCREENWIDTH/2 - 200)
                peon.rect.y = 6*50 + (SCREENHEIGHT/2 - 200)
                piezas.add(peon)             
                

background = pygame.image.load("img/background.jpg").convert()

tablero = pygame.sprite.Group()
validas = pygame.sprite.Group()
piezas = pygame.sprite.Group()
clock=pygame.time.Clock()

logo = pygame.image.load('img/logo.png')
pygame.display.set_icon(logo)




screen.blit(background, [0,0], (400, 100, SCREENWIDTH, SCREENHEIGHT))
pygame.draw.rect(screen, OUTSIDE , [SCREENWIDTH/2 - 220, SCREENHEIGHT/2 - 220, 440, 440] )
for row in range(8):
        for col in range (8):
                sq = Square(50, row+1, col+1) #Empieza en 0
                tablero.add(sq)
añadir_piezas_negras(piezas)
añadir_piezas_blancas(piezas)

selected = None
carryOn = True
escoge_pieza = True
turno = 1
while carryOn:
        
        tablero.draw(screen)
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        carryOn=False
                if event.type == pygame.MOUSEBUTTONUP:
                        if escoge_pieza:
                                for casilla in tablero:
                                        if casilla.is_pressed(escoge_pieza, None):
                                                if casilla.pieza.color != turno:
                                                        print('No es tu turno')
                                                else:        
                                                        selected = casilla
                                                        casilla.selected = 1
                                                        escoge_pieza = False
                                if selected:
                                        for casilla in tablero:
                                                if selected.pieza.valid_move(casilla):
                                                        if check_obstacles(casilla, selected):
                                                                if casilla.pieza == None or casilla.pieza.color != selected.pieza.color:
                                                                        validas.add(casilla)

                        else:
                                for casilla in tablero:
                                        if casilla.is_pressed(escoge_pieza, selected):
                                                if casilla == selected:
                                                        selected.selected = 0
                                                        selected = None
                                                        escoge_pieza = True
                                                        validas.empty()
                                                else:
                                                        if casilla in validas:
                                                                        if casilla.pieza != None:
                                                                                matar_pieza(casilla, selected)
                                                                        if isinstance(selected.pieza,Peon):
                                                                                selected.pieza.first_move = False
                                                                        selected.selected = 0
                                                                        selected.pieza.move(casilla)
                                                                        selected.pieza = None
                                                                        selected = None
                                                                        escoge_pieza = True
                                                                        turno = not turno 
                                                                        validas.empty()

        for casilla in tablero:
                for pieza in piezas:
                        casilla.contiene_pieza(pieza)

        if turno:
                who_plays = font_small.render("White plays", True, (0, 0, 0))
                wp_width = who_plays.get_width()
                pygame.draw.rect(screen, WHITE, [screen.get_width()/2 - wp_width/2 -10, 10, wp_width + 20, 50])
                screen.blit(who_plays, (screen.get_width()/2 - wp_width/2, 20))
        else:
                who_plays = font_small.render("Black plays", True, (255, 255, 255))
                pygame.draw.rect(screen, BLACK, [screen.get_width()/2 -wp_width/2 -10, 10, wp_width + 20, 50])
                screen.blit(who_plays, (screen.get_width()/2 - who_plays.get_width()/2, 20))
        
        for casilla in tablero:
                casilla.check_color(validas)
        tablero.update()
        tablero.draw(screen)
        piezas.update()
        piezas.draw(screen)

        #Refresh Screen
        pygame.display.flip()

        #Number of frames per secong e.g. 60
        clock.tick(60)

        
pygame.quit()
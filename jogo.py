import pygame
import time
import random

pygame.init()

tela_largura = 800
tela_altura = 600
gameDisplay = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Caça Alfabeto")
icone = pygame.image.load("assets/alfabetoIcon.png")
pygame.display.set_icon(icone)
clock = pygame.time.Clock()
preto = (0, 0, 0)
branco = (255, 255, 255)
cesta = pygame.image.load("assets/cestaIcon.png")
cesta_largura = 212
cesta_altura = 128

a = pygame.image.load("assets/a_icon.png")
a_largura = 86
a_altura = 86


b = pygame.image.load("assets/b_icon.png")
b_largura = 86
b_altura = 86


c = pygame.image.load("assets/c_icon.png")
c_largura = 79
c_altura = 76

um = pygame.image.load("assets/um_icon.png")
um_largura = 53
um_altura = 71

dois = pygame.image.load("assets/dois_icon.png")
dois_largura = 68 
dois_altura = 68


tres = pygame.image.load("assets/tres_icon.png")
tres_largura = 76
tres_altura = 78


fundo = pygame.image.load("assets/fundo.jpg")

letras_numero = [a,b,c,um,dois,tres]


def mostrarCesta(x, y):
    gameDisplay.blit(cesta, (x, y))

def mostrarAlfabeto(objeto,x, y):
    gameDisplay.blit(objeto, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, branco)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (tela_largura/2, tela_altura/2)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def dead():
    pygame.mixer.music.stop()
    message_display("Você Perdeu")


def escrePlacar(contador):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Letras Coletadas: "+str(contador), True, branco)
    gameDisplay.blit(text, (10, 30))


def pegaObjeto(indice):
    if indice==1:
        return a
    elif indice==2:
        return b
    elif indice==3:
        return c
    elif indice==4:
        return um
    elif indice==5:
        return dois
    elif indice==6:
        return tres


def game_loop():
    pygame.mixer.music.load("assets/SoundTrack")
    pygame.mixer.music.play(-1)
    cesta_posicaoX = 350
    cesta_posicaoY = 450
    movimentoX = 0
    item_speed = 3
    item_posicaoX = random.randrange(0, tela_largura)
    item_posicaoY = -250
    item_altura = 86
    item_largura = 70
    coleta = 0
    item = pegaObjeto( random.randrange(1, 7) )


    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -10
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 10
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    movimentoX = 0
        cesta_posicaoX = cesta_posicaoX + movimentoX

        gameDisplay.fill(branco)
        gameDisplay.blit(fundo, (0, 0))

        mostrarCesta(cesta_posicaoX, cesta_posicaoY)


        mostrarAlfabeto(item,item_posicaoX, item_posicaoY)
        item_posicaoY = item_posicaoY + item_speed

        if item_posicaoY > tela_altura:
            item = pegaObjeto( random.randrange(1, 7) )
            item_posicaoY = 0-86
            item_speed += 1
            item_posicaoX = random.randrange(0, tela_largura)

        escrePlacar(coleta)
        
        if cesta_posicaoX > tela_largura - cesta_largura:
            cesta_posicaoX = tela_largura - cesta_largura
        elif cesta_posicaoX < 0:
            cesta_posicaoX = 0

        if cesta_posicaoY+50 < item_posicaoY + item_altura:
            if cesta_posicaoX < item_posicaoX and cesta_posicaoX + cesta_largura > item_posicaoX or item_posicaoX+item_largura > cesta_posicaoX and item_posicaoX + item_largura < cesta_posicaoX + item_largura:    
                if item == um or item == dois or item == tres:
                    dead()
                elif item == a or item == b or item == c:
                    item_posicaoY = 900
                    item_posicaoX = 3000
                    coleta = coleta + 1
                    time.sleep(0.05)
                    if item_posicaoY == 900:
                        item = pegaObjeto( random.randrange(1, 7) )
                        item_posicaoX = random.randrange(0, tela_largura)
                        item_posicaoY = 0-86
                        
                    
                    
        
        
        
        pygame.display.update()
        clock.tick(60)


        
        
        











game_loop()
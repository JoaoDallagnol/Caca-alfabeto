import pygame
import time
import random

pygame.init()

tela_largura = 800
tela_altura = 600
gameDisplay = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Caça Alfabeto")
icone = pygame.image.load("assest/alfabetoIcon.png")
pygame.display.set_icon(icone)
clock = pygame.time.clock()
preto = (0, 0, 0)
branco = (255, 255, 255)
cesta = pygame.image.load("assest/cestaIcon.png")
cesta_largura = 212
cesta_altura = 128

a = pygame.image.load("assests/a_icon.png")
a_largura = 86
a_altura = 86

b = pyggame.image.load("assest/b_icon.png")
b_largura = 86
b_altura = 86

c = pygame.image.load("assest/c_icon.png")
c_largura = 79
c_altura = 76

um = pygame.image.load("assest/um_icon.png")
um_largura = 53
um_altura = 71

dois = pygame.image.load("assest/dois_icon.png")
dois_largura = 68 
dois_altura = 68

tres = pygame.image.load("assest/tres_icon.png")
tres_largura = 76
tres_altura = 78

fundo = pygame.image.load("assest/fundo.jpg")

letras_numero = [a,b,c,um,dois,tres]

coleta = pygame.image.load(random.choice(letras_numero))

def mostrarCesta(x, y):
    gameDisplay.blit(cesta, (x, y))

def mostrarAlfabeto(x, y):
    gameDisplay.blit(coleta, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
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
    message_display("Você Morreu")


def escrePlacar(contador):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Desvios: "+str(contador), True, white)
    gameDisplay.blit(text, (10, 30))
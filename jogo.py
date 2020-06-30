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
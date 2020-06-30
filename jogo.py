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
for item in letras_numero:
    item = item

    def mostrarCesta(x, y):
        gameDisplay.blit(cesta, (x, y))

    def mostrarAlfabeto(x, y):
        gameDisplay.blit(item (x, y))

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


    def game_loop():
        cesta_posicaoX = 350
        cesta_posicaoY = 450
        movimentoX = 0
        item_speed = 3
        item_posicaoX = random.randrange(0, tela_largura)
        item_posicaoY = -250
        desvios = 0

        while True:
            # inicio - Interação do usuário
            # event.get do pygame, devolve uma lista de eventos da janela
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    # fecha tudo!
                    quit()
    game_loop()
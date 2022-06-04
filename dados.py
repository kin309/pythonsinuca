import pygame
import sys

pygame.init()

janela_lar = 1100
janela_alt = 700
janela = pygame.display.set_mode((janela_lar, janela_alt))

fonte = pygame.font.SysFont("verdana", 10)
fonte2 = pygame.font.SysFont("verdana", 15)
fonte3 = pygame.font.SysFont("verdana", 30)
fonte4 = pygame.font.SysFont("verdana", 80)
fonte5 = pygame.font.SysFont("verdana", 100)

preto = (15, 15, 15)
gray = (80, 80, 80)
darkgray = (45, 45, 45)
lightgray = (130, 130, 130)
white = (255, 255, 255)
verde = (50, 195, 20)
vermelho = (170, 20, 20)
azul = (10, 50, 140)
amarelo = (220, 200, 20)
pink = (200, 30, 200)
marrom = (40, 30, 10)
roxo = (70, 20, 205)
purplered = (215, 20, 70)
salmao = (210, 90, 110)
laranja = (230, 130, 20)
grenesc = (30, 120, 50)
outer = (140, 80, 60)

cor_fundo = gray
cor_mesa = grenesc

mesa_lar = 700
mesa_alt = 400
borda_largura = 40

xb1,yb1 = 350,350
raiob = 21.6

posb1 = (xb1, yb1)
posb2 = (xb1-raiob, yb1+raiob/2)
posb3 = (xb1-raiob, yb1-raiob/2)
posb4 = (xb1-raiob*2, yb1+raiob)
posb5 = (xb1-raiob*3, yb1+raiob/2)
posb6 = (xb1-raiob*2, yb1-raiob)
posb7 = (xb1-raiob*3, yb1+raiob*1.5)
posb8 = (xb1-raiob*2, yb1)
posb9 = (xb1-raiob*3, yb1-raiob/2)
posb10 = (xb1-raiob*3, yb1-raiob*1.5)
posb11 = (xb1-raiob*4, yb1+raiob*2)
posb12 = (xb1-raiob*4, yb1+raiob)
posb13 = (xb1-raiob*4, yb1)
posb14 = (xb1-raiob*4, yb1-raiob)
posb15 = (xb1-raiob*4, yb1-raiob*2)
posbb = (xb1+400, yb1)

contador = 0
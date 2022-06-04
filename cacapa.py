import pygame
from balls import *


class Cacapa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.diametro = 40
        self.raio = self.diametro/2
        self.color = preto

    def draw(self):
        pygame.draw.ellipse(janela, self.color, (self.x - self.raio, self.y - self.raio, self.diametro, self.diametro))

    def engolir_bola(self):
        for bola in balls:
            if ((bola.x - self.x)**2 + (bola.y - self.y)**2)**0.5 <= bola.raio + self.raio - 3:
                if bola is ballb:
                    ballb.x = -20
                    ballb.y = -20
                    if len(bolas_paradas) == len(balls):
                        ballb.x, ballb.y = posbb
                        ballb.speedx = 0
                        ballb.speedy = 0
                else:
                    balls.remove(bola)
                    bolas_encacapadas.append(bola)
                    bola.speedx = 0
                    bola.speedy = 0
                    bola.x = -20
                    bola.y = -20




def colocador_cacapa():
    caca1.draw()
    caca2.draw()
    caca3.draw()
    caca4.draw()
    caca5.draw()
    caca6.draw()


caca1 = Cacapa(200, 150)
caca2 = Cacapa((200+200+mesa_lar)/2, 140)
caca3 = Cacapa(200+mesa_lar, 150)
caca4 = Cacapa(200, 150+mesa_alt)
caca5 = Cacapa(200+mesa_lar/2, 160+mesa_alt)
caca6 = Cacapa(200+mesa_lar, 150+mesa_alt)

cacapas = [caca1, caca2, caca3, caca4, caca5, caca6]

bolas_encacapadas = []
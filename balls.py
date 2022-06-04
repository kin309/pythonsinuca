import pygame
import numpy as np
from dados import *
import math


class Ball:
    def __init__(self, x, y, speedx, speedy, numero_bola, color, raio = 10, accelerationy = 0, accelerationx=0, friccao = 0.0015,
                 constituicao = 0.08):
        self.x = x
        self.y = y
        self.movimento = bool
        self.speedx = speedx
        self.speedy = speedy
        self.speed = self.calculo_speed
        self.accelerationy = accelerationy
        self.accelerationx = accelerationx
        self.constituicao = constituicao
        self.friccao = friccao
        self.numero_bola = int(numero_bola)
        self.speed = float()
        self.forcar = float()

        self.color = color
        self.raio = raio
        self.diametro = raio * 2

    def principal(self):
        pygame.draw.ellipse(janela, self.color, (self.x - self.raio, self.y - self.raio,
                                                 self.diametro, self.diametro))

        self.x += self.speedx/60
        self.y += self.speedy/60
        self.speedy += self.accelerationy
        self.speedx += self.accelerationx
        if self.speedx > 0:
            self.speedx =  (self.speedx-self.friccao) - self.speedx*self.friccao*1.000001
        if self.speedx < 0:
            self.speedx =   (self.speedx+self.friccao) - self.speedx*self.friccao*1.000001
        if self.speedy > 0:
            self.speedy =   (self.speedy-self.friccao) - self.speedy*self.friccao*1.000001
        if self.speedy < 0:
            self.speedy =   (self.speedy+self.friccao) - self.speedy*self.friccao*1.000001

        # Colisão lado esquerdo
        if self.x - self.raio <= 200 and self in balls:
            self.x = 200.1 + self.raio
            self.speedx = (-self.speedx)+(self.speedx*self.constituicao+0.00111)

        # Colisão lado direito
        if self.x + self.raio >= mesa_lar+200 and self in balls:
            self.x = mesa_lar+200 - 0.1 - self.raio
            self.speedx = (-self.speedx)+(self.speedx*self.constituicao+0.00111)

        # Colisão em cima
        if self.y - self.raio <= 150 and self in balls:
            self.y = self.raio+151
            self.speedy = (-self.speedy)+(self.speedy*self.constituicao+0.00111)

        # Colisão em baixo
        if self.y + self.raio >= mesa_alt+150 - 0.1 and self in balls:
            self.y = mesa_alt+150 - 0.2 - self.raio
            self.speedy = (-self.speedy) + (self.speedy * self.constituicao + 0.00241)
            self.speedx = self.speedx - self.speedx * self.friccao


    def calculo_barra_forcar(self):
        mx, my = pygame.mouse.get_pos()
        distancia_eixo_x = 0
        distancia_eixo_y = 0
        if mx > self.x + self.raio * 2:
            distancia_eixo_x = self.x + self.raio * 2 - mx

        if mx < self.x - self.raio * 2:
            distancia_eixo_x = self.x - self.raio * 2 - mx

        if my > self.y + self.raio * 2:
            distancia_eixo_y = self.y + self.raio * 2 - my

        if my < self.y - self.raio * 2:
            distancia_eixo_y = self.y - self.raio * 2 - my

        forcax = distancia_eixo_x
        forcay = distancia_eixo_y
        self.forcar = (forcay ** 2 + forcax ** 2) ** 0.5
        if self.forcar > 160:
            self.forcar = 160
        return self.forcar


    def aplicarforca(self):
        mx, my = pygame.mouse.get_pos()
        radforcax = 0
        radforcay = 0
        distancia_eixo_x = self.x - mx
        distancia_eixo_y = self.y - my
        forcax = distancia_eixo_x
        forcay = distancia_eixo_y
        self.forcar = (forcay**2 + forcax**2)**0.5
        if self.forcar > 0 or self.forcar < 0:
            radforcax = math.sin(math.asin(forcax/self.forcar))
            radforcay = math.cos(math.acos(forcay/self.forcar))
        if self.forcar > 160:
            self.forcar = 160
        forcax = radforcax * self.forcar
        forcay = radforcay * self.forcar
        self.speedx = forcax*1.6
        self.speedy = forcay*1.6


    def calculo_speed(self):
        self.speed = (self.speedx ** 2 + self.speedy ** 2) ** 0.5
        return self.speed


    def numerobolas(self, fontes):
            numero_bola = fontes.render(str(self.numero_bola), True, preto)
            if self.color == preto:
                numero_bola = fontes.render(str(self.numero_bola), True, white)
                janela.blit(numero_bola, (self.x-4, self.y-6))
            elif self.numero_bola > 0:
                if self.numero_bola <= 9:
                    janela.blit(numero_bola, (self.x-3, self.y-7))
                else:
                    janela.blit(numero_bola, (self.x - 6, self.y - 7))


    def numerobolas_mortas(self, fontes, x, y):
            numero_bolas = fontes.render(str(self.numero_bola), True, preto)
            if self.color == preto:
                numero_bolas = fontes.render(str(self.numero_bola), True, white)
                janela.blit(numero_bolas, (x+15, y+8))

            else:
                if self.numero_bola <= 9:
                    janela.blit(numero_bolas, (x+14, y+8))
                else:
                    janela.blit(numero_bolas, (x+10, y+8))


def calculo_speed_das_bolas():
       for ba in balls:
        if ba.calculo_speed() < 2.4:
            ba.speedx = 0
            ba.speedy = 0
            ba.movimento = False
        else:
            ba.movimento = True


def desenhar_linha():
    for ba in balls:
        if ba.movimento is True:
            if ba in bolas_paradas:
                bolas_movimento.append(ba)
                bolas_paradas.remove(ba)

        else:
            if ba in bolas_movimento:
                bolas_paradas.append(ba)
                bolas_movimento.remove(ba)
    if len(bolas_paradas) == len(balls):
        pygame.draw.line(janela, start_pos=(pygame.mouse.get_pos()), end_pos=(ballb.x, ballb.y), color=salmao, width=3)


def checkcollisions():
    for i in range(len(balls)):
        for j in range(len(balls) - 1, i, -1):
            distancia_bolas = ((balls[i].x - balls[j].x) ** 2 + (balls[i].y - balls[j].y) ** 2) ** 0.5
            if distancia_bolas + 0.01 +  0.00005*balls[i].speed <= balls[i].raio + balls[j].raio:
                if i != j:
                    vb1 = np.array([balls[i].speedx, balls[i].speedy])
                    vb2 = np.array([balls[j].speedx, balls[j].speedy])
                    xbs1 = np.array([balls[i].x, balls[i].y])
                    xb2 = np.array([balls[j].x, balls[j].y])
                    balls[i].speedx, balls[i].speedy = compute_velocity(vb1, vb2, ball1.raio, ball2.raio, xbs1,
                                                                        xb2) / 1.0005
                    balls[j].speedx, balls[j].speedy = compute_velocity(vb2, vb1, ball1.raio, ball2.raio, xb2,
                                                                        xbs1) / 1.0005


def compute_velocity(v1, v2, m1, m2, x1, x2):
    return v1 - (2 * m2 / (m1 + m2)) * np.dot(v1 - v2, x1 - x2) / np.linalg.norm(x1 - x2) ** 2 * (x1 - x2)


ball1 = Ball(posb1[0],posb1[1], speedx=0, speedy=0, color=amarelo, numero_bola=1)
ball2 = Ball(posb2[0],posb2[1], speedx=0, speedy=0, color=azul, numero_bola=2)
ball3 = Ball(posb3[0],posb3[1], speedx=0, speedy=0, color=vermelho, numero_bola=3)
ball4 = Ball(posb4[0],posb4[1], speedx=0, speedy=0, color=roxo, numero_bola=4)
ball8 = Ball(posb8[0],posb8[1], speedx=0, speedy=0, color=preto, numero_bola=8)
ball6 = Ball(posb6[0],posb6[1], speedx=0, speedy=0, color=verde, numero_bola=6)
ball7 = Ball(posb7[0],posb7[1], speedx=0, speedy=0, color=marrom, numero_bola=7)
ball5 = Ball(posb5[0],posb5[1], speedx=0, speedy=0, color=laranja, numero_bola=5)
ball9 = Ball(posb9[0],posb9[1], speedx=0, speedy=0, color=amarelo, numero_bola=9)
ball10 = Ball(posb10[0],posb10[1], speedx=0, speedy=0, color=azul, numero_bola=10)
ball11 = Ball(posb11[0],posb11[1], speedx=0, speedy=0, color=vermelho, numero_bola=11)
ball12 = Ball(posb12[0],posb12[1], speedx=0, speedy=0, color=roxo, numero_bola=12)
ball13 = Ball(posb13[0],posb13[1], speedx=0, speedy=0, color=laranja, numero_bola=13)
ball14 = Ball(posb14[0],posb14[1], speedx=0, speedy=0, color=verde, numero_bola=14)
ball15 = Ball(posb15[0],posb15[1], speedx=0, speedy=0, color=marrom, numero_bola=15)
ballb = Ball(posbb[0],posbb[1], speedx=0, speedy=0, color=white, numero_bola=0)

balls = [ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9,
         ball10, ball11, ball12, ball13, ball14, ball15, ballb]

bolas_paradas = [ball1, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9,
         ball10, ball11, ball12, ball13, ball14, ball15, ballb]

bolas_movimento = []
import sys

import pygame

from mesa import *
from timer import *
from time import sleep

from evenhandler import eventhandler

def principal_bolas():
    for bal in balls:
        bal.principal()
        bal.numerobolas(fonte)


def tirador_bola_branca():
    if ballb in bolas_encacapadas:
        bolas_encacapadas.remove(ballb)
        if len(bolas_paradas) == len(balls):
            balls.append(ballb)
            ballb.speedx = 0
            ballb.speedy = 0
            ballb.x, ballb.y = posbb

def fim_de_jogo():
    if len(balls) == 1:
        looper = False
        eventhandler.scene = 0
        return looper



def voce_perdeu():
    if ball8 in bolas_encacapadas and len(balls) > 1:

        pygame.draw.rect(janela, lightgray, (290, 160, 480, 90))
        texto_perdeu = fonte4.render('Fim de jogo', False, white)
        janela.blit(texto_perdeu, (290,150))
        ball8morreu = True
        eventhandler.scene = 0


def desenhar_cronometro():
    segundos = cronometro.intervalo_tempo
    minutos = int(segundos/60)
    segundos -= int(minutos*60)
    pygame.draw.rect(janela, lightgray, (495, 30, 100, 40), 2)
    textoc = fonte3.render(f"{minutos:02}:{segundos:02}", True, white)
    janela.blit(textoc,(500, 30))

def jogo():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bug = True
                    if bug is True:
                        ballb.x, ballb.y = pygame.mouse.get_pos()

                if event.key == pygame.K_q:
                    for ball in balls:
                        balls.remove(ball)
                        bolas_encacapadas.append(ball)

                if event.key == pygame.K_w:
                    if ball8 in balls:
                        balls.remove(ball8)
                        bolas_encacapadas.append(ball8)
                        print(len(balls))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(bolas_paradas) == len(balls):
                    forca = True
                    if forca is True:
                        ballb.aplicarforca()

        cronometro.comecar()
        janela.fill(cor_fundo)
        ballb.calculo_speed()
        for caca in cacapas:
            caca.engolir_bola()
        calculo_speed_das_bolas()
        mesa.desenhar_mesa()
        desenhar_linha()
        checkcollisions()
        principal_bolas()
        desenhar_cronometro()
        if fim_de_jogo() is False:
            eventhandler.scene = 0
        if voce_perdeu() is True:
            eventhandler.scene = 0

        pygame.display.update()
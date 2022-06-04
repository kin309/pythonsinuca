from jogo import *
from time import sleep
from evenhandler import eventhandler


def tela_inicial():
        mouseposx, mouseposy = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 365+320 > mouseposx > 365 and 280+90 > mouseposy > 280:
                    eventhandler.scene = 1
                    break

                if 365 + 320 > mouseposx > 365 and 440+90 > mouseposy > 440:
                    sleep(0.15)
                    pygame.quit()
                    sys.exit()




        janela.fill(grenesc)

        texto_inicial = fonte5.render(str('Sinuqueta'), True, white)
        janela.blit(texto_inicial, (280, 90))

        pygame.draw.rect(janela, lightgray, (365, 280, 320, 90))
        texto_botao_iniciar = fonte4.render(str('Iniciar'), True, white)
        janela.blit(texto_botao_iniciar, (395, 275))


        pygame.draw.rect(janela, lightgray, (365, 440, 320, 90))
        texto_sair = fonte4.render(str('Sair'), True, white)
        janela.blit(texto_sair, (435, 435))
        pygame.display.update()
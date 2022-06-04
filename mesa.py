from cacapa import *

class Mesa:
    def __init__(self):
        self.areax = (200, 900)
        self.areay = (150, 550)
        self.largura = 700
        self.altura = 400
        self.bordaespessura = 40

    def desenhar_mesa(self):
        # Área da mesa
        pygame.draw.rect(janela, cor_mesa, (200, 150, self.largura, self.altura))

        # Barra de força
        if len(bolas_paradas) == len(balls):
            pygame.draw.rect(janela, vermelho, (100, 110, 10, 5.33 * ballb.calculo_barra_forcar()/1.75))

        # Borda da mesa
        pygame.draw.rect(janela, darkgray, (160, 150, borda_largura, mesa_alt))
        pygame.draw.rect(janela, darkgray, (200 + mesa_lar, 150, borda_largura, mesa_alt))
        pygame.draw.rect(janela, darkgray, (160, 110, mesa_lar + 80, borda_largura))
        pygame.draw.rect(janela, darkgray, (160, 550, mesa_lar + 80, borda_largura))

        # Espaço para bolas mortas
        pygame.draw.rect(janela, darkgray, (195, 630, 700, 60))
        pygame.draw.rect(janela, lightgray, (200, 635, 690, 50))

        for x in range(15):
            pygame.draw.ellipse(janela, preto, (210 + 45 * x, 640,
                                                   20 * 2, 20 * 2))

        # Colocador bolas encaçapadas
        for x, ba in enumerate(bolas_encacapadas):
            pygame.draw.ellipse(janela, ba.color, (210 + 45 * x, 640,
                                                   ba.diametro * 2, ba.diametro * 2))
            ba.numerobolas_mortas(fonte2, 210 + 45 * x, 640)



        # Colocador caçapas
        caca1.draw()
        caca2.draw()
        caca3.draw()
        caca4.draw()
        caca5.draw()
        caca6.draw()

mesa = Mesa()

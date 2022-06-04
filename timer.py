import time

class Cronometro:
    def __init__(self):
        self.start = time.time()
        self.intervalo_tempo = 0

    def comecar(self):
        self.intervalo_tempo = int(time.time() - self.start)
        return self.intervalo_tempo

    def resetar(self):
        self.start = time.time()




cronometro = Cronometro()
# while True:
#     cronometro.comecar()
#     print(cronometro.intervalo_tempo)

    # if cronometro.intervalo_tempo == 10:
    #     cronometro.resetar()
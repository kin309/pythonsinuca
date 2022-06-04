from cacapa import *
from telainicial import *
from evenhandler import eventhandler

actual_scene = 0
while True:
    if eventhandler.scene == 0:
        tela_inicial()
    elif eventhandler.scene == 1:
        jogo()



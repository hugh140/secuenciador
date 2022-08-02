import pygame
from pygame import mixer

#Iniciar Pygame
pygame.init()
size = 100, 100
pygame.display.set_mode(size)

#Cargar Sonidos
bb = mixer.Sound("Sounds/bombo.mp3")
sn = mixer.Sound("Sounds/snare.mp3")
hh = mixer.Sound("Sounds/hihat.wav")
nd = mixer.Sound("Sounds/silencio.mp3")

#Secuenciador ejemplo
ritmo = [
    [bb, nd, nd, nd, bb, bb, nd, nd],
    [nd, nd, sn, nd, nd, nd, sn, nd],
    [hh, hh, hh, hh, hh, hh, hh, hh]
]
bpm = 100
bpmSec = int((60 / (bpm * 4)) * 1000)

class Secuenciador:
    compas = 0

    def update(self):
        while True:
            pygame.time.delay(bpmSec)
            self.secuenciador()

    def secuenciador(self):
        for sonido in range(len(ritmo)):
            ritmo[sonido][self.compas].play()
        
        if self.compas >= len(ritmo[0]) - 1:
            self.compas = 0
        else: self.compas += 1
    
Secuenciador().update()
    
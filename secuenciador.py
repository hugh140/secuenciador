from pygame import mixer

mixer.init()
mixer.set_num_channels(6)

#Cargar sonidos
kk =    mixer.Sound('Sonidos/kick.wav')
sn =    mixer.Sound('Sonidos/snare.wav')
clhh =  mixer.Sound('Sonidos/clhh.wav')
ophh =  mixer.Sound('Sonidos/ophh.wav')
cymbal =  mixer.Sound('Sonidos/cymbal.wav')
nd =    mixer.Sound("Sonidos/silencio.mp3")

#Secuenciador ejemplo
class Secuenciador:
    def __init__(self):
        self.compas = 0
        self.ritmo = (  
            [nd,nd,nd,nd, nd,nd,nd,nd, nd,nd,nd,nd, nd,nd,nd,nd],
            [nd,nd,nd,nd, nd,nd,nd,nd, nd,nd,nd,nd, nd,nd,nd,nd],
            [nd,nd,nd,nd, nd,nd,nd,nd, nd,nd,nd,nd, nd,nd,nd,nd],
            [nd,nd,nd,nd, nd,nd,nd,nd, nd,nd,nd,nd, nd,nd,nd,nd],
            [nd,nd,nd,nd, nd,nd,nd,nd, nd,nd,nd,nd, nd,nd,nd,nd])
        self.instrumento = [kk, sn, clhh, ophh, cymbal]
        self.nd = nd

    def play(self):
        for sonido in range(len(self.ritmo)):
            self.ritmo[sonido][self.compas].play()
        
        if self.compas >= len(self.ritmo[0]) - 1:
            self.compas = 0
        else: self.compas += 1

    def stop(self):
        self.compas = 0

    def cambiarRitmo(self, instrumento, compas):
        if self.ritmo[instrumento][compas] == self.instrumento[instrumento]:
            self.ritmo[instrumento][compas] = nd
        else:
            self.ritmo[instrumento][compas] = self.instrumento[instrumento]

    def getCompas(self):
        return self.compas

from secuenciador import Secuenciador

sec = Secuenciador()
class App():
    #Métodos introducción de datos
    def __init__(self, bpm):
        self.bpm = bpm
        self.playSecuenciador = False
        
    def appInfo(self, listaBotones, pantalla):
        self.botones = listaBotones
        self.pantalla = pantalla

    def playBoton(self, playBoton, playIMG, stopIMG):
        self.playBoton = playBoton
        self.playIMG = playIMG
        self.stopIMG = stopIMG

    def bpmBotones(self, bpmTxt, 
            incBoton, dcrBoton,
            incIMG, dcrIMG, 
            mptyIMG):
        self.bpmTxt = bpmTxt
        self.incBoton = incBoton
        self.dcrBoton = dcrBoton
        self.mptyIMG = mptyIMG
        self.incIMG = incIMG
        self.dcrIMG = dcrIMG

    #Métodos Funcionamiento Secuenciador
    def loopSecuenciador(self):
        if self.playSecuenciador:
            self.compasBotonColor()
            sec.play()
            bpmSec = int(15000 / self.bpm)
            self.pantalla.after(bpmSec, self.loopSecuenciador)
        else: 
            self.eliminarCompasColor()
            sec.stop()

    def switch(self):
        if not self.playSecuenciador:
            self.playSecuenciador = True
            self.loopSecuenciador()
            self.playBoton["image"] = self.stopIMG
        else:
            self.playSecuenciador = False
            self.loopSecuenciador()
            self.playBoton["image"] = self.playIMG

    def aumentarBPM(self):
        if self.bpm < 240:
            self.bpm += 10
            self.bpmTxt["text"] = str(self.bpm)
            self.incBoton["image"] = self.incIMG
            self.dcrBoton["image"] = self.dcrIMG
        else:
            self.bpm += 10
            self.bpmTxt["text"] = str(self.bpm)
            self.incBoton["image"] = self.mptyIMG

    def disminuirBPM(self):
        if self.bpm > 60:
            self.bpm -= 10
            self.bpmTxt["text"] = str(self.bpm)
            self.incBoton["image"] = self.incIMG
            self.dcrBoton["image"] = self.dcrIMG
        else:
            self.bpm -= 10
            self.bpmTxt["text"] = str(self.bpm)
            self.dcrBoton["image"] = self.mptyIMG

    def secBoton(self, instrumento, compas, boton):
        sec.cambiarRitmo(instrumento, compas)
        if boton["bg"] == "#26408B":
            boton.configure(bg="#438CDB")
        else: boton["bg"] = "#26408B"

    def compasBotonColor(self):
        indice = sec.getCompas() - 1
        if sec.getCompas() == 0:
            indice = 15

        botonColAnterior = [b[indice] for b in self.botones]
        for boton in range(len(botonColAnterior)):
            if sec.ritmo[boton][indice] == sec.nd:
                self.botones[boton][indice].configure(bg="#438CDB")
            else: self.botones[boton][indice].configure(bg="#26408B")

        botonCol = [b[sec.getCompas()] for b in self.botones]
        for boton in botonCol:
            boton.configure(bg="black")

    def eliminarCompasColor(self):
        row = 0; col = 0
        for botonCol in self.botones:
            for boton in botonCol:
                if sec.ritmo[row][col] == sec.nd:
                    boton.configure(bg="#438CDB")
                else: boton.configure(bg="#26408B")
                col += 1
            col = 0; row += 1
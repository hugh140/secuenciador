from tkinter import *
from app import App
            
if __name__ == '__main__':

    #Diseño Tkinter
    pantalla = Tk()
    pantalla.geometry("1280x720")
    pantalla.title("Music Station")

    #Intefaz Secuenciador
    fr = Frame(pantalla)

    Label(fr, 
        text="Music Station\n",
        font=("Lucida Console", 30)
        ).grid(row=0,column=0,columnspan=30)

    Frame(fr, bg="#193552", width=25*2, height=10).grid(row=1,column=1)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=1,column=2)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=1,column=3)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=1,column=4)
    Frame(fr, bg="#193552", width=25*2, height=10).grid(row=1,column=5)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=1,column=6)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=1,column=7)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=1,column=8)
    Frame(fr, bg="#193552", width=25*2, height=10).grid(row=1,column=9)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=1,column=10)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=1,column=11)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=1,column=12)
    Frame(fr, bg="#193552", width=25*2, height=10).grid(row=1,column=13)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=1,column=14)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=1,column=15)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=1,column=16)

    Label(fr, 
        text="Kick", 
        font=("Microsoft New Tai Lue", "16")
        ).grid(row=2,column=0,padx=20)
    b00 = Button(fr, command=lambda: app.secBoton(0,0,b00))
    b01 = Button(fr, command=lambda: app.secBoton(0,1,b01))
    b02 = Button(fr, command=lambda: app.secBoton(0,2,b02))
    b03 = Button(fr, command=lambda: app.secBoton(0,3,b03))
    b04 = Button(fr, command=lambda: app.secBoton(0,4,b04))
    b05 = Button(fr, command=lambda: app.secBoton(0,5,b05))
    b06 = Button(fr, command=lambda: app.secBoton(0,6,b06))
    b07 = Button(fr, command=lambda: app.secBoton(0,7,b07))
    b08 = Button(fr, command=lambda: app.secBoton(0,8,b08))
    b09 = Button(fr, command=lambda: app.secBoton(0,9,b09))
    b010 = Button(fr, command=lambda: app.secBoton(0,10,b010))
    b011 = Button(fr, command=lambda: app.secBoton(0,11,b011))
    b012 = Button(fr, command=lambda: app.secBoton(0,12,b012))
    b013 = Button(fr, command=lambda: app.secBoton(0,13,b013))
    b014 = Button(fr, command=lambda: app.secBoton(0,14,b014))
    b015 = Button(fr, command=lambda: app.secBoton(0,15,b015))

    Label(fr,
        text="Snare", 
        font=("Microsoft New Tai Lue", "16")
        ).grid(row=3,column=0,padx=20)
    b10 = Button(fr, command=lambda: app.secBoton(1,0,b10))
    b11 = Button(fr, command=lambda: app.secBoton(1,1,b11))
    b12 = Button(fr, command=lambda: app.secBoton(1,2,b12))
    b13 = Button(fr, command=lambda: app.secBoton(1,3,b13))
    b14 = Button(fr, command=lambda: app.secBoton(1,4,b14))
    b15 = Button(fr, command=lambda: app.secBoton(1,5,b15))
    b16 = Button(fr, command=lambda: app.secBoton(1,6,b16))
    b17 = Button(fr, command=lambda: app.secBoton(1,7,b17))
    b18 = Button(fr, command=lambda: app.secBoton(1,8,b18))
    b19 = Button(fr, command=lambda: app.secBoton(1,9,b19))
    b110 = Button(fr, command=lambda: app.secBoton(1,10,b110))
    b111 = Button(fr, command=lambda: app.secBoton(1,11,b111))
    b112 = Button(fr, command=lambda: app.secBoton(1,12,b112))
    b113 = Button(fr, command=lambda: app.secBoton(1,13,b113))
    b114 = Button(fr, command=lambda: app.secBoton(1,14,b114))
    b115 = Button(fr, command=lambda: app.secBoton(1,15,b115))

    Label(fr, 
        text="Cl hh", 
        font=("Microsoft New Tai Lue", "16")
        ).grid(row=4,column=0,padx=20)
    b20 = Button(fr, command=lambda: app.secBoton(2,0,b20))
    b21 = Button(fr, command=lambda: app.secBoton(2,1,b21))
    b22 = Button(fr, command=lambda: app.secBoton(2,2,b22))
    b23 = Button(fr, command=lambda: app.secBoton(2,3,b23))
    b24 = Button(fr, command=lambda: app.secBoton(2,4,b24))
    b25 = Button(fr, command=lambda: app.secBoton(2,5,b25))
    b26 = Button(fr, command=lambda: app.secBoton(2,6,b26))
    b27 = Button(fr, command=lambda: app.secBoton(2,7,b27))
    b28 = Button(fr, command=lambda: app.secBoton(2,8,b28))
    b29 = Button(fr, command=lambda: app.secBoton(2,9,b29))
    b210 = Button(fr, command=lambda: app.secBoton(2,10,b210))
    b211 = Button(fr, command=lambda: app.secBoton(2,11,b211))
    b212 = Button(fr, command=lambda: app.secBoton(2,12,b212))
    b213 = Button(fr, command=lambda: app.secBoton(2,13,b213))
    b214 = Button(fr, command=lambda: app.secBoton(2,14,b214))
    b215 = Button(fr, command=lambda: app.secBoton(2,15,b215))

    Label(fr, 
        text="Op hh", 
        font=("Microsoft New Tai Lue", "16")
        ).grid(row=5,column=0,padx=20)
    b30 = Button(fr, command=lambda: app.secBoton(3,0,b30))
    b31 = Button(fr, command=lambda: app.secBoton(3,1,b31))
    b32 = Button(fr, command=lambda: app.secBoton(3,2,b32))
    b33 = Button(fr, command=lambda: app.secBoton(3,3,b33))
    b34 = Button(fr, command=lambda: app.secBoton(3,4,b34))
    b35 = Button(fr, command=lambda: app.secBoton(3,5,b35))
    b36 = Button(fr, command=lambda: app.secBoton(3,6,b36))
    b37 = Button(fr, command=lambda: app.secBoton(3,7,b37))
    b38 = Button(fr, command=lambda: app.secBoton(3,8,b38))
    b39 = Button(fr, command=lambda: app.secBoton(3,9,b39))
    b310 = Button(fr, command=lambda: app.secBoton(3,10,b310))
    b311 = Button(fr, command=lambda: app.secBoton(3,11,b311))
    b312 = Button(fr, command=lambda: app.secBoton(3,12,b312))
    b313 = Button(fr, command=lambda: app.secBoton(3,13,b313))
    b314 = Button(fr, command=lambda: app.secBoton(3,14,b314))
    b315 = Button(fr, command=lambda: app.secBoton(3,15,b315))

    Label(fr, 
        text="Cymbal", 
        font=("Microsoft New Tai Lue", "16")
        ).grid(row=6,column=0,padx=20)
    b40 = Button(fr, command=lambda: app.secBoton(4,0,b40))
    b41 = Button(fr, command=lambda: app.secBoton(4,1,b41))
    b42 = Button(fr, command=lambda: app.secBoton(4,2,b42))
    b43 = Button(fr, command=lambda: app.secBoton(4,3,b43))
    b44 = Button(fr, command=lambda: app.secBoton(4,4,b44))
    b45 = Button(fr, command=lambda: app.secBoton(4,5,b45))
    b46 = Button(fr, command=lambda: app.secBoton(4,6,b46))
    b47 = Button(fr, command=lambda: app.secBoton(4,7,b47))
    b48 = Button(fr, command=lambda: app.secBoton(4,8,b48))
    b49 = Button(fr, command=lambda: app.secBoton(4,9,b49))
    b410 = Button(fr, command=lambda: app.secBoton(4,10,b410))
    b411 = Button(fr, command=lambda: app.secBoton(4,11,b411))
    b412 = Button(fr, command=lambda: app.secBoton(4,12,b412))
    b413 = Button(fr, command=lambda: app.secBoton(4,13,b413))
    b414 = Button(fr, command=lambda: app.secBoton(4,14,b414))
    b415 = Button(fr, command=lambda: app.secBoton(4,15,b415))

    Frame(fr, bg="#193552", width=25*2, height=10).grid(row=7,column=1)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=7,column=2)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=7,column=3)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=7,column=4)
    Frame(fr, bg="#193552", width=25*2, height=10).grid(row=7,column=5)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=7,column=6)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=7,column=7)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=7,column=8)
    Frame(fr, bg="#193552", width=25*2, height=10).grid(row=7,column=9)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=7,column=10)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=7,column=11)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=7,column=12)
    Frame(fr, bg="#193552", width=25*2, height=10).grid(row=7,column=13)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=7,column=14)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=7,column=15)
    Frame(fr, bg="#3269A4", width=25*2, height=10).grid(row=7,column=16)

    #Menú Opciones
    playIMG = PhotoImage(file="Iconos/play.png").zoom(2,2)
    stopIMG = PhotoImage(file="Iconos/stop.png").zoom(2,2)
    increaseIMG = PhotoImage(file="Iconos/increase.png")
    decreaseIMG = PhotoImage(file="Iconos/decrease.png")
    emptyIMG = PhotoImage(None)

    playBoton = Button(fr, 
        image=playIMG, 
        borderwidth=0,
        command=lambda: app.switch())
    playBoton.grid(row=8, column=1, pady=25)

    decreaseBoton = Button(fr, 
        image=decreaseIMG,
        padx=1, pady=1,
        borderwidth=0,
        command=lambda: app.disminuirBPM())
    decreaseBoton.grid(row=8, column=2)

    bpmTXT = Label(fr, 
        text="120",
        font=("Microsoft New Tai Lue", "20"))
    bpmTXT.grid(row=8, column=3)

    increaseBoton = Button(fr,
        image=increaseIMG,
        padx=1, pady=1,
        borderwidth=0,
        command=lambda: app.aumentarBPM())
    increaseBoton.grid(row=8, column=4)

    botones = (
        (b00,b01,b02,b03,b04,b05,b06,b07,b08,b09,b010,b011,b012,b013,b014,b015),
        (b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b110,b111,b112,b113,b114,b115),
        (b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b210,b211,b212,b213,b214,b215),
        (b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b310,b311,b312,b313,b314,b315),
        (b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b410,b411,b412,b413,b414,b415))

    #Invocar App
    app = App(120)
    app.appInfo(botones, fr)
    app.playBoton(playBoton, playIMG, stopIMG)
    app.bpmBotones(bpmTXT, 
        increaseBoton, decreaseBoton,
        increaseIMG, decreaseIMG,
        emptyIMG)

    #Dibujar Botones
    row = 2; col = 1
    for boton in botones:
        for colBoton in boton:
            colBoton.configure(
                padx=25, 
                pady=20, 
                bd=5, 
                bg="#438CDB", 
                activebackground="#17043A")
            colBoton.grid(row=row, column=col, padx=2)
            col += 1
        col = 1; row += 1

    fr.place(relx=0.5, rely=0.5, anchor=CENTER)
    fr.mainloop()
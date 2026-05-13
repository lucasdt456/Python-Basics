import tkinter
import customtkinter as ctk
from PIL import Image, ImageDraw, ImageFont, ImageTk
import random

class tres_en_raya:

    def __init__(self):
        self.raiz = ctk.CTk()
        self.raiz.title("Juego - Tres en Raya")
        self.raiz.geometry("450x450")
        self.raiz.resizable(False, False)

        self.canvas_uno = ctk.CTkCanvas(self.raiz, bg="#242424",
                                        #bd=0, # quita cualquier borde adicional
                                        highlightthickness=0 #elimina el borde por defecto
                                        )  
        self.canvas_uno.create_line(162, 6, 162, 480, fill="white", width=12) #vertical 1
        self.canvas_uno.create_line(324, 6, 324, 480, fill="white", width=12) #vertical 2
        self.canvas_uno.create_line(6, 162, 480, 162, fill="white", width=12) #horizontal 1
        self.canvas_uno.create_line(6, 324, 480, 324, fill="white", width=12) #horizontal 2
        self.canvas_uno.pack(pady=200)

        self.sale_X_de_inicio = False
        self.sale_O_de_inicio = False

        self.ganador_partida = False

    #Emoji_Label
    def emoji_img(self, texto="❎🔴", font_px=32, padding=6):
        
        # pixels = points * 96 / 72 : 96 is windowsDPI
        font_pt = int(round(font_px * 72/96))

        try:
            font = ImageFont.truetype("seguiemj.ttf", size=font_pt)

        except OSError:
            font = ImageFont.truetype(r"C:\Windows\Fonts\seguiemj.ttf", size=font_pt)

        bbox = font.getbbox(texto)
        w = (bbox[2] - bbox[0])
        h = (bbox[3] - bbox[1])


        im = Image.new("RGBA", (w, h), (255, 255, 255, 0))
        draw = ImageDraw.Draw(im)
        draw.text((padding, padding), texto, font=font, embedded_color=True)

        return ImageTk.PhotoImage(im)

    #Label
    def Label_principal(self):
        
        self.emoji = self.emoji_img("⭕✖️", font_px=64)
        
        texto_inicial = ctk.CTkLabel(master=self.raiz,
                                     text="   Juego Tres en Raya -",
                                     text_color="white",
                                     fg_color="#73AD75",
                                     corner_radius=300,
                                     font=ctk.CTkFont(family='Cascadia Code', size=20, weight="bold"),
                                     image=self.emoji,
                                     compound="right",
                                     pady = 6
                                     )
                                    
        texto_inicial.place(x=27, y=50)

    #Botones
    def botones(self):
        #1
        self.boton_uno_primeraF = ctk.CTkButton(master=self.canvas_uno,
                                  text="", font=ctk.CTkFont(family='Cascadia Code', size=50, weight="bold"),
                                  width=75, height=75,
                                  corner_radius=0,
                                  border_width=0,
                                  fg_color="#242424",
                                  hover_color="#242424",
                                  command=lambda: self.click(self.boton_uno_primeraF))
                                                
        self.boton_uno_primeraF.grid(row=0, column=0, padx=3, pady=3)
        

        #2
        self.boton_dos_primeraF = ctk.CTkButton(master=self.canvas_uno,
                                  text="", font=ctk.CTkFont(family='Cascadia Code', size=50, weight="bold"),
                                  width=75, height=75,
                                  corner_radius=0,
                                  border_width=0,
                                  fg_color="#242424",
                                  hover_color="#242424",
                                  command=lambda: self.click(self.boton_dos_primeraF))

        self.boton_dos_primeraF.grid(row=0, column=1, padx=3, pady=3)

        #3
        self.boton_tres_primeraF = ctk.CTkButton(master=self.canvas_uno,
                                  text="", font=ctk.CTkFont(family='Cascadia Code', size=50, weight="bold"),
                                  width=75, height=75,
                                  corner_radius=0,
                                  border_width=0,
                                  fg_color="#242424",
                                  hover_color="#242424",
                                  command=lambda: self.click(self.boton_tres_primeraF))

        self.boton_tres_primeraF.grid(row=0, column=2, padx=3, pady=3)

        #4
        self.boton_cuatro_segundaF = ctk.CTkButton(master=self.canvas_uno,
                                  text="", font=ctk.CTkFont(family='Cascadia Code', size=50, weight="bold"),
                                  width=75, height=75,
                                  corner_radius=0,
                                  border_width=0,
                                  fg_color="#242424",
                                  hover_color="#242424",
                                  command=lambda: self.click(self.boton_cuatro_segundaF))

        self.boton_cuatro_segundaF.grid(row=1, column=0, padx=3, pady=3)

        #5
        self.boton_cinco_segundaF = ctk.CTkButton(master=self.canvas_uno,
                                  text="", font=ctk.CTkFont(family='Cascadia Code', size=50, weight="bold"),
                                  width=75, height=75,
                                  corner_radius=0,
                                  border_width=0,
                                  fg_color="#242424",
                                  hover_color="#242424",
                                  command=lambda: self.click(self.boton_cinco_segundaF))

        self.boton_cinco_segundaF.grid(row=1, column=1, padx=3, pady=3)

        #6
        self.boton_seis_segundaF = ctk.CTkButton(master=self.canvas_uno,
                                  text="", font=ctk.CTkFont(family='Cascadia Code', size=50, weight="bold"),
                                  width=75, height=75,
                                  corner_radius=0,
                                  border_width=0,
                                  fg_color="#242424",
                                  border_color="white",
                                  hover_color="#242424",
                                  command=lambda: self.click(self.boton_seis_segundaF))

        self.boton_seis_segundaF.grid(row=1, column=2, padx=3, pady=3)

        #7
        self.boton_siete_terceraF = ctk.CTkButton(master=self.canvas_uno,
                                  text="", font=ctk.CTkFont(family='Cascadia Code', size=50, weight="bold"),
                                  width=75, height=75,
                                  corner_radius=0,
                                  border_width=0,
                                  fg_color="#242424",
                                  border_color="white",
                                  hover_color="#242424",
                                  command=lambda: self.click(self.boton_siete_terceraF))

        self.boton_siete_terceraF.grid(row=2, column=0, padx=3, pady=3)

        #8
        self.boton_ocho_terceraF = ctk.CTkButton(master=self.canvas_uno,
                                  text="", font=ctk.CTkFont(family='Cascadia Code', size=50, weight="bold"),
                                  width=75, height=75,
                                  corner_radius=0,
                                  border_width=0,
                                  fg_color="#242424",
                                  border_color="white",
                                  hover_color="#242424",
                                  command=lambda: self.click(self.boton_ocho_terceraF))


        self.boton_ocho_terceraF.grid(row=2, column=1, padx=3, pady=3)

        #9
        self.boton_nueve_terceraF = ctk.CTkButton(master=self.canvas_uno,
                                  text="", font=ctk.CTkFont(family='Cascadia Code', size=50, weight="bold"),
                                  width=75, height=75,
                                  corner_radius=0,
                                  border_width=0,
                                  fg_color="#242424",
                                  hover_color="#242424",
                                  command=lambda: self.click(self.boton_nueve_terceraF))


        self.boton_nueve_terceraF.grid(row=2, column=2, padx=3, pady=3)

    #Emoji_X y O
    def emoji_X(self, texto="❌", font_px=50, padding=11):
        
        # pixels = points * 96 / 72 : 96 is windowsDPI
        font_pt = int(round(font_px * 72/96))

        try:
            font = ImageFont.truetype("seguiemj.ttf", size=font_pt)

        except OSError:
            font = ImageFont.truetype(r"C:\Windows\Fonts\seguiemj.ttf", size=font_pt)

        bbox = font.getbbox(texto)
        w = (bbox[2] - bbox[0]) + 2 * padding
        h = (bbox[3] - bbox[1]) + 1 * padding


        im = Image.new("RGBA", (w, h), (255, 255, 255, 0))
        draw = ImageDraw.Draw(im)
        draw.text((padding, padding), texto, font=font, embedded_color=False, fill="#785DC7")

        return ImageTk.PhotoImage(im)
    
    def emoji_O(self, texto="⭕", font_px=50, padding=11):
        
        # pixels = points * 96 / 72 : 96 is windowsDPI
        font_pt = int(round(font_px * 72/96))

        try:
            font = ImageFont.truetype("seguiemj.ttf", size=font_pt)

        except OSError:
            font = ImageFont.truetype(r"C:\Windows\Fonts\seguiemj.ttf", size=font_pt)

        bbox = font.getbbox(texto)
        w = (bbox[2] - bbox[0]) + 2 * padding
        h = (bbox[3] - bbox[1]) + 1 * padding


        im = Image.new("RGBA", (w, h), (255, 255, 255, 0))
        draw = ImageDraw.Draw(im)
        draw.text((padding, padding), texto, font=font, embedded_color=True)

        return ImageTk.PhotoImage(im)

    
    #Texto para turno de X 
    def jugar_con_X(self):

        if hasattr(self, "mensaje_jugador_O"):
            self.mensaje_jugador_O.place_forget()

        self.emoji_x = self.emoji_X(texto="❌", font_px=50)

        if not self.ganador_partida:

            self.mensaje_jugador_X = ctk.CTkLabel(master=self.raiz,
                        text="Es el turno de:", text_color="white", 
                        font=ctk.CTkFont(family='Cascadia Code', size=16, weight="bold"),
                        fg_color="#73AD75",
                        width=80, height=40,
                        corner_radius=200,
                        image=self.emoji_x,
                        compound="right"
                        )
            
            self.mensaje_jugador_X.place(x=110, y=360)
            
            self.boton_jugar.destroy()
            self.sale_X_de_inicio = True

    #Texto para turno de O
    def jugar_con_O(self):

        if hasattr(self, "mensaje_jugador_X"):
            self.mensaje_jugador_X.place_forget()

        self.emoji_o = self.emoji_O(texto="⭕", font_px=50)

        if not self.ganador_partida:

            self.mensaje_jugador_O = ctk.CTkLabel(master=self.raiz,
                        text="Es el turno de:", text_color="white", 
                        font=ctk.CTkFont(family='Cascadia Code', size=16, weight="bold"),
                        fg_color="#73AD75",
                        width=80, height=40,
                        corner_radius=200,
                        image=self.emoji_o,
                        compound="right"
                        )
            
            self.mensaje_jugador_O.place(x=110, y=360)

            self.boton_jugar.destroy()
            self.sale_O_de_inicio = True

    #Botón inicial de jugar
    def boton_jugar_inicio(self):

        if not self.ganador_partida:

            self.boton_jugar = ctk.CTkButton(master=self.raiz,
                        text="Jugar", text_color="white", 
                        font=ctk.CTkFont(family='Cascadia Code', size=16, weight="bold"),
                        fg_color="#73AD75", border_color="white",  border_width=2,
                        width=80, height=30,
                        hover_color="#6BC882",
                        command= lambda: random.choice([self.jugar_con_O, self.jugar_con_X])()
                        )
            
            self.boton_jugar.place(x=185, y=360)

    #Click sobre botones
    def click(self, boton):

        if boton.cget("text") == "" and not self.ganador_partida:
            
            if hasattr(self, "mensaje_jugador_O"):
                self.mensaje_jugador_O.place_forget()
            if hasattr(self, "mensaje_jugador_X"):
                self.mensaje_jugador_X.place_forget()

            if self.sale_X_de_inicio:
                boton.configure(text="❌", text_color="#785DC7")
                if not self.ganador_partida:
                    self.sale_X_de_inicio = False
                    self.jugar_con_O()

            elif self.sale_O_de_inicio:
                boton.configure(text="⭕", text_color="#F92F61")
                if not self.ganador_partida:
                    self.sale_O_de_inicio = False
                    self.jugar_con_X()

        self.ganador()
        self.reiniciar()

   #Se limpian todos los botones para volver a jugar 
    def limpiar_botones(self):

        self.boton_uno_primeraF.configure(text="")
        self.boton_dos_primeraF.configure(text="")
        self.boton_tres_primeraF.configure(text="")
        self.boton_cuatro_segundaF.configure(text="")
        self.boton_cinco_segundaF.configure(text="")
        self.boton_seis_segundaF.configure(text="")
        self.boton_siete_terceraF.configure(text="")
        self.boton_ocho_terceraF.configure(text="")
        self.boton_nueve_terceraF.configure(text="")
        
        self.ganador_partida = False
        #self.sale_O_de_inicio = False
        #self.sale_X_de_inicio = False

    #Reiniciar partida  
    def reiniciar(self):

        if (self.boton_uno_primeraF.cget("text") != "" and self.boton_dos_primeraF.cget("text") != "" and \
            self.boton_tres_primeraF.cget("text") != "" and self.boton_cuatro_segundaF.cget("text") != "" and \
            self.boton_cinco_segundaF.cget("text") != "" and self.boton_seis_segundaF.cget("text") != "" and \
            self.boton_siete_terceraF.cget("text") != "" and self.boton_ocho_terceraF.cget("text") != "" and \
            self.boton_nueve_terceraF.cget("text") != "" and not self.ganador_partida):

            self.boton_jugar.destroy()

            if hasattr(self, "mensaje_jugador_O"):
                self.mensaje_jugador_O.place_forget()
            if hasattr(self, "mensaje_jugador_X"):
                self.mensaje_jugador_X.place_forget()

            self.boton_reiniciar = ctk.CTkButton(master=self.raiz,
                    text="Reiniciar", text_color="white", 
                    font=ctk.CTkFont(family='Cascadia Code', size=16, weight="bold"),
                    fg_color="#C9C457", border_color="white",  border_width=2,
                    width=80, height=30,
                    hover_color="#6BC882",
                    command= self.reinciar_partida
                    )
            
            #self.boton_reiniciar.place(x=180, y=360)
            self.boton_reiniciar.place(x=180, y=370)


    #Ganador de la partida
    def ganador(self):

        if (self.boton_uno_primeraF.cget("text") == "❌" 
        and self.boton_dos_primeraF.cget("text") == "❌" 
        and self.boton_tres_primeraF.cget("text") == "❌") or \
        (self.boton_cuatro_segundaF.cget("text") == "❌" 
        and self.boton_cinco_segundaF.cget("text") == "❌" 
        and self.boton_seis_segundaF.cget("text") == "❌") or \
        (self.boton_siete_terceraF.cget("text") == "❌" 
        and self.boton_ocho_terceraF.cget("text") == "❌" 
        and self.boton_nueve_terceraF.cget("text") == "❌") or \
        (self.boton_uno_primeraF.cget("text") == "❌" 
        and self.boton_cuatro_segundaF.cget("text") == "❌" 
        and self.boton_siete_terceraF.cget("text") == "❌") or \
        (self.boton_dos_primeraF.cget("text") == "❌" 
        and self.boton_cinco_segundaF.cget("text") == "❌" 
        and self.boton_ocho_terceraF.cget("text") == "❌") or \
        (self.boton_tres_primeraF.cget("text") == "❌" 
        and self.boton_seis_segundaF.cget("text") == "❌" 
        and self.boton_nueve_terceraF.cget("text") == "❌") or \
        (self.boton_uno_primeraF.cget("text") == "❌" 
        and self.boton_cinco_segundaF.cget("text") == "❌" 
        and self.boton_nueve_terceraF.cget("text") == "❌") or \
        (self.boton_tres_primeraF.cget("text") == "❌" 
        and self.boton_cinco_segundaF.cget("text") == "❌" 
        and self.boton_siete_terceraF.cget("text") == "❌"):
            
            self.ganador_partida = True
            #self.boton_jugar.destroy()

            self.emoji_x = self.emoji_X(texto="❌", font_px=70, padding=15)

            self.texto_gana_X = ctk.CTkLabel(master=self.raiz, 
                                 text=" Ha ganado el jugador", image=self.emoji_x, compound="right",
                                 font=ctk.CTkFont(family="Cascadia Code", size=25, weight="bold",),
                                 text_color="white", fg_color="#C687D5", corner_radius=20,
                                 width=150, height=50)
            
            self.texto_gana_X.place(x=25, y=200)

            self.boton_uno_primeraF.configure(state=ctk.DISABLED)
            self.boton_dos_primeraF.configure(state=ctk.DISABLED)
            self.boton_tres_primeraF.configure(state=ctk.DISABLED)
            self.boton_cuatro_segundaF.configure(state=ctk.DISABLED)
            self.boton_cinco_segundaF.configure(state=ctk.DISABLED)
            self.boton_seis_segundaF.configure(state=ctk.DISABLED)
            self.boton_siete_terceraF.configure(state=ctk.DISABLED)
            self.boton_ocho_terceraF.configure(state=ctk.DISABLED)
            self.boton_nueve_terceraF.configure(state=ctk.DISABLED)

            if hasattr(self, "mensaje_jugador_O"):
                self.mensaje_jugador_O.place_forget()
            if hasattr(self, "mensaje_jugador_X"):
                self.mensaje_jugador_X.place_forget()

            self.boton_jugar_nuevo_X = ctk.CTkButton(master=self.raiz,
                    text="¿Jugar de nuevo?", text_color="white", 
                    font=ctk.CTkFont(family='Cascadia Code', size=18, weight="bold"),
                    fg_color="#00B91C", border_color="#FFFFFF", border_width=2,
                    width=80, height=40, corner_radius=30,
                    hover_color="#6BC882",
                    command= self.jugar_de_nuevo_ganando_X
                    )
            
            #self.boton_jugar_nuevo_X.place(x=117, y=360)
            self.boton_jugar_nuevo_X.place(x=117, y=390)


        elif (self.boton_uno_primeraF.cget("text") == "⭕" 
        and self.boton_dos_primeraF.cget("text") == "⭕" 
        and self.boton_tres_primeraF.cget("text") == "⭕") or \
        (self.boton_cuatro_segundaF.cget("text") == "⭕" 
        and self.boton_cinco_segundaF.cget("text") == "⭕" 
        and self.boton_seis_segundaF.cget("text") == "⭕") or \
        (self.boton_siete_terceraF.cget("text") == "⭕" 
        and self.boton_ocho_terceraF.cget("text") == "⭕" 
        and self.boton_nueve_terceraF.cget("text") == "⭕") or \
        (self.boton_uno_primeraF.cget("text") == "⭕" 
        and self.boton_cuatro_segundaF.cget("text") == "⭕" 
        and self.boton_siete_terceraF.cget("text") == "⭕") or \
        (self.boton_dos_primeraF.cget("text") == "⭕" 
        and self.boton_cinco_segundaF.cget("text") == "⭕" 
        and self.boton_ocho_terceraF.cget("text") == "⭕") or \
        (self.boton_tres_primeraF.cget("text") == "⭕" 
        and self.boton_seis_segundaF.cget("text") == "⭕" 
        and self.boton_nueve_terceraF.cget("text") == "⭕") or \
        (self.boton_uno_primeraF.cget("text") == "⭕" 
        and self.boton_cinco_segundaF.cget("text") == "⭕" 
        and self.boton_nueve_terceraF.cget("text") == "⭕") or \
        (self.boton_tres_primeraF.cget("text") == "⭕" 
        and self.boton_cinco_segundaF.cget("text") == "⭕" 
        and self.boton_siete_terceraF.cget("text") == "⭕"):
            
            self.ganador_partida = True

            self.emoji_o = self.emoji_O(texto="⭕", font_px=70, padding=15)

            self.texto_gana_O = ctk.CTkLabel(master=self.raiz,
                                 text=" Ha ganado el jugador", image=self.emoji_o, compound="right",
                                 font=ctk.CTkFont(family="Cascadia Code", size=25, weight="bold",),
                                 text_color="white", fg_color="#E97A7A", corner_radius=20,
                                 width=150, height=50)
            
            self.texto_gana_O.place(x=25, y=200)

            self.boton_uno_primeraF.configure(state=ctk.DISABLED)
            self.boton_dos_primeraF.configure(state=ctk.DISABLED)
            self.boton_tres_primeraF.configure(state=ctk.DISABLED)
            self.boton_cuatro_segundaF.configure(state=ctk.DISABLED)
            self.boton_cinco_segundaF.configure(state=ctk.DISABLED)
            self.boton_seis_segundaF.configure(state=ctk.DISABLED)
            self.boton_siete_terceraF.configure(state=ctk.DISABLED)
            self.boton_ocho_terceraF.configure(state=ctk.DISABLED)
            self.boton_nueve_terceraF.configure(state=ctk.DISABLED)

            if hasattr(self, "mensaje_jugador_O"):
                self.mensaje_jugador_O.place_forget()
            if hasattr(self, "mensaje_jugador_X"):
                self.mensaje_jugador_X.place_forget()

            self.boton_jugar_nuevo_O = ctk.CTkButton(master=self.raiz,
                    text="¿Jugar de nuevo?", text_color="white", 
                    font=ctk.CTkFont(family='Cascadia Code', size=18, weight="bold"),
                    fg_color="#00B91C", border_color="#FFFFFF", border_width=2,
                    width=80, height=40, corner_radius=30,
                    hover_color="#6BC882",
                    command= self.jugar_de_nuevo_ganando_O
                    )
            
            #self.boton_jugar_nuevo_O.place(x=117, y=360)
            self.boton_jugar_nuevo_O.place(x=117, y=390)

    def jugar_de_nuevo_ganando_X(self):

        self.texto_gana_X.destroy()
        self.limpiar_botones()
        self.boton_uno_primeraF.configure(state=ctk.NORMAL)
        self.boton_dos_primeraF.configure(state=ctk.NORMAL)
        self.boton_tres_primeraF.configure(state=ctk.NORMAL)
        self.boton_cuatro_segundaF.configure(state=ctk.NORMAL)
        self.boton_cinco_segundaF.configure(state=ctk.NORMAL)
        self.boton_seis_segundaF.configure(state=ctk.NORMAL)
        self.boton_siete_terceraF.configure(state=ctk.NORMAL)
        self.boton_ocho_terceraF.configure(state=ctk.NORMAL)
        self.boton_nueve_terceraF.configure(state=ctk.NORMAL)
        random.choice([self.jugar_con_O, self.jugar_con_X])()

        self.boton_jugar_nuevo_X.place_forget()


    def jugar_de_nuevo_ganando_O(self):
    
        self.texto_gana_O.destroy()
        self.limpiar_botones()
        self.boton_uno_primeraF.configure(state=ctk.NORMAL)
        self.boton_dos_primeraF.configure(state=ctk.NORMAL)
        self.boton_tres_primeraF.configure(state=ctk.NORMAL)
        self.boton_cuatro_segundaF.configure(state=ctk.NORMAL)
        self.boton_cinco_segundaF.configure(state=ctk.NORMAL)
        self.boton_seis_segundaF.configure(state=ctk.NORMAL)
        self.boton_siete_terceraF.configure(state=ctk.NORMAL)
        self.boton_ocho_terceraF.configure(state=ctk.NORMAL)
        self.boton_nueve_terceraF.configure(state=ctk.NORMAL)
        random.choice([self.jugar_con_O, self.jugar_con_X])()

        self.boton_jugar_nuevo_O.place_forget()

    def reinciar_partida(self):

        self.limpiar_botones()
        random.choice([self.jugar_con_O, self.jugar_con_X])()
        
        self.boton_reiniciar.place_forget()


#no sé aún explicar muy bien su funcionamiento, pero nos sirve para que se ejecute la clase como programa principal
#(llamando a las funciones correspondientes cómo se puede ver)
if __name__ == "__main__":

    juego = tres_en_raya()

    juego.Label_principal()
    juego.botones()
    juego.boton_jugar_inicio()
    #juego.click()
    juego.raiz.mainloop()
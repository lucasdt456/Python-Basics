from tkinter import *
import math

#Raiz y Frame
miRaiz=Tk()
miRaiz.title("Calculadora")
miRaiz.resizable(False,False)
#miRaiz.geometry("500x500")

miFrame=Frame(bg="#292929")
miFrame.pack(fill="both", expand=True)

class Calculadora:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operacion = ""
        self.resultado = 0
        self.operador = False
        self.reset_pantalla = False

    def clickNumero(self, num):

        actual=numeroPantalla.get()

        if self.reset_pantalla:
            operacionPantalla.set("")
            numeroPantalla.set(num)
            self.reset_pantalla = False
            self.operador = False
            self.operacion = ""

        else:
            if actual == "0":
                numeroPantalla.set(num)
            else:
                numeroPantalla.set(actual + num)

    def borrarTodo(self):

        numeroPantalla.set("0")
        operacionPantalla.set("")
        self.num1=0
        self.num2=0
        self.resultado=0
        self.operacion=""
        self.operador=False

    def borrarNumero(self):

        actual = numeroPantalla.get()

        if actual == "ERROR" or "DESBORDADO":
            numeroPantalla.set("0")
            operacionPantalla.set("")
            self.num1 = 0
            self.num2 = 0
            self.resultado = 0
            self.operacion = ""
            self.operador = False

        if self.operacion != "" :
            if len(actual) > 1:
                numeroPantalla.set(actual[:-1])
            else:
                numeroPantalla.set("0")

        else:
            if len(actual) > 1:
                self.operacion = ""
                self.operador = False
                operacionPantalla.set("")
            else:
                self.operacion = ""
                self.operador = False
                operacionPantalla.set("")

    def clickComa(self, coma):

        actual = numeroPantalla.get()

        if "." in actual:
            return
            #nada
        else:
            numeroPantalla.set(actual + coma)

    def suma(self):

        if not self.operador:
            if self.operacion == "sumar":
                try:
                    self.num2 = float(numeroPantalla.get())

                except ValueError:
                    self.num2 = 0

                except OverflowError:
                    operacionPantalla.set("")
                    numeroPantalla.set("DESBORDADO")
                    self.reset_pantalla = True
                    self.operador = True

                self.resultado = self.num1 + self.num2
                self.num1 = self.resultado
                numeroPantalla.set(str(self.resultado))
                operacionPantalla.set(str(self.num1) + " +")
                self.operador = True
                self.reset_pantalla = True
                self.operacion = ""

            else:
                try:
                    self.num1 = float(numeroPantalla.get())
                    operacionPantalla.set(str(self.num1) + " +")
                    actual = numeroPantalla.get()
                    #self.operador = True

                    if actual != "":
                        numeroPantalla.set("")

                except ValueError:
                    self.num1 = 0

        self.operacion = "sumar"

    def resta(self):

        if not self.operador:
            if self.operacion == "resta":
                try:
                    self.num2 = float(numeroPantalla.get())

                except ValueError:
                    self.num2 = 0

                except OverflowError:
                    operacionPantalla.set("")
                    numeroPantalla.set("DESBORDADO")
                    self.reset_pantalla = True
                    self.operador = True

                self.resultado = self.num1 - self.num2
                self.num1 = self.resultado
                numeroPantalla.set(str(self.resultado))
                operacionPantalla.set(str(self.num1) + " -")
                self.operador = True
                self.reset_pantalla = True

            else:
                try:
                    self.num1 = float(numeroPantalla.get())
                    operacionPantalla.set(str(self.num1) + " -")
                    actual = numeroPantalla.get()
                    # self.operador = True

                    if actual != "":
                        numeroPantalla.set("")

                except ValueError:
                    self.num1 = 0

        self.operacion = "resta"

    def multi(self):

        if not self.operador:
            if self.operacion == "multi":
                try:
                    self.num2 = float(numeroPantalla.get())

                except ValueError:
                    self.num2 = 0

                except OverflowError:
                    operacionPantalla.set("")
                    numeroPantalla.set("DESBORDADO")
                    self.reset_pantalla = True
                    self.operador = True

                self.resultado = self.num1 * self.num2
                self.num1 = self.resultado
                numeroPantalla.set(str(self.resultado))
                operacionPantalla.set(str(self.num1) + " x")
                self.operador = True
                self.reset_pantalla = True

            else:
                try:
                    self.num1 = float(numeroPantalla.get())
                    operacionPantalla.set(str(self.num1) + " x")
                    actual = numeroPantalla.get()
                    # self.operador = True

                    if actual != "":
                        numeroPantalla.set("")

                except ValueError:
                    self.num1 = 0

        self.operacion = "multi"

    def div(self):

        if not self.operador:
            if self.operacion == "div":
                try:
                    self.num2 = float(numeroPantalla.get())

                except ValueError:
                    self.num2 = 0

                except OverflowError:
                    operacionPantalla.set("")
                    numeroPantalla.set("DESBORDADO")
                    self.reset_pantalla = True
                    self.operador = True

                except ZeroDivisionError:
                    operacionPantalla.set("")
                    numeroPantalla.set("ERROR")
                    self.reset_pantalla = True
                    self.operador = True

                self.resultado = self.num1 / self.num2
                self.num1 = self.resultado
                numeroPantalla.set(str(self.resultado))
                operacionPantalla.set(str(self.num1) + " ÷")
                self.operador = True
                self.reset_pantalla = True

            else:
                try:
                    self.num1 = float(numeroPantalla.get())
                    operacionPantalla.set(str(self.num1) + " ÷")
                    actual = numeroPantalla.get()
                    # self.operador = True

                    if actual != "":
                        numeroPantalla.set("")

                except ValueError:
                    self.num1 = 0

        self.operacion = "div"

    def porcentaje(self):

        if not self.operador:
            if self.operacion == "porcen":
                try:
                    self.num2 = float(numeroPantalla.get())

                except ValueError:
                    self.num2 = 0

                except OverflowError:
                    operacionPantalla.set("")
                    numeroPantalla.set("DESBORDADO")
                    self.reset_pantalla = True
                    self.operador = True

                self.resultado = self.num1 * 0.01
                self.num1 = self.resultado
                numeroPantalla.set(str(self.resultado))
                operacionPantalla.set(str(self.num1) + " %")
                self.operador = True
                self.reset_pantalla = True

            else:
                try:
                    self.num1 = float(numeroPantalla.get())
                    operacionPantalla.set(str(self.num1) + " %")
                    actual = numeroPantalla.get()
                    # self.operador = True

                    if actual != "":
                        numeroPantalla.set("")

                except ValueError:
                    self.num1 = 0

        self.operacion = "porcen"

    def elevado_cuadrado(self):

             try:
                self.num1 = float(numeroPantalla.get())
                operacionPantalla.set(f" sqr({self.num1})")
                self.resultado = self.num1 ** 2
                self.num1 = self.resultado
                numeroPantalla.set(str(self.resultado))
                self.operador = True
                self.reset_pantalla = True
                self.operacion = "elevado"

             except ValueError:
                self.num1 = 0

             except OverflowError:
                operacionPantalla.set("")
                numeroPantalla.set("DESBORDADO")
                self.reset_pantalla = True
                self.operador = True

    def raiz_cuadrada(self):

             try:
                self.num1 = float(numeroPantalla.get())
                operacionPantalla.set(f" √({self.num1})")
                self.resultado = math.sqrt(self.num1)
                self.num1 = self.resultado
                numeroPantalla.set(str(self.resultado))
                self.operador = True
                self.reset_pantalla = True
                self.operacion = "raiz"

             except ValueError:
                self.num1 = 0

             except OverflowError:
                operacionPantalla.set("")
                numeroPantalla.set("DESBORDADO")
                self.reset_pantalla = True
                self.operador = True

    def uno_partido_x(self):

             try:
                self.num1 = float(numeroPantalla.get())
                operacionPantalla.set(f" 1/({self.num1})")
                self.resultado = 1/(self.num1)
                self.num1 = self.resultado
                numeroPantalla.set(str(self.resultado))
                self.operador = True
                self.reset_pantalla = True
                self.operacion = "uno_partido"

             except ValueError:
                self.num1 = 0

             except OverflowError:
                operacionPantalla.set("")
                numeroPantalla.set("DESBORDADO")
                self.reset_pantalla = True
                self.operador = True

             except ZeroDivisionError:
                operacionPantalla.set("")
                numeroPantalla.set("ERROR")
                self.reset_pantalla = True
                self.operador = True


    def igual(self):
        
        if self.operacion == "sumar_dos" and self.num1 != 0:
                self.resultado = float(self.num1) + float(self.num2)
                operacionPantalla.set(f" {float(self.num1)} + {float(self.num2)} =")
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.num1 = self.resultado
                self.reset_pantalla = True

        elif self.operacion == "restar_dos":
                self.resultado = float(self.num1) - float(self.num2)
                operacionPantalla.set(f" {float(self.num1)} - {float(self.num2)} =")
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.num1 = self.resultado
                self.reset_pantalla = True

        elif self.operacion == "multi_dos" and self.num1 != 0:
                self.resultado = float(self.num1) * float(self.num2)
                operacionPantalla.set(f" {float(self.num1)} x {float(self.num2)} =")
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.num1 = self.resultado
                self.reset_pantalla = True

        elif self.operacion == "div_dos" and self.num1 != 0:
            try:
                self.resultado = float(self.num1) / float(self.num2)
                operacionPantalla.set(f" {float(self.num1)} ÷ {float(self.num2)} =")
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.num1 = self.resultado
                self.reset_pantalla = True

            except ZeroDivisionError:
                operacionPantalla.set("")
                numeroPantalla.set("ERROR")
                self.reset_pantalla = True
                self.operador = True

        elif self.operacion == "porcen_dos" and self.num1 != 0:
                self.resultado = float(self.num1) * 0.01
                operacionPantalla.set(f" {float(self.num1)} % =")
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.num1 = self.resultado
                self.reset_pantalla = True

        elif self.operacion == "elevado_dos" and self.num1 != 0:
                self.resultado = float(self.num1) ** 2
                operacionPantalla.set(f" sqr({float(self.num1)}) ")
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.num1 = self.resultado
                self.reset_pantalla = True

        elif self.operacion == "raiz_dos" and self.num1 != 0:
                self.resultado = float(self.num1)
                operacionPantalla.set(f" √({float(self.num1)}) ")
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.num1 = self.resultado
                self.reset_pantalla = True

        elif self.operacion == "uno_partido_dos" and self.num1 != 0:
            try:
                self.resultado = float(self.num1)
                operacionPantalla.set(f" 1/({float(self.num1)}) ")
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.num1 = self.resultado
                self.reset_pantalla = True

            except ZeroDivisionError:
                operacionPantalla.set("")
                numeroPantalla.set("ERROR")
                self.reset_pantalla = True
                self.operador = True

        else:
            try:
                self.num2 = float(numeroPantalla.get())

            except ValueError:
                self.num2 = 0

            if self.operacion == "sumar":
                self.resultado = float(self.num1) + float(self.num2)
                operacionPantalla.set(f" {float(self.num1)} + {float(self.num2)} =")
                self.num1 = self.resultado
                self.operacion="sumar_dos"
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.reset_pantalla = True

            elif self.operacion == "resta":
                self.resultado = float(self.num1) - float(self.num2)
                operacionPantalla.set(f"{self.num1} - {self.num2} =")
                self.num1 = self.resultado
                self.operacion="restar_dos"
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.reset_pantalla = True

            elif self.operacion == "multi":
                self.resultado = float(self.num1) * float(self.num2)
                operacionPantalla.set(f"{self.num1} x {self.num2} =")
                self.num1 = self.resultado
                self.operacion="multi_dos"
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.reset_pantalla = True

            elif self.operacion == "div":
                try:
                    self.resultado = float(self.num1) / float(self.num2)
                    operacionPantalla.set(f"{self.num1} ÷ {self.num2} =")
                    self.num1 = self.resultado
                    self.operacion="div_dos"
                    numeroPantalla.set(f" {self.resultado:.2f}" )
                    self.reset_pantalla = True

                except ZeroDivisionError:
                    operacionPantalla.set("")
                    numeroPantalla.set("ERROR")
                    self.reset_pantalla = True
                    self.operador = True

            elif self.operacion == "porcen":
                self.resultado = float(self.num1) * 0.01
                operacionPantalla.set(f"{self.num1} % =")
                self.num1 = self.resultado
                self.operacion="porcen_dos"
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.reset_pantalla = True

            elif self.operacion == "elevado":
                self.resultado = float(self.num1) ** 2
                operacionPantalla.set(f"sqr({self.num1})")
                self.num1 = self.resultado
                self.operacion="elevado_dos"
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.reset_pantalla = True

            elif self.operacion == "raiz":
                self.resultado = math.sqrt(float(self.num1))
                operacionPantalla.set(f"√({self.num1})")
                self.num1 = self.resultado
                self.operacion="raiz_dos"
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.reset_pantalla = True

            elif self.operacion == "uno_partido":
                self.resultado = 1/(float(self.num1))
                operacionPantalla.set(f"1/({self.num1})")
                self.num1 = self.resultado
                self.operacion="uno_partido_dos"
                numeroPantalla.set(f" {self.resultado:.2f}" )
                self.reset_pantalla = True

    def mas_menos(self):

        actual=numeroPantalla.get()

        try:
            valor = float(actual)
            valor = -valor
            resultado = float(valor)
            numeroPantalla.set(f"{resultado}")
        except ValueError:
            numeroPantalla.set("0")

#Cuadro de texto
numeroPantalla=StringVar()
numeroPantalla.set("0")

operacionPantalla=StringVar()
operacionPantalla.set("")

miCalculadora = Calculadora()

cuadroTexto=Entry(miFrame,bg="#292929",fg="white",justify="right",textvariable=numeroPantalla, width=20, font=("Arial", 18))
cuadroTexto.grid(row=1,column=1,padx=4,pady=4,columnspan=4)

cuadroTexto2=Entry(miFrame, bg="#292929",fg="white",justify="right",textvariable=operacionPantalla, width=20, font=("Arial", 18))
cuadroTexto2.grid(row=0,column=1,padx=4,pady=4,columnspan=4)

#cuadroTexto.insert(0,"0")

#Primera fila (%,CE,C,→)
def accion_porcentaje():
    miCalculadora.porcentaje()

botonPorcentaje=Button(miFrame, bg="#3D3D3D", fg="white", text="%", width=5, font=("Arial", 14), command=accion_porcentaje)
botonPorcentaje.grid(row=2, column=1, padx=1)

#funcion 'wrapped' borrarTodo
def accion_borrarTodo():
    miCalculadora.borrarTodo()

botonCE=Button(miFrame, bg="#3D3D3D", fg="white", text="CE", width=5, font=("Arial", 14), command=accion_borrarTodo)
botonCE.grid(row=2, column=2, padx=1)

botonC=Button(miFrame, bg="#3D3D3D", fg="white", text="C", width=5, font=("Arial", 14), command=accion_borrarTodo)
botonC.grid(row=2, column=3, padx=1)

botonBorrar=Button(miFrame, bg="#3D3D3D", fg="white", text="→", width=5, font=("Arial", 14), command=lambda:miCalculadora.borrarNumero())
botonBorrar.grid(row=2, column=4, padx=1)

#Segunda fila (1/x,x²,√x,÷)
def accion_uno_partido_x():
    miCalculadora.uno_partido_x()

boton_uno_partidoX=Button(miFrame, bg="#3D3D3D", fg="white", text="1/x", width=5, font=("Arial", 14), command=accion_uno_partido_x)
boton_uno_partidoX.grid(row=3, column=1, padx=1)

def accion_elevado():
    miCalculadora.elevado_cuadrado()

botonCuadrado=Button(miFrame, bg="#3D3D3D", fg="white", text="x²", width=5, font=("Arial", 14), command=accion_elevado)
botonCuadrado.grid(row=3, column=2, padx=1)

def accion_raiz_cuadrada():
    miCalculadora.raiz_cuadrada()

botonRaiz=Button(miFrame, bg="#3D3D3D", fg="white", text="√x", width=5, font=("Arial", 14), command=accion_raiz_cuadrada)
botonRaiz.grid(row=3, column=3, padx=1)

def accion_div():
    miCalculadora.div()

botonDividir=Button(miFrame, bg="#3D3D3D", fg="white", text="÷", width=5, font=("Arial", 14), command=accion_div)
botonDividir.grid(row=3, column=4, padx=1)

#Tercera fila (7,8,9,x)
boton7=Button(miFrame, bg="#595959", fg="white", text="7", width=5, font=("Arial", 14), command=lambda:miCalculadora.clickNumero("7"))
boton7.grid(row=4, column=1, padx=1)

boton8=Button(miFrame, bg="#595959", fg="white", text="8", width=5, font=("Arial", 14), command=lambda:miCalculadora.clickNumero("8"))
boton8.grid(row=4, column=2, padx=1)

boton9=Button(miFrame, bg="#595959", fg="white", text="9", width=5, font=("Arial", 14), command=lambda:miCalculadora.clickNumero("9"))
boton9.grid(row=4, column=3, padx=1)

def accion_multi():
    miCalculadora.multi()

botonMulti=Button(miFrame, bg="#3D3D3D", fg="white", text="x", width=5, font=("Arial", 14), command=accion_multi)
botonMulti.grid(row=4, column=4, padx=1)

#Cuarta fila (4,5,6,-)
boton4=Button(miFrame, bg="#595959", fg="white", text="4", width=5, font=("Arial", 14), command=lambda:miCalculadora.clickNumero("4"))
boton4.grid(row=5, column=1, padx=1)

boton5=Button(miFrame, bg="#595959", fg="white", text="5", width=5, font=("Arial", 14), command=lambda:miCalculadora.clickNumero("5"))
boton5.grid(row=5, column=2, padx=1)

boton6=Button(miFrame, bg="#595959", fg="white", text="6", width=5, font=("Arial", 14), command=lambda:miCalculadora.clickNumero("6"))
boton6.grid(row=5, column=3, padx=1)

def accion_restar():
    miCalculadora.resta()

botonMenos=Button(miFrame, bg="#3D3D3D", fg="white", text="-", width=5, font=("Arial", 14), command=accion_restar)
botonMenos.grid(row=5, column=4, padx=1)

#Quinta fila (1,2,3,+)
boton1=Button(miFrame, bg="#595959", fg="white", text="1", width=5, font=("Arial", 14), command=lambda:miCalculadora.clickNumero("1"))
boton1.grid(row=6, column=1, padx=1)

boton2=Button(miFrame, bg="#595959", fg="white", text="2", width=5, font=("Arial", 14), command=lambda:miCalculadora.clickNumero("2"))
boton2.grid(row=6, column=2, padx=1)

boton3=Button(miFrame, bg="#595959", fg="white", text="3", width=5, font=("Arial", 14), command=lambda:miCalculadora.clickNumero("3"))
boton3.grid(row=6, column=3, padx=1)

def accion_sumar():
    miCalculadora.suma()

botonMas=Button(miFrame, bg="#3D3D3D", fg="white", text="+", width=5, font=("Arial", 14) ,command=accion_sumar)
botonMas.grid(row=6, column=4, padx=1)

#Quinta fila (±,0, ',' ,=)

def accion_mas_menos():
    miCalculadora.mas_menos()

botonMasMenos=Button(miFrame, bg="#595959", fg="white", text="±",width=5, font=("Arial", 14), command=accion_mas_menos)
botonMasMenos.grid(row=7, column=1, padx=1)

boton0=Button(miFrame, bg="#595959", fg="white", text="0", width=5, command=lambda:miCalculadora.clickNumero("0"), font=("Arial", 14))
boton0.grid(row=7, column=2, padx=1)

botonComa=Button(miFrame, bg="#595959", fg="white", text=",", width=5, command=lambda:miCalculadora.clickComa("."), font=("Arial", 14))
botonComa.grid(row=7, column=3, padx=1)

botonIgual=Button(miFrame, bg="#7AB9BC", fg="black", text="=", width=5, font=("Arial", 14), command=lambda:miCalculadora.igual())
botonIgual.grid(row=7, column=4, padx=1)

miRaiz.mainloop()
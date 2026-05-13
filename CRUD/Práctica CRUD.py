from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
import sqlite3

raiz=Tk()
barra_menu=Menu(raiz)

raiz.config(menu=barra_menu)
raiz.title("PRÁCTICA CRUD")
raiz.iconbitmap("python_ico.ico")
raiz.geometry("300x300")

frame_textos=Frame(raiz)
frame_textos.pack()

#---FUNCIONES PARTE LÓGICA---
#---CREAR BBDD---
def conexion_con_BBDD():

    crear = messagebox.askyesno(
        title="Crear",
        message="¿Desea crear una Base de Datos?",
        icon="question"
    )

    if crear:
        conexion_BBDD = sqlite3.connect("Usuarios")

        cursor_BBDD = conexion_BBDD.cursor()
        try:
            cursor_BBDD.execute("""
            CREATE TABLE DATOS_USUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(100),
            DIRECCION VARCHAR(100),
            COMENTARIOS VARCHAR(1000)
            )
            """)

            messagebox.showinfo("Base de datos creándose...",
                                "La base de datos ha sido creada con éxito :U")

        except:
            messagebox.showwarning("!Atención¡",
                                   "La base de datos ya ha sido creada...")
#------

#---BORRAR CAMPOS INSERTADOS---
def funcion_borrar_campos():
    borrar = messagebox.askyesno(
        "Borrar datos",
        "¿Desea borrar los datos insertados?",
        icon="warning"
    )

    if borrar:
        ID_ingreso.set("")
        nombre_ingreso.set("")
        password_ingreso.set("")
        direccion_ingreso.set("")
        texto_comentarios.delete(1.0, END)

        messagebox.showwarning("Datos insertados eliminados",
                           "Se han borrado todos los campos")

#---CERRAR PROGRAMA---
def funcion_BBDD_cerrar():
    cerrar = messagebox.askokcancel("Salir", "¿Desea salir del programa?")

    if cerrar:
        raiz.destroy()
#------

#---CRUD barra---
#---CREAR---
def funcion_crear_usuario_BBDD():
    crear = messagebox.askyesno(
        "Crear Usuario en BBDD",
        "¿Desea crear un usuario en la BBDD?",
        icon="question"
    )

    if crear:
        conexion_BBDD = sqlite3.connect("Usuarios")

        cursor_BBDD = conexion_BBDD.cursor()

        """cursor_BBDD.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, '" + nombre_ingreso.get() +
                            "','" + password_ingreso.get() +
                            "','" + direccion_ingreso.get() +
                            "','" + texto_comentarios.get("1.0", END) + "')")"""
        datos_ingresar = nombre_ingreso.get(), password_ingreso.get(), direccion_ingreso.get(), texto_comentarios.get("1.0", END)

        cursor_BBDD.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,?,?,?,?)",(datos_ingresar))
        #mas sencill, inserción de datos de forma paramétrica

        conexion_BBDD.commit()

        messagebox.showinfo("Usuario creado", "Se ha creado el usuario de forma correcta")
#------

#---LEER---
def funcion_leer_usuario_BBDD():
    leer = messagebox.askyesno(
        "Leer Usuario en BBDD",
        "¿Desea leer la información de un usuario en la BBDD?",
        icon="question"
    )

    if leer:
        conexion_BBDD = sqlite3.connect("Usuarios")

        cursor_BBDD = conexion_BBDD.cursor()

        cursor_BBDD.execute("SELECT * FROM DATOS_USUARIOS WHERE ID=" + str(ID_ingreso.get()))

        leer_usuario = cursor_BBDD.fetchall()

        for usuario in leer_usuario:

            ID_ingreso.set(usuario[0])
            nombre_ingreso.set(usuario[1])
            password_ingreso.set(usuario[2])
            direccion_ingreso.set(usuario[3])
            texto_comentarios.insert(1.0, usuario[4])

        conexion_BBDD.commit()
#------

#---ACTUALIZAR---
def funcion_actualizar_usuario_BBDD():
    actualizar = messagebox.askyesno(
        "Actualizar Usuario en BBDD",
        "¿Desea actualizar la información de un usuario en la BBDD?",
        icon="question"
    )

    if actualizar:
        conexion_BBDD = sqlite3.connect("Usuarios")

        cursor_BBDD = conexion_BBDD.cursor()

        """cursor_BBDD.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO='" + nombre_ingreso.get() +
                            "', PASSWORD='" + password_ingreso.get() +
                            "', DIRECCION='" + direccion_ingreso.get() +
                            "', COMENTARIOS='" + texto_comentarios.get("1.0", END) +
                            "' WHERE ID=" + str(ID_ingreso.get()))"""

        datos_ingresar = nombre_ingreso.get(), password_ingreso.get(), direccion_ingreso.get(), texto_comentarios.get("1.0", END)

        cursor_BBDD.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, DIRECCION=?, COMENTARIOS=?" +
                            "WHERE ID="+ str(ID_ingreso.get()), datos_ingresar)

        conexion_BBDD.commit()

        messagebox.showinfo("Usuario actualizado", "El usuario se ha actualizad correctamente")
#------

#---ELIMINAR---
def funcion_eliminar_usuario_BBDD():
    eliminar = messagebox.askyesno(
        "Eliminar Usuario en BBDD",
        "¿Desea eliminar un usuario en la BBDD?",
        icon="question"
    )

    if eliminar:
        conexion_BBDD = sqlite3.connect("Usuarios")

        cursor_BBDD = conexion_BBDD.cursor()

        cursor_BBDD.execute("DELETE FROM DATOS_USUARIOS WHERE ID=" + str(ID_ingreso.get()))

        conexion_BBDD.commit()

        messagebox.showinfo("Usuario eliminado", "El usuario ha sido eliminado correctamente")

        ID_ingreso.set("")
        nombre_ingreso.set("")
        password_ingreso.set("")
        direccion_ingreso.set("")
        texto_comentarios.delete(1.0, END)
#------

#---BBDD---
BBDD_menu=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="BBDD", menu=BBDD_menu)
BBDD_menu.add_command(label="Crear", command=conexion_con_BBDD)
BBDD_menu.add_command(label="Salir", command=funcion_BBDD_cerrar)
#------

#---BORRAR---
Borrar_menu=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Borrar", menu=Borrar_menu)
Borrar_menu.add_command(label="Borrar campos", command=funcion_borrar_campos)
#------



#---CRUD---
CRUD_menu=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="CRUD", menu=CRUD_menu)
CRUD_menu.add_command(label="Crear", command=funcion_crear_usuario_BBDD)
CRUD_menu.add_command(label="Leer", command=funcion_leer_usuario_BBDD)
CRUD_menu.add_command(label="Actualizar", command=funcion_actualizar_usuario_BBDD)
CRUD_menu.add_separator()
CRUD_menu.add_command(label="Eliminar", command=funcion_eliminar_usuario_BBDD)
#------

#---AYUDA---
def licencia():
    licencia_mensaje = messagebox.showwarning(
        "Licencia de programa",
        "Actualmente sin licencia..."
    )

def acerca_del_programa():
    ventana = Toplevel(raiz)
    ventana.title("Acerca del programa")
    ventana.geometry("200x130")
    ventana.resizable(False, False)
    Label(ventana,
          text="Este programa ejecuta un CRUD:\nCreate\nRead\nUpdate\nDelate"
               "\nEnviándolo a una BD de DB Browser",
          justify="center").pack()

    Button(ventana,
           text="Cerrar",
           command=ventana.destroy).pack()


AYUDA_menu=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=AYUDA_menu)
AYUDA_menu.add_command(label="Licencia", command=licencia)
AYUDA_menu.add_separator()
AYUDA_menu.add_command(label="Acerca de...", command=acerca_del_programa)

#---LABEL & ENTRY de TEXTOS y DATOS a INGRESAR---
#---ID---
ID_label=Label(frame_textos,
               text="ID:")
ID_label.grid(row=0,
              column=0,
              padx=5, pady=10)

ID_ingreso=IntVar()
ID_ingreso.set("")
texto_ID=Entry(frame_textos,
               fg="gray",
               textvariable=ID_ingreso)
texto_ID.grid(row=0,
              column=1,
              padx=5, pady=10)

#---NOMBRE---
nombre_label=Label(frame_textos,
               text="NOMBRE:")
nombre_label.grid(row=2,
              column=0,
              padx=5, pady=10)

nombre_ingreso=StringVar()
texto_nombre=Entry(frame_textos,
               fg="black",
               textvariable=nombre_ingreso)
texto_nombre.grid(row=2,
              column=1,
              padx=5, pady=10)


#---PASSWORD---
password_label=Label(frame_textos,
               text="PASSWORD:")
password_label.grid(row=3,
              column=0,
              padx=5, pady=10)

password_ingreso=StringVar()
texto_password=Entry(frame_textos,
               fg="black",
               show="*",
               textvariable=password_ingreso)
texto_password.grid(row=3,
              column=1,
              padx=5, pady=10)

#---DIRECCION---
direccion_label=Label(frame_textos,
               text="DIRECCION:")
direccion_label.grid(row=4,
              column=0,
              padx=5, pady=10)

direccion_ingreso=StringVar()
texto_direccion=Entry(frame_textos,
               fg="black",
               textvariable=direccion_ingreso)
texto_direccion.grid(row=4,
              column=1,
              padx=5, pady=10)

#---COMENTARIOS---
comentarios_label=Label(frame_textos,
               text="COMENTARIOS:")
comentarios_label.grid(row=5,
              column=0,
              padx=5, pady=10)

texto_comentarios=Text(frame_textos,
                       width=20,
                       height=5,
                       fg="black")
texto_comentarios.grid(row=5,
              column=1,
              padx=5, pady=10)

barra_scroll=Scrollbar(frame_textos,
                       command=texto_comentarios.yview)
barra_scroll.grid(row=5,
                  column=2,
                  sticky="nsew")
texto_comentarios.config(yscrollcommand=barra_scroll.set)
#------

#---BOTONES CRUD---
frame_botones=Frame(raiz)
frame_botones.pack()

#---CREAR---
boton_crear=Button(frame_botones,
                   text="Crear",
                   command=funcion_crear_usuario_BBDD)
boton_crear.grid(row=6, column=0, padx=5)

#---LEER---
boton_leer=Button(frame_botones,
                   text="Leer",
                  command=funcion_leer_usuario_BBDD)
boton_leer.grid(row=6, column=1, padx=5)

#---ACTUALIZAR---
boton_actualizar=Button(frame_botones,
                   text="Actualizar",
                   command=funcion_actualizar_usuario_BBDD)
boton_actualizar.grid(row=6, column=2, padx=5)

#---ELIMINAR---
boton_eliminar=Button(frame_botones,
                   text="Eliminar",
                   command=funcion_eliminar_usuario_BBDD)
boton_eliminar.grid(row=6, column=3, padx=5)

raiz.mainloop()

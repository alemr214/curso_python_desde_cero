from pydoc import importfile
from tkinter import *
from tkinter import messagebox
import sqlite3

from regex import D


# Conexion a la BBDD
conexion = sqlite3.connect("basedatos1.db")
miCursor = conexion.cursor()

# Funciones basicas


def conexionBD():
    try:
        miCursor.execute("""CREATE TABLE DatosUsuario(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR(50),
        APELLIDO VARCHAR(50),
        PASSWORD VARCHAR(50), 
        DIRECCION VARCHAR(50))""")
        messagebox.showinfo("BBDD", "La BBDD se ha creado correctamente")
    except:
        messagebox.showwarning("BBDD", "Error al crear la BBDD")


def crear():
    miCursor.execute("INSERT INTO DatosUsuario VALUES(NULL, '" + displayNombre.get() +
                     "', '" + displayApellido.get() + "', '" + displayPassword.get() + "', '" + displayDireccion.get() + "')")
    conexion.commit()
    messagebox.showinfo("BBDD", "El registro se ha creado correctamente")


def leer():
    miCursor.execute(
        "SELECT * FROM DatosUsuario WHERE ID = " + displayID.get())
    usuario = miCursor.fetchall()
    for datos in usuario:
        displayNombre.set(datos[1])
        displayApellido.set(datos[2])
        displayPassword.set(datos[3])
        displayDireccion.set(datos[4])


def actualizar():
    miCursor.execute("UPDATE DatosUsuario SET NOMBRE_USUARIO = '" + displayNombre.get() +
                     "', APELLIDO = '" + displayApellido.get() + "', PASSWORD = '" + displayPassword.get() +
                     "', DIRECCION = '" + displayDireccion.get() + "' WHERE ID = " + displayID.get())
    conexion.commit()
    messagebox.showinfo("BBDD", "El registro se ha actualizado correctamente")


def borrar():
    miCursor.execute("DELETE FROM DatosUsuario WHERE ID = " + displayID.get())
    conexion.commit()
    messagebox.showinfo("BBDD", "El registro se ha borrado correctamente")


def salirApp():
    salida = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if salida == "yes":
        root.destroy()


def limpiarCampos():
    displayID.set("")
    displayNombre.set("")
    displayApellido.set("")
    displayPassword.set("")
    displayDireccion.set("")


# Creamos la ventana principal
root = Tk()
root.title("Practica")
frame = Frame(root)
frame.pack()

# Variables de entrada
displayID = StringVar()
displayNombre = StringVar()
displayApellido = StringVar()
displayPassword = StringVar()
displayDireccion = StringVar()

# Creando la barra de menu y estableciendola
menuBar = Menu(root)
root.config(menu=menuBar)

# Estableciendo las secciones del menu
bbddSection = Menu(menuBar, tearoff=0)
borrarSection = Menu(menuBar, tearoff=0)
crudSection = Menu(menuBar, tearoff=0)
ayudaSection = Menu(menuBar, tearoff=0)

# Agregando las secciones al menu
menuBar.add_cascade(label='BBDD', menu=bbddSection)
menuBar.add_cascade(label='Borrar', menu=borrarSection)
menuBar.add_cascade(label='CRUD', menu=crudSection)
menuBar.add_cascade(label='Ayuda', menu=ayudaSection)

# Estableciendo las opciones a las secciones
bbddSection.add_command(label="Conectar", command=conexionBD)
bbddSection.add_command(label="Salir", command=salirApp)

borrarSection.add_command(label="Borrar campos", command=limpiarCampos)

crudSection.add_command(label="Crear", command=crear)
crudSection.add_command(label="Leer", command=leer)
crudSection.add_command(label="Actualizar", command=actualizar)
crudSection.add_command(label="Borrar", command=borrar)

ayudaSection.add_command(label="Licencia")
ayudaSection.add_command(label="Acerca de...")

# Establecemos los labels y los entrys
labelID = Label(frame, text="ID:")
labelNombre = Label(frame, text="Nombre:")
labelApellido = Label(frame, text="Apellido:")
labelPassword = Label(frame, text="Password:")
labelDireccion = Label(frame, text="Direccion:")

entryID = Entry(frame, textvariable=displayID)
entryNombre = Entry(frame, textvariable=displayNombre)
entryApellido = Entry(frame, textvariable=displayApellido)
entryPassword = Entry(frame, show="*", textvariable=displayPassword)
entryDireccion = Entry(frame, textvariable=displayDireccion)

# Establecemos las posiciones de los labels y entrys
labelID.grid(row=0, column=0, sticky=W, padx=10, pady=10)
labelNombre.grid(row=1, column=0, sticky=W, padx=10, pady=10)
labelApellido.grid(row=2, column=0, sticky=W, padx=10, pady=10)
labelPassword.grid(row=3, column=0, sticky=W, padx=10, pady=10)
labelDireccion.grid(row=4, column=0, sticky=W, padx=10, pady=10)

entryID.grid(row=0, column=1, padx=10, pady=10)
entryNombre.grid(row=1, column=1, padx=10, pady=10)
entryApellido.grid(row=2, column=1, padx=10, pady=10)
entryPassword.grid(row=3, column=1, padx=10, pady=10)
entryDireccion.grid(row=4, column=1, padx=10, pady=10)

# Establecemos los botones CRUD
botonCreate = Button(root, text="Crear", command=crear)
botonRead = Button(root, text="Leer", command=leer)
botonUpdate = Button(root, text="Actualizar", command=actualizar)
botonDelete = Button(root, text="Eliminar", command=borrar)

# Empaquetamos los botones para su muestra
botonCreate.pack(side=LEFT, padx=10, pady=10)
botonRead.pack(side=LEFT, padx=10, pady=10)
botonUpdate.pack(side=LEFT, padx=10, pady=10)
botonDelete.pack(side=LEFT, padx=10, pady=10)

# Ejecutando la ventana
root.mainloop()

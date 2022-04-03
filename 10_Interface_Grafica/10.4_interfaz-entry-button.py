from tkinter import *

root = Tk()
root.title("Interfaz Entry")
frame = Frame(root)
frame.pack()

entryNombre = Entry(frame)
entryNombre.grid(row=0, column=1, padx=10, pady=10)
entryApellido = Entry(frame)
entryApellido.grid(row=1, column=1, padx=10, pady=10)
entryDireccion = Entry(frame)
entryDireccion.grid(row=2, column=1, padx=10, pady=10)

labelNombre = Label(frame, text="Nombre:")
labelNombre.grid(row=0, column=0, sticky=W, padx=10, pady=10)
labelApellido = Label(frame, text="Apellido:")
labelApellido.grid(row=1, column=0, sticky=W, padx=10, pady=10)
labelDireccion = Label(frame, text="Direccion:")
labelDireccion.grid(row=2, column=0, sticky=W, padx=10, pady=10)

botonEnvio = Button(root, text="Enviar")
botonEnvio.pack()
root.mainloop()

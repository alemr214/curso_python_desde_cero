from tkinter import *
from tkinter import messagebox

# Creamos la ventana principal
root = Tk()
root.title()

# Funciones


def alert():
    messagebox.askquestion("Alerta", "Has pulsado la seccion de alerta")

    # Se crea el menu contextual
menuBar = Menu(root)

# Especifica a la ventana principal que el menu contextual es el menuBar
root.config(menu=menuBar)

# Creamos las secciones del menu y quitando la opcion por defecto de espacio vacio
fileSection = Menu(menuBar, tearoff=0)
editSection = Menu(menuBar, tearoff=0)
toolSection = Menu(menuBar, tearoff=0)
helpSection = Menu(menuBar, tearoff=0)

# Agregamos las secciones al menu
menuBar.add_cascade(label='File', menu=fileSection)
menuBar.add_cascade(label='Edit', menu=editSection)
menuBar.add_cascade(label='Tools', menu=toolSection)
menuBar.add_cascade(label='Help', menu=helpSection)

# Agregando opciones a las secciones
fileSection.add_command(label='New File')
fileSection.add_command(label='Open Window')
# Agrega un separador entre las opciones dadas
fileSection.add_separator()
fileSection.add_command(label='Open')
fileSection.add_command(label='Save')

editSection.add_command(label='Cut')
editSection.add_command(label='Copy')
editSection.add_command(label='Paste')

toolSection.add_command(label='Undo')
toolSection.add_command(label='Redo')

helpSection.add_command(label='About')
helpSection.add_command(label='Alert', command=alert)
root.mainloop()

from textwrap import fill
from tkinter import *

# Se establece la raiz de la interfaz
raiz = Tk()
raiz.title("Prueba - Frame")
raiz.config(bg="blue")

# Se establece el frame principal de la interfaz grafica
frame = Frame()
# Permite ajustar el frame tanto se expanda la interfaz
frame.pack(fill='both', expand=1)
# Establece configuraciones iniciales como el color de fondo, las medidas de alto y ancho, etc.
frame.config(bg="red", width="630", height="360")
raiz.mainloop()

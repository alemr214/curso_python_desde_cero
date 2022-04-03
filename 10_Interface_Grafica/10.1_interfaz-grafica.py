from tkinter import *

# Establece la base de la interfaz como un objeto
raiz = Tk()
# Asigna un titulo a la interfaz
raiz.title("Pruebas")
# Permite o no modificar las medidas a lo ancho | alto
raiz.resizable(True, False)
# Establece las medidas con la que la interfaz se mostrara al aparecer a lo ancho | alto
raiz.geometry("630x360")
# Permite hacer ajustes como el color de fondo
raiz.config(bg='orange')
# Permite la visualizacion de la interfaz sin cerrarse
raiz.mainloop()

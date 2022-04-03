from tkinter import *

root = Tk()
root.title("Prueba - Labels")
frame = Frame(root, width="500", height="400")
frame.pack()
# Establece una etiqueta para mostrar texto o imagen con coordenadas de inicio
Label(frame, text="Hola Mundo",
      fg="red", font=(19)).place(x=100, y=100)
root.mainloop()

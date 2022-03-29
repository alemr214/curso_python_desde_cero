from tkinter import *

root = Tk()
root.title("Calculadora")

frame = Frame(root)
frame.pack()

# Pantalla de visualizacion
display = Entry(frame)
display.grid(row=0, padx=5, pady=5, columnspan=4)
display.config(background="white", justify="right")

"""---Fila 1---"""
# Botones de operaciones
button7 = Button(frame, text="7")
button8 = Button(frame, text="8")
button9 = Button(frame, text="9")
buttonDiv = Button(frame, text="/")

# Posicionamiento de los botones
button7.grid(row=1, column=0, padx=5, pady=5)
button8.grid(row=1, column=1, padx=5, pady=5)
button9.grid(row=1, column=2, padx=5, pady=5)
buttonDiv.grid(row=1, column=3, padx=5, pady=5)

"""---Fila 2---"""
# Botones de operaciones
button4 = Button(frame, text="4")
button5 = Button(frame, text="5")
button6 = Button(frame, text="6")
buttonMult = Button(frame, text="*")

# Posicionamiento de los botones
button4.grid(row=2, column=0, padx=5, pady=5)
button5.grid(row=2, column=1, padx=5, pady=5)
button6.grid(row=2, column=2, padx=5, pady=5)
buttonMult.grid(row=2, column=3, padx=5, pady=5)

"""---Fila 3---"""
# Botones de operaciones
button1 = Button(frame, text="1")
button2 = Button(frame, text="2")
button3 = Button(frame, text="3")
buttonRest = Button(frame, text="-")

# Posicionamiento de los botones
button1.grid(row=3, column=0, padx=5, pady=5)
button2.grid(row=3, column=1, padx=5, pady=5)
button3.grid(row=3, column=2, padx=5, pady=5)
buttonRest.grid(row=3, column=3, padx=5, pady=5)

"""---Fila 4---"""
# Botones de operaciones
button0 = Button(frame, text="0")
buttonDot = Button(frame, text=".")
buttonSum = Button(frame, text="+")
buttonEqual = Button(frame, text="=")

# Posicionamiento de los botones
button0.grid(row=4, column=0, padx=5, pady=5)
buttonDot.grid(row=4, column=1, padx=5, pady=5)
buttonSum.grid(row=4, column=2, padx=5, pady=5)
buttonEqual.grid(row=4, column=3, padx=5, pady=5)
# Fin de la interfaz grafica
root.mainloop()

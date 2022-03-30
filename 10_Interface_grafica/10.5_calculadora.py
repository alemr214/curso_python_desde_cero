from tkinter import *

# Raiz
root = Tk()
root.title("Calculadora")
# Frame principal
frame = Frame(root)
frame.pack()

# Variables
operator = ""
result = 0

# Funciones


def numberClick(number):
    global operator
    if operator != "":
        displayNumber.set(number)
        operator = ""
    else:
        displayNumber.set(displayNumber.get() + str(number))


def operation(method, number):
    global operator
    global result
    operator = method
    if operator == "sum":
        result += float(number)
        displayNumber.set(result)
    elif operator == "rest":
        result -= float(number)
        displayNumber.set(result)
    elif operator == "mult":
        result *= float(number)
        displayNumber.set(result)
    elif operator == "div":
        result /= float(number)
        displayNumber.set(result)
    elif operator == "equal":
        result += float(number)
        displayNumber.set(result)
        result = 0


# Pantalla de visualizacion
displayNumber = StringVar()
display = Entry(frame, textvariable=displayNumber)
display.grid(row=0, padx=5, pady=5, columnspan=4)
display.config(background="white", justify="right")

"""---Fila 1---"""
# Botones de operaciones
button7 = Button(frame, text="7", command=lambda: numberClick(7))
button8 = Button(frame, text="8", command=lambda: numberClick(8))
button9 = Button(frame, text="9", command=lambda: numberClick(9))
buttonDiv = Button(
    frame, text="/", command=lambda: operation("div", displayNumber.get()))

# Posicionamiento de los botones
button7.grid(row=1, column=0, padx=5, pady=5)
button8.grid(row=1, column=1, padx=5, pady=5)
button9.grid(row=1, column=2, padx=5, pady=5)
buttonDiv.grid(row=1, column=3, padx=5, pady=5)

"""---Fila 2---"""
# Botones de operaciones
button4 = Button(frame, text="4", command=lambda: numberClick(4))
button5 = Button(frame, text="5", command=lambda: numberClick(5))
button6 = Button(frame, text="6", command=lambda: numberClick(6))
buttonMult = Button(
    frame, text="*", command=lambda: operation("mult", displayNumber.get()))

# Posicionamiento de los botones
button4.grid(row=2, column=0, padx=5, pady=5)
button5.grid(row=2, column=1, padx=5, pady=5)
button6.grid(row=2, column=2, padx=5, pady=5)
buttonMult.grid(row=2, column=3, padx=5, pady=5)

"""---Fila 3---"""
# Botones de operaciones
button1 = Button(frame, text="1", command=lambda: numberClick(1))
button2 = Button(frame, text="2", command=lambda: numberClick(2))
button3 = Button(frame, text="3", command=lambda: numberClick(3))
buttonRest = Button(
    frame, text="-", command=lambda: operation("rest", displayNumber.get()))

# Posicionamiento de los botones
button1.grid(row=3, column=0, padx=5, pady=5)
button2.grid(row=3, column=1, padx=5, pady=5)
button3.grid(row=3, column=2, padx=5, pady=5)
buttonRest.grid(row=3, column=3, padx=5, pady=5)

"""---Fila 4---"""
# Botones de operaciones
button0 = Button(frame, text="0", command=lambda: numberClick(0))
buttonDot = Button(frame, text=".")
buttonSum = Button(
    frame, text="+", command=lambda: operation("sum", displayNumber.get()))
buttonEqual = Button(frame, text="=", command=lambda: operation(
    "equal", displayNumber.get()))

# Posicionamiento de los botones
button0.grid(row=4, column=0, padx=5, pady=5)
buttonDot.grid(row=4, column=1, padx=5, pady=5)
buttonSum.grid(row=4, column=2, padx=5, pady=5)
buttonEqual.grid(row=4, column=3, padx=5, pady=5)
# Fin de la interfaz grafica
root.mainloop()

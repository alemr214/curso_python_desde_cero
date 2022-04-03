from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Abrir archivos")


def abrir_archivo():
    archivo = filedialog.askopenfilename(
        initialdir="~/", title="Selecciona un archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))


Button(root, text="Abrir archivo", command=abrir_archivo).pack()
root.mainloop()

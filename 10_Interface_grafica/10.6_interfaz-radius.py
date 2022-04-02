from tkinter import *

root = Tk()
root.title("Radio-buttons")
option = IntVar()
Label(root, text="Genero:").pack()
Radiobutton(root, text="Masculino", value=1).pack(anchor=W)
Radiobutton(root, text="Femenino", value=2).pack(anchor=W)
root.mainloop()

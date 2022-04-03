from multiprocessing.sharedctypes import Value
from tkinter import *

root = Tk()
root.title("Radio-buttons")
frame = Frame(root)
frame.pack()
Label(frame, text="Mascotas").pack()
Checkbutton(frame, text="Perro").pack(anchor=W)
Checkbutton(frame, text="Gato").pack(anchor=W)
Checkbutton(frame, text="Conejo").pack(anchor=W)
root.mainloop()

from tkinter import *
import sqlite3
from tkinter import messagebox


conexion = sqlite3.connect("basedatos1.db")
miCursor = conexion.cursor()

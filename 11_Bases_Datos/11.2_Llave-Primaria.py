import sqlite3

conexion = sqlite3.connect("GestionProductos.db")
miCursor = conexion.cursor()

miCursor.execute("""
    CREATE TABLE IF NOT EXISTS PRODUCTOS (
        codigo_articulo VARCHAR(4) PRIMARY KEY,
        nombre_articulo VARCHAR(50),
        precio INTEGER, 
        seccion VARCHAR(20))""")

productos = [
    ("AR01", "Leche", 15, "Alimentos"),
    ("AR02", "Jabon", 12, "Alimentos"),
    ("AR03", "Cereal", 8, "Alimentos"),
    ("AR04", "Manteca", 25, "Alimentos"),
    ("AR05", "Lavadora", 1200, "Electrodomesticos"),
    ("AR06", "Television", 1500, "Electrodomesticos"),
    ("AR07", "Refrigerador", 1800, "Electrodomesticos"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?, ?, ?, ?)", productos)
conexion.commit()
miCursor.close()
conexion.close()

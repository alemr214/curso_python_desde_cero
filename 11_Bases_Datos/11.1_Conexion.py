import sqlite3

# 1 - Abrir - crear una conexion
conexion = sqlite3.connect("PrimeraBaseDatos.db")

# 2 - Crear un cursor
miCursor = conexion.cursor()

# 3 - Ejecutar querys sql

# 3.1 - Crear tabla
miCursor.execute(
    "CREATE TABLE IF NOT EXISTS productos (nombre_articulo VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")

# 3.2 - Insertar datos
# miCursor.execute(
#     "INSERT INTO productos VALUES('Bici', 15000, 'Deportes')")

# 3.2.1 - Se pueden insertar varios registros a la vez con una lista
variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 20, "Ceramica"),
    ("Campera", 30, "Deportes"),
    ("Lapicero", 1, "Oficina")
]

# 3.2.2 - Usar el metodo executemany para insertar varios registros dados por una lista
miCursor.executemany("INSERT INTO productos VALUES(?, ?, ?)", variosProductos)

# Realizar los cambios en la base de datos
conexion.commit()
# 5 - Cerrar el cursor
miCursor.close()
# 6 - cerrar la conexion
conexion.close()

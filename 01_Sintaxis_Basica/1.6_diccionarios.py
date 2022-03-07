miDiccionario = {"nombre": "Alejandro", "edad": 20, "nickname": "alemr214"}

# Agrega un nuevo elemento con su clave al final del diccionario
miDiccionario["twitter"] = "@alemr215"
print(miDiccionario)
# Sobrescribe el nuevo valor a la clave dada
miDiccionario["twitter"] = "@alemr214"
print(miDiccionario)
# Elimina el valor al cual pertenece la clave dada
del miDiccionario["twitter"]
print(miDiccionario)
# Devuelve solamente las claves del diccionario
print(miDiccionario.keys())
# Devuelve solamente los valores del diccionario
print(miDiccionario.values())
# Devuelve el diccionario entero
print(miDiccionario)

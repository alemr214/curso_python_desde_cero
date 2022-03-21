# Texto de ejemplo
texto = " este es un ejemplar de texto "

# Texto vueto mayusculas
print(texto.upper())
# texto vuelto minusculas
print(texto.lower())
# Texto con la primera letra mayuscula (capitales)
print(texto.capitalize())
# Devuelve la cantidad de coincidencias en todo el texto
print(texto.count('es'))
# Devuelve el indice de la primer coincidencia
print(texto.find('ejemplar'))
# Devuelve un booleano (true o false) si el texto son digitos
print(texto.isdigit())
# Devuelve un booleano (true o false) si el texto es alfanumerico
print(texto.isalnum())
# Devuelve un booleano (true o false) si el texto solo cuenta con puras letras
print(texto.isalpha())
# Regresa en una lista los caracteres (palabra), siendo separado por los espacios en blanco
print(texto.split())
# Elemina el caracter si es que lo tiene en al inicio y al final de la cadena
print(texto.strip(' '))
# Reemplaza las conincidencias por los nuevos caracteres
print(texto.replace('ejemplar', 'ejemplo'))
# Devuelve el indice de la ultima coincidencia de la cadena o caracter
print(texto.rfind('o'))

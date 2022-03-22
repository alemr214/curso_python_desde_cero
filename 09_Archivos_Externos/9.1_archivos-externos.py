import io

archivo = open("archivo.txt", "a ")
frase = "Este es una frase de ejemplo que  se escribira en un nuevo archivo de texto"
archivo.write(frase)
archivo.close()

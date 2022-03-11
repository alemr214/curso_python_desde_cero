# Tupla para almacenar los datos
materias = ("informatica", "pruebas de software", "usabilidad y accesibilidad")
print("Programa para eleccion de materias")
cantidadMaterias = int(
    input("Ingresa la cantidad de materias cargadas actualmente: "))
# Condicional anidado
if cantidadMaterias >= 0 and cantidadMaterias <= 5:
    print("Puedes elegir entre las siguientes materias: ", materias)
    desicion = input("Ingresa el nombre de la materia a elegir: ").lower()
    if desicion in materias:
        print("Asignatura elegida: ", desicion)
    else:
        print("Asignatura incorrecta")
else:
    print("No puedes cargar mas asignaturas")

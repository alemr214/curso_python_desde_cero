miLista = [10, 5, 2, 10, 3, 10, 7, 7, 3, 7]

# Devuelve el valor que se encuentra en la posicion dada
print(miLista[2])
# Imprime los valores de las posiciones que se encuentran desde el primer limite inferior hasta antes del limite superior
print(miLista[1:4])
# Permite agregar un nuevo valor al final de la lista
miLista.append(13)
print(miLista[:])
# Permite agregar en la posicion indicada un nuevo valor
miLista.insert(2, 4)
print(miLista[:])
# Agrega multiples elementos al final de la lista
miLista.extend([20, 16, 20, 16, 20, 18, 18, 16, 20, 19])
print(miLista[:])
# Regresa el valor del indice (posicion) en la que se encuentra la primera concidencia del valor
print(miLista.index(10))
# Regresa un valor booleano (true o false) si es que existe el dato en la lista
coincidencia = 1 in miLista
print(coincidencia)
# Elimina la primer coincidencia del dato ingresado
miLista.remove(10)
print(miLista[:])
# Elimina el ultimo elemento de la lista
miLista.pop()
print(miLista[:])

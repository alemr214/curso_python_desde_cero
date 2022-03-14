# El * se usa para indicarle una cantidad indefinida
def devuelveSubElementos(*elementos):
    for iterador in elementos:
        # Devuelve un subelemento del elemento elemento dado
        yield from iterador


nombres = devuelveSubElementos("John", "Doe")
# Imprime los sub elementos del primer elemento
print(next(nombres))

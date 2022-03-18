# Se declara la clase con su nombre
class Automovil():
    # Se declaran los atributos de la clase con su modificador de acceso
    # public = nombre_atributo
    # protected = _nombre_atributo
    # private = __nombre_atributo
    __velocidad = None
    __velocidadMaxima = None

    # Metodos lectores (getters)
    def getVelocidad(self):
        return self.velocidad

    def getVelocidadMaxima(self):
        return self.__velocidadMaxima

    # Metodos modificadores (setters)
    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad

    def setVelocidadMaxima(self, velocidadMaxima):
        self.__velocidadMaxima = velocidadMaxima

    # Metodo constructor
    def __init__(self):
        self.__velocidadMaxima = 90

    # Metodo algoritmico
    def determinaExcede(self):
        excede = False
        if self.__velocidad > self.__velocidadMaxima:
            excede = True
        else:
            excede = False
        return excede


# Funcion principal (main) del programa
def main():
    # Instancia de la clase
    miAutomovil = Automovil()
    velocidad = float(input("INgresa la velocidad del automovil"))
    # Modificando el valor del atributo
    miAutomovil.setVelocidad(velocidad)
    excede = miAutomovil.determinaExcede()
    if excede == True:
        print("El auto excede la velocidad maxima de 90 km/h")
    else:
        print("El auto no excede la velocidad maxima de 90 km/h")


if __name__ == '__main__':
    main()

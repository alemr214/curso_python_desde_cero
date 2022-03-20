# Super clase con atributos, metodos y constructor definido
class Persona():
    __nombre = None
    __apellidoPaterno = None
    __apellidoMaterno = None
    __edad = None

    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad):
        self.__nombre = nombre
        self.__apellidoPaterno = apellidoPaterno
        self.__apellidoMaterno = apellidoMaterno
        self.__edad = edad

    def describir(self):
        print("Nombre: ", self.__nombre, " ", self.__apellidoPaterno,
              " ", self.__apellidoMaterno, " edad: ", self.__edad)


# Sub clase que va a obtener (heredar) los atributos de Persona
class Empleado(Persona):
    __salario = None
    __antiguedad = None

    # Constructor propio agregando parametros para hacer uso de metodos (opcionales) de la superclase
    def __init__(self, salario, antiguedad, nombre_empleado, apellidoP_empleado, apellidoM_empleado, edad_empleado):
        # Se sobre ingresan los atributos de la superclase usando el constructor de la misma
        super().__init__(nombre_empleado, apellidoP_empleado,
                         apellidoM_empleado, edad_empleado)
        self.__salario = salario
        self.__antiguedad = antiguedad

    def describir(self):
        # Pasa el metodo de la superclase y despues ejecuta las sentencias del propio
        super().describir()
        print("Salario: ", self.__salario,
              " Antiguedad: ", self.__antiguedad, " anios")


def main():
    miEmpleado = Empleado(1500, 5, "Alejandro", "Martinez", "Rivera", 19)
    miEmpleado.describir()


if __name__ == '__main__':
    main()

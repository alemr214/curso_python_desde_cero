# Multiples clases declaradas
class Automovil():
    def descripcion():
        print("Este vehiculo usa 4 ruedas")


class Motocicleta():
    def descripcion():
        print("Este vehiculo usa 2 ruedas")


class Autobus():
    def descripcion():
        print("Este vehiculo usa 6 ruedas")


def main():
    # Funcion que permite el polimorfismo haciendo cambio
    # del objeto al momento de declararlo y posiblemente
    # cambiarlo en funcion de lo requerido
    def definirVehiculo(vehiculo):
        vehiculo.descripcion()

    # Declaracion del objeto
    miVehiculo = Automovil()
    definirVehiculo(miVehiculo)


if __name__ == '__main__':
    main()

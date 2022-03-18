def operarDivison():
    try:
        numero1 = int(input("Ingresa un numero: "))
        numero2 = int(input("Ingresa otro numero: "))
        division = numero1 / numero2
        return division
    except ZeroDivisionError:
        print("No se puede divir sobre 0")
    finally:
        print("Fin de la ejecucion")


print(operarDivison())

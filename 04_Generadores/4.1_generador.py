def generarPares(limite):
    numero = 1
    while numero < limite:
        yield numero * 2
        numero += 1


def main():
    resultado = generarPares(10)
    for i in resultado:
        print(i)


if __name__ == '__main__':
    main()

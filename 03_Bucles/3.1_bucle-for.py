email = input("Ingrese su correo electronico: ")
validacion = False

for i in email:
    if i == "@":
        validacion = True

if validacion == True:
    print("El correo es valido")
else:
    print("El correo es invalido")

print("Evaluacion para entrar a un lugar")
edadUsuario = int(input("Ingresa tu edad: "))

# Primera condicion
if edadUsuario > 0 and edadUsuario < 18:
    print("No puede pasar")
# Segunda condicion
elif edadUsuario > 18 and edadUsuario < 100:
    print("Puede pasar")
# Instruccion por defecto
else:
    print("Edad incorrecta")

def evaluacion(calificacion):
    valoracion = "aprobado"
    # Condicional if - condicion a evaluar
    #   instrucciones
    if calificacion < 5:
        valoracion = "suspenso"
    return valoracion


print("Programa de evaluacion de calificaciones\nIngresa tu calificacion:")
calificacion1 = int(input())
print("usted esta", evaluacion(calificacion1))

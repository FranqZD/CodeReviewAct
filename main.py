import random

def iniciar_juego():
    numero_secreto = random.randint(1, 20)
    intento_usuario = 0
    intentos_totales = 0
    print("Adivina el número entre 1 y 20")
    
    while intento_usuario != numero_secreto:
        intento_usuario = int(input("Ingresa tu intento: "))
        intentos_totales += 1
        if intento_usuario < numero_secreto:
            print("Muy bajo")
        elif intento_usuario > numero_secreto:
            print("Muy alto")
        elif intento_usuario == numero_secreto:
            print("¡Correcto!")
        print("Número de intentos:", intentos_totales)

iniciar_juego()
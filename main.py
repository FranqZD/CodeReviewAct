import random

def mostrar_instrucciones():
    print("--- BIENVENIDO AL JUEGO ---")
    print("Adivina el número entre 1 y 20")

def procesar_intento(intento, objetivo):
    if intento < objetivo:
        print("Muy bajo")
        return False
    elif intento > objetivo:
        print("Muy alto")
        return False
    print("¡Correcto!")
    return True

def iniciar_juego():
    mostrar_instrucciones()
    numero_secreto = random.randint(1, 20)
    intentos = 0
    adivinado = False
    
    while not adivinado:
        intento = int(input("Ingresa tu intento: "))
        intentos += 1
        adivinado = procesar_intento(intento, numero_secreto)
        print(f"Intentos: {intentos}")

iniciar_juego()
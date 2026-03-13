import random

def mostrar_instrucciones(min_val, max_val):
    """Muestra el mensaje de bienvenida con el rango dinámico."""
    print("--- BIENVENIDO AL JUEGO ---")
    print(f"Instrucciones: Adivina el número entre {min_val} y {max_val}")

def solicitar_numero(min_val, max_val):
    """Solicita un número y valida que sea un entero."""
    while True:
        try:
            return int(input(f"Ingresa tu intento ({min_val}-{max_val}): "))
        except ValueError:
            print("Error: Solo se permiten números enteros.")

def procesar_intento(intento, objetivo):
    """Compara el intento con el objetivo y retorna el estado de la partida."""
    if intento < objetivo:
        print("Muy bajo")
        return False
    elif intento > objetivo:
        print("Muy alto")
        return False
    print("¡Correcto!")
    return True

def iniciar_juego(min_val=1, max_val=20):
    """Lógica principal del juego con parámetros de rango."""
    mostrar_instrucciones(min_val, max_val)
    numero_secreto = random.randint(min_val, max_val)
    intentos = 0
    adivinado = False
    
    while not adivinado:
        intento = solicitar_numero(min_val, max_val)
        intentos += 1
        adivinado = procesar_intento(intento, numero_secreto)
        print(f"Número de intentos: {intentos}\n")

if __name__ == "__main__":
    iniciar_juego(1, 20)
import random

def seleccionar_dificultad() -> tuple[int, int]:
    """Permite al usuario elegir un nivel y devuelve el rango (min, max)."""
    niveles = {
        "1": ("Fácil", 1, 10),
        "2": ("Medio", 1, 50),
        "3": ("Difícil", 1, 100)
    }
    
    print("Selecciona un nivel de dificultad:")
    for tecla, (nombre, inicio, fin) in niveles.items():
        print(f"{tecla}. {nombre} ({inicio}-{fin})")
    
    while True:
        opcion = input("Opción: ")
        if opcion in niveles:
            _, mi, ma = niveles[opcion]
            return mi, ma
        print("Opción no válida. Elige 1, 2 o 3.")

def solicitar_numero(min_val: int, max_val: int) -> int:
    """Solicita un número y valida que sea un entero dentro del rango."""
    while True:
        try:
            valor = int(input(f"Ingresa tu intento ({min_val}-{max_val}): "))
            if min_val <= valor <= max_val:
                return valor
            print(f"Fuera de rango. Prueba entre {min_val} y {max_val}.")
        except ValueError:
            print("Error: Escribe un número entero.")

def procesar_intento(intento: int, objetivo: int) -> bool:
    """Compara el intento con el objetivo."""
    if intento < objetivo:
        print("📉 Muy bajo")
        return False
    if intento > objetivo:
        print("📈 Muy alto")
        return False
    print("🎉 ¡Correcto!")
    return True

def iniciar_juego() -> None:
    """Configura y arranca la partida."""
    print("--- BIENVENIDO AL JUEGO DE ADIVINANZA ---")
    
    # Obtenemos el rango basado en la dificultad seleccionada
    min_val, max_val = seleccionar_dificultad()
    
    numero_secreto = random.randint(min_val, max_val)
    intentos = 0
    adivinado = False
    
    print(f"\n¡Listo! He pensado un número entre {min_val} y {max_val}.")
    
    while not adivinado:
        intento = solicitar_numero(min_val, max_val)
        intentos += 1
        adivinado = procesar_intento(intento, numero_secreto)
        print(f"Número de intentos: {intentos}\n")

if __name__ == "__main__":
    iniciar_juego()
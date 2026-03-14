import random

def obtener_entero(mensaje: str, min_permitido: int = float('-inf')) -> int:
    """Función auxiliar para validar entradas de configuración."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= min_permitido:
                return valor
            print(f"El valor debe ser al menos {min_permitido}.")
        except ValueError:
            print("Error: Ingresa un número entero válido.")

def seleccionar_configuracion() -> tuple[int, int, int]:
    """Gestiona la selección de dificultad y devuelve (min, max, intentos)."""
    niveles = {
        "1": ("Fácil", 1, 10, 5),
        "2": ("Medio", 1, 50, 8),
        "3": ("Difícil", 1, 100, 10)
    }
    
    print("\n--- SELECCIONA TU DIFICULTAD ---")
    for tecla, (nombre, inicio, fin, intentos) in niveles.items():
        print(f"{tecla}. {nombre} ({inicio}-{fin}) | {intentos} intentos")
    print("4. Personalizada (Tú eliges las reglas)")
    
    while True:
        opcion = input("Opción: ")
        if opcion in niveles:
            _, mi, ma, i = niveles[opcion]
            return mi, ma, i
        
        if opcion == "4":
            print("\n--- CONFIGURACIÓN PERSONALIZADA ---")
            mi = obtener_entero("Rango inicial (mín): ")
            ma = obtener_entero(f"Rango final (máx) [debe ser > {mi}]: ", mi + 1)
            i = obtener_entero("Número máximo de intentos: ", 1)
            return mi, ma, i
            
        print("Opción no válida. Elige 1, 2, 3 o 4.")

def solicitar_numero(min_val: int, max_val: int) -> int:
    """Solicita un número y valida que esté dentro del rango especificado."""
    while True:
        try:
            valor = int(input(f"Ingresa tu intento ({min_val}-{max_val}): "))
            if min_val <= valor <= max_val:
                return valor
            print(f"Fuera de rango. Prueba entre {min_val} y {max_val}.")
        except ValueError:
            print("Error: Escribe un número entero.")

def procesar_intento(intento: int, objetivo: int) -> bool:
    """Compara el intento con el objetivo y da feedback."""
    if intento < objetivo:
        print("📉 Muy bajo")
        return False
    if intento > objetivo:
        print("📈 Muy alto")
        return False
    print("🎉 ¡Correcto!")
    return True

def iniciar_juego() -> None:
    """Orquestador principal del juego."""
    print("--- BIENVENIDO AL JUEGO DE ADIVINANZA ---")
    
    min_val, max_val, intentos_restantes = seleccionar_configuracion()
    numero_secreto = random.randint(min_val, max_val)
    intentos_totales = intentos_restantes
    adivinado = False
    
    print(f"\n¡Listo! He pensado un número entre {min_val} y {max_val}.")
    
    while intentos_restantes > 0 and not adivinado:
        print(f"Intentos restantes: {intentos_restantes}")
        intento = solicitar_numero(min_val, max_val)
        intentos_restantes -= 1
        
        adivinado = procesar_intento(intento, numero_secreto)
        
        if adivinado:
            print(f"Ganaste en {intentos_totales - intentos_restantes} intentos.\n")
        elif intentos_restantes == 0:
            print(f"Te has quedado sin intentos. El número era {numero_secreto}.\n")

if __name__ == "__main__":
    iniciar_juego()
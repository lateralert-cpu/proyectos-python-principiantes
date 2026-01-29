import random

def adivina_el_numero(limite_inferior=1, limite_superior=100):
    """
    Juego de Adivina el Número.
    El programa elige un número aleatorio entre limite_inferior y limite_superior.
    El usuario debe adivinarlo con pistas de 'mayor' o 'menor'.
    """
    
    # 1. El programa elige un número aleatorio dentro del rango
    numero_secreto = random.randint(limite_inferior, limite_superior)
    intentos = 0
    adivinado = False

    print(f"¡Bienvenido a Adivina el Número!")
    print(f"He pensado un número entre {limite_inferior} y {limite_superior}.")
    print("¿Puedes adivinar cuál es?")

    # 2. Bucle del juego
    while not adivinado:
        try:
            # Pedir input al usuario
            entrada = input("Ingresa tu predicción: ")
            probada = int(entrada)
            intentos += 1

            # 3. Dar pistas
            if probada < numero_secreto:
                print("¡Mas alto! El número es mayor.")
            elif probada > numero_secreto:
                print("¡Mas bajo! El número es menor.")
            else:
                # 4. Adivinó correctamente
                adivinado = True
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} correctamente.")
                print(f"Te tomó {intentos} intentos.")
        
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    adivina_el_numero()

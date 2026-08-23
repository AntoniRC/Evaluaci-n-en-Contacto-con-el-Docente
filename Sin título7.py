import random

def mostrar_titulo():
    """Muestra el título del juego"""
    print("=" * 40)
    print("JUEGO DE PIEDRA, PAPEL O TIJERA")
    print("=" * 40)

def mostrar_menu():
    """Muestra las opciones del menú principal"""
    print("=" * 40)
    print("           MENU")
    print("1. Jugar")
    print("2. Ver marcador")
    print("3. Reiniciar marcador")
    print("4. Salir")
    print("=" * 40)

def obtener_nombre():
    """Pide y devuelve el nombre del jugador"""
    nombre = input("Ingrese su nombre: ")
    return nombre

def elegir_jugada_jugador():
    """Pide la jugada, valida y devuelve el nombre (Piedra/Papel/Tijera)"""
    print("\nSeleccione su jugada:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    
    while True:
        entrada = input("Elija una opción: ")
        
        try:
            jugador = int(entrada)
        except ValueError:
            print("Error: Debe escribir un número. Inténtelo de nuevo.")
            continue
        
        if jugador == 1:
            return "Piedra"
        elif jugador == 2:
            return "Papel"
        elif jugador == 3:
            return "Tijera"
        else:
            print("Opción incorrecta. Inténtelo de nuevo.")

def elegir_jugada_computadora():
    """Genera y devuelve una jugada aleatoria de la computadora"""
    opciones = ["Piedra", "Papel", "Tijera"]
    return random.choice(opciones)

def calcular_resultado(jugador, computadora):
    """Recibe las dos jugadas, compara y devuelve el resultado y el tipo"""
    if jugador == computadora:
        return "¡Empate!", "empate"
    elif (jugador == "Piedra" and computadora == "Tijera") or \
         (jugador == "Papel" and computadora == "Piedra") or \
         (jugador == "Tijera" and computadora == "Papel"):
        return "¡Ganaste!", "victoria"
    else:
        return "¡Perdiste!", "derrota"

def mostrar_marcador(nombre, victorias, derrotas, empates):
    """Muestra el marcador usando bucle FOR para recorrer los datos"""
    print("\n" + "=" * 40)
    print("            MARCADOR")
    datos = [
        ("Jugador", nombre),
        ("Victorias", victorias),
        ("Derrotas", derrotas),
        ("Empates", empates)
    ]
    for etiqueta, valor in datos:
        print(f"{etiqueta}: {valor}")
    print("=" * 40)

def reiniciar_marcador():
    """Devuelve los contadores a cero"""
    return 0, 0, 0

mostrar_titulo()
nombre = obtener_nombre()

victorias = 0
derrotas = 0
empates = 0

while True:
    mostrar_menu()
    opcion = input("Elija una opción: ")

    if opcion == "1":
        jugada_jugador = elegir_jugada_jugador()
        jugada_pc = elegir_jugada_computadora()

        print(f"\nJugador: {jugada_jugador}")
        print(f"Computadora: {jugada_pc}")

        mensaje, tipo = calcular_resultado(jugada_jugador, jugada_pc)
        print(f"Resultado: {mensaje}")

        if tipo == "victoria":
            victorias += 1
        elif tipo == "derrota":
            derrotas += 1
        else:
            empates += 1

    elif opcion == "2":
        mostrar_marcador(nombre, victorias, derrotas, empates)

    elif opcion == "3":
        victorias, derrotas, empates = reiniciar_marcador()
        print("\nMarcador reiniciado.")

    elif opcion == "4":
        print(f"\nGracias por jugar, {nombre}")
        break

    else:
        print("Opción incorrecta. Inténtelo de nuevo.")
import time, random

# Recursos iniciales
madera = 0
palos = 0
piedra = 0
carbon = 0
hierro = 0
diamante = 0

# Herramientas
pico = "pico de piedra"  # Comienza con un pico de piedra

# Función para mostrar el inventario
def mostrar_inventario():
    print(f"\nInventario:")
    print(f"Madera: {madera}")
    print(f"Palos: {palos}")
    print(f"Piedra: {piedra}")
    print(f"Carbón: {carbon}")
    print(f"Hierro: {hierro}")
    print(f"Diamante: {diamante}")
    print(f"Herramienta actual: {pico}")

# Introducción al juego
print("Bienvenido a Minecraft")
print("Spawneas cerca de un bosque y una mina")
print("Tu meta es hacer una espada de diamante, pero para eso necesitas recolectar recursos y mejorar tu pico.")

# Ciclo principal del juego
while True:
    mostrar_inventario()
    
    print('''\n¿Qué deseas hacer?:
    1.- Ir a talar madera
    2.- Ir a minar piedra
    3.- Ir a minar carbón
    4.- Ir a minar hierro
    5.- Ir a minar diamantes
    6.- Mejorar tu pico
    S.- Salir del juego
    ''')
    
    opc = input("Selecciona una opción: ").lower()

    if opc == "1":
        cantm = random.randint(1, 14)
        madera += cantm
        print(f"Talas {cantm} de madera.")

    elif opc == "2":
        if pico == "pico de piedra" or pico == "pico de hierro" or pico == "pico de diamante":
            cantp = random.randint(1, 14)
            piedra += cantp
            print(f"Minas {cantp} de piedra.")
        else:
            print("Tu pico no puede minar piedra.")

    elif opc == "3":
        if pico == "pico de piedra" or pico == "pico de hierro" or pico == "pico de diamante":
            cantc = random.randint(1, 14)
            carbon += cantc
            print(f"Minas {cantc} de carbón.")
        else:
            print("Tu pico no puede minar carbón.")

    elif opc == "4":
        if pico == "pico de hierro" or pico == "pico de diamante":
            canthi = random.randint(1, 14)
            hierro += canthi
            print(f"Minas {canthi} de hierro.")
        else:
            print("Tu pico no puede minar hierro.")

    elif opc == "5":
        if pico == "pico de diamante":
            cantd = random.randint(1, 14)
            diamante += cantd
            print(f"Minas {cantd} de diamantes.")
        else:
            print("Tu pico no puede minar diamantes.")
    
    elif opc == "6":
        # Mejorar el pico
        if pico == "pico de piedra":
            if madera >= 3 and piedra >= 2:
                pico = "pico de hierro"
                madera -= 3
                piedra -= 2
                print("¡Has mejorado tu pico a un pico de hierro!")
            else:
                print("No tienes los materiales suficientes para mejorar a pico de hierro.")
        elif pico == "pico de hierro":
            if hierro >= 3 and madera >= 2:
                pico = "pico de diamante"
                hierro -= 3
                madera -= 2
                print("¡Has mejorado tu pico a un pico de diamante!")
            else:
                print("No tienes los materiales suficientes para mejorar a pico de diamante.")
        else:
            print("Ya tienes el pico más avanzado: pico de diamante.")

    elif opc == "s":
        print("¡Gracias por jugar! Adiós.")
        break

    else:
        print("Opción no válida. Intenta nuevamente.")
    
    # Espera para hacer el juego más realista
    time.sleep(1)

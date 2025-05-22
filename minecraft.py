import time , random

madera=0
palos=0
piedra=0
carbon=0
hierro=0
diamante=0



print("Bienvenido a Minecraft")
print("Spawneas cerca de un bosque y una mina")

while True:

    print('''
    1.- Ir a Talar
    2.- Ir a minar
    3.- Craftear
    4.-  Tradear
    S.- Salir del juego
    ''')

    opc=int(input("¿Que deseas hacer?"))

    match opc:

        case 1:
            canta=random.randint(7,9)
            print("Decides talar madera de un arbol\n" \
            f"Consigues {canta} de madera")
            madera+=canta
            print("Tienes {Madera} de madera")
        case 2:
            break

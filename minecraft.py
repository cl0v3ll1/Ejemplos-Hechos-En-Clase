import time , random

madera=0
palos=0
piedra=0
carbon=0
hierro=0
diamante=0

def mostrar_inventario():

    print(f"\nInventario:")
    print(f"Madera: {madera}")
    print(f"Palos: {palos}")
    print(f"Piedra: {piedra}")
    print(f"Carbón: {carbon}")
    print(f"Hierro: {hierro}")
    print(f"Diamante: {diamante}")
    print(f"Herramienta actual: {pico}")

pico="pico de madera"
print("Bienvenido a Minecraft")
print("Spawneas cerca de un bosque y una mina")
print("Tu meta es hacer una espada de diamante, miras alrededor y ves varias zonas")

while True:
    
    print('''
    1.- Ir a talar madera
    2.- Ir a minar piedra
    3.- Ir a minar carbon
    4.- Ir a minar hierro
    5.- Ir a minar diamantes
    S.- Salir del juego
    ''')

    opc=int(input("¿Que deseas hacer? \n"))

    match opc:

        case 1:
            cantm=int(input("Decides talar madera"))
            cantm=random.randint(1,14)
            if cantm==1:
                print(f"Talas 1 de madera")
            madera+=1
        case 2:
            cantp=int(input("Decides minar piedra en la mina"))
            cantp=random.randint(1,14)
            if cantp==1:
                print(f"Minas 1 de piedra")
            piedra+=1
        case 3: 
            cantc=int(input("Decides minar piedra en la mina"))
            cantc=random.randint(1,14)
            if cantc==1:
                print(f"Minas 1 de carbon")
            carbon+=1
        case 4:
            canthi=int(input("Decides minar piedra en la mina"))
            canth=random.randint(1,14)
            if canth==1:
                print(f"Minas 1 de carbon")
            hierro+=1
        
        
        


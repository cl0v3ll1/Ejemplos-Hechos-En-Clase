# import random, time

# perros=int(input("Ingresa la cantidad de perros que vas a mandar a cazar"))
# cuota=3
# cumple=0

# print("¡Comienza la caza!")
# for i in range(perros):
#     conejos=random.randint(0,6)
#     if conejos>=cuota:
#         print(f"El perro {i+1} trajo {conejos} conejos")
#         print("¡Hay flete!")
#         cumple+=1
#     else:
#         print(f"El perro {i+1} trajo {conejos} conejos")
#         print("No hay flete.")
# print(f"La cantidad de perros que cumplio fue {cumple}")

total=0
print("¡Bienvenido al lavado de autos!")
print('''

1.-  Cursar pago del lavado
2.- Ver ventas diarias
3.- Salir    ''')

opc=int(input("Ingresa tu opcion:"))
match opc:

    case 1:
        print('''
        1.-  Full $15000
        2.- Estandar 10000
        3.-Basico     ''')

        opc=int(input("Ingresa tu opcion:"))

        match opc:

            case 1:
                total+=15000

    case 2:
    case 3:
    case _:


#--------------------------------------------------------------------------------------

#Try en bucle de while

# while True:
#     try:
#         num=int(input("Ingrese un numero: "))
#         break
#     except Exception:
#         print("Error. Solo numeros enteros")
# print(f"Su numero es {num}")

# el except depende de si es int str o float

#--------------------------------------------------------------------------------------

#Ejemplo de sintaxis de try except

# try:
#     num=int(input("ingrese un numero: "))
# except Exception:
#     print("Solo puede ingresar numeros enteros")
# else: # 98% no se usa
#     print("Si es que no hay excepcion")
# finally: # 99% de las veces no se usa
#     print("Este bloque se ejecutara si o si, sin importar si hay excepcion o no")

#--------------------------------------------------------------------------------------

# Menu de opciones con Try & Except


# while True:
#     try:
#         opc=int(input('''
#                      Seleccione una opcion (SOLO NUMEROS ENTEROS)
#                     1.- Opcion 1 
#                     2.- Opcion 2 
#                     3.- Opcion 3 
#                     4.- Salir
                    
#                       '''))
#         match opc:
#             case 1:
#                 print("Eligiste opcion 1")
#             case 2:
#                 print("Eligiste opcion 2")
#             case 3:
#                 print("Eligiste opcion 3")
#             case 4:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opcion invalida")

#     except Exception:
#         print("Solo puede ingresar numeros enteros")

# Carrito yum
# total=0
# cantart=0

# print("Este es un carrito de compras")

# while True:
#     try:
#         opc=int(input('''
#                     --Carrito de Compras--
#                     Seleccione una opcion (Solo puede digitar numeros enteros)
#                     1.- Comprar Fruta
#                     2.- Comprar Verdura
#                     3.- pagar
#                     4.- Salir
                    
#                       '''))
#         match opc:
#             case 1: 
#                while True:
#                     try:
#                         print("Eligiste opcion 1")
#                         opc=int(input('''
#                                     1.- Platano {$200}
#                                     2.- Melon {$700}
#                                     3.- Frutilla {$300}
#                                     4.- Salir
                                    
#                                     '''))
#                         match opc:
#                             case 1:
#                                 print("Eligiste opcion 1")
#                                 total+=200
#                                 cantart+=1
#                                 print("Añadiste [Platano] a tu carrito")
#                             case 2:
#                                print("Eligiste opcion 2")
#                                total+=700
#                                cantart+=1
#                                print("Añadiste [Melon] a tu carrito")
#                             case 3:
#                                 print("Eligiste opcion 3")
#                                 total+=300
#                                 cantart+=1
#                                 print("Añadiste [Frutilla] a tu carrito")
#                             case 4:
#                                 print("Saliendo")
#                                 break
#                             case _:
#                                 print("Opcion invalida")
#                         print(f"Su total hasta ahora es de {total}")

#                     except Exception:
#                         print("Solo puede ingresar numeros enteros")
#             case 2:
#                 while True:
#                     try:
#                         print("Eligiste opcion 2")
#                         opc=int(input('''
#                                     1.- Tomate {$300}
#                                     2.- Papa {$200}
#                                     3.- Brocoli {$700}
#                                     4.- Salir
                                    
#                                     '''))
#                         match opc:
#                             case 1:
#                                 print("Eligiste opcion 1")
#                                 total+=300
#                                 cantart+=1
#                                 print("Añadiste [Tomate] a tu carrito")
#                             case 2:
#                                print("Eligiste opcion 2")
#                                total+=200
#                                cantart+=1
#                                print("Añadiste [Papa] a tu carrito")
#                             case 3:
#                                 print("Eligiste opcion 3")
#                                 total+=700
#                                 cantart+=1
#                                 print("Añadiste [Brocoli] a tu carrito")
#                             case 4:
#                                 print("Saliendo")
#                                 break
#                             case _:
#                                 print("Opcion invalida")
#                         print(f"Su total hasta ahora es de {total}")

#                     except Exception:
#                         print("Solo puede ingresar numeros enteros")
#             case 3:
#                 print("Eligiste opcion 3")
#                 print("BOLETA DE COMPRA")
#                 print(f"Productos comprados: {cantart}")
#                 print(f"Total Neto: ${total}")

#                 iva=total*0.19
#                 total_final=total+iva

#                 print(f"IVA (19%): ${iva:.0f}")
#                 print(f"TOTAL A PAGAR: ${total_final:.0f}")
#             case 4:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opcion invalida")

#     except Exception:
#         print("Solo puede ingresar numeros enteros")

#--------------------------------------------------------------------------------------

# Domingo de pascua

# Preguntar la cantidad de niños de niños que buscan huevitos de chocolates
# Cuando se termine la busqueda, preguntar cantos huevos encontró cada uno
# y clasificarlos de la sigueinte forma
# Menos de una docena: NOOB
# Entre una docena a 24: Master
# 25 huevos o mas : Legend

# Mostrar resumen, y mostrar la mayor cantida de huevitos encontrados por un solo niño

import random
while True:

    try:
        cantniños=int(input("¿Cuantos niños van a buscar huevitos: \n"))

        while cantniños<0:
            print("Error. Solo numeros enteros positivos")
            cantniños=int(input("¿Cuantos niños van a buscar huevitos: \n"))

        noob=0
        pro=0
        legend=0

        top=0

        for n in range(cantniños):
            canthuevos=random.randint(5,30)
            if canthuevos>top:
                top=canthuevos
            print(f"El niño {n+1} encontro {canthuevos} huevos (eggs)")
            if canthuevos<12:
                noob+=1
            elif canthuevos>=12 and canthuevos<=24:
                pro+=1
            else:
                legend+=1

        print(f"La cantidad de noobs es {noob}")
        print(f"La cantidad de pros es {pro}")
        print(f"La cantidad de legends es {legend}")
        print(f"La mayor cantidad de huevos encontrada por un niño es {top}")
        break
    except Exception:
        print("Solo numeros enteros")

#--------------------------------------------------------------------------------------
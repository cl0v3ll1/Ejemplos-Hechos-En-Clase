#Lista (Carrito de compras)

# productos=["Disco SSD 1TB", "Memoria Ram 8GB", "Mouse"]
# precios=[70000, 30000, 15000]
# carrito=[]

# while True:
#     print('''
#         1.- Ingresar productos a la tienda
#         2.- Comprar
#         3.- Crear Boleta
#         4.- Salir
#           ''')
#     op=int(input("Ingese una opcion: "))
#     match op:
#         case 1:
#             pro=input("Ingrese el nombre del Producto: ")
#             productos.append(pro)
#             pre=int(input("Ingrese el Precio: "))
#             precios.append(pre)
#         case 2:
#                 for i in range(len(productos)):
#                     print(i+1, ".-", productos[i], "$", precios[i] )
#                 pro=int(input("Selecione que quiere comprar: "))
#                 carrito.append(pro-1)
#                 print(carrito)
#         case 3:
#             total=0
#             print("---------------0----------------")
#             print("Bienvenido a PC House ")


#             for i in carrito:
#                   print( productos[i], "----- $", precios[i] )
#                   total=total+precios[i]
#             print("Es total de articulos es", len(carrito))
#             print("Su total neto es ", total)
#             print("Su total mas iva es ", total*1.19)
#             print("---------------0----------------")

#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("opcion invalida")

# --------------------------------------------------------------------------------

# Lista (Nombres y Apellidos)

# nombres=[]
# apellidos=[]

# while True:

#     try:

#         print("Bienvenido al programa de nombres y apellidos")

#         print('''
#             --------------_0_---------------
#             Seleccione una opcion
#             1.- Insertar nombre y apellidos
#             2.- Buscar nombres
#             3.- Mostrar nombres
#             4.- Salir
#             --------------_0_---------------''')

#         opc=int(input("¿Que va a hacer?"))

#         match opc:

#             case 1:

#                 nom=input("Ingrese su nombre: \n")
#                 nombres.append(nom)

#                 ape=input("Ingrese su apellido: \n")
#                 apellidos.append(ape)

#             case 2:

#                 nombre=input("¿Que nombre desea buscar?")

#                 if nombre in nombres:
#                     print("El nombre que desea buscar si se encuentra")
#                 else:
#                     print("El nombre que desea buscar no se encuentra")

#             case 3:

#                 print(nombres)
#                 print(apellidos)

#             case 4:

#                 print("Saliendo del programa")
#                 break

#             case _:
#                 print("Opcion invalida")

#     except Exception:
#         print("Valor Invalido")

# --------------------------------------------------------------------------------

# Lista (Notas)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
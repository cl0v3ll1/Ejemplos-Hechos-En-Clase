# --------------------------------------------------------------------------------

# Diccionario ( hecho por el profe, funciona¿? )

# dic={
# "nombre": "Diego Robles",
# "numero": 79873432,
# "casado": True,
# "empleado": True,
# "direccion": "Los Claveles #456"
# }

# print(dic)

# dic["edad"]=64

# print(dic)

# dic["empleado"]=False

# print(dic)

# --------------------------------------------------------------------------------

# Diccionario ( Menu )

# corredores=["Ohio King", "Quandale Dingle", "John Pork"]
# tiempos=[10.9, 11.1, 12.5]

# while True:

#     try:
#         print('''
#         1.-Registrar Corredor y tiempo
#         2.- Ver listado de corredores
#         3.- Ver estadisticas
#         4.- Salir
#         ''')

#         op=int(input("Seleccione una opcion"))

#         match op:

#             case 1:

#                 corre=input("Ingrese el nombre del corredor")
#                 corredores.append(corre)
#                 tie=float(input("Ingrese su mejor tiempo"))
#                 tiempos.append(tie)

#             case 2:

#                 for i in range(len(corredores)):
#                     print(f"Corredor: {corredores[i]}, Tiempo: {tiempos[i]}")

#             case 3:

#                 print("El tiempo mas rapido es", min(tiempos))
#                 print("El tiempo mas lento es", max(tiempos))
#                 print("El tiempo mas lento al mas rapido")

#                 tiempos.sort()
#                 print(tiempos)

#             case 4:

#                 print("Saliendo")
#                 break

#             case _:

#                 print("Opcion invalida")

#     except Exception as e:
#         print("Error:", e)

# --------------------------------------------------------------------------------

# Diccionario ( Menu ( agregar, eliminar y actualizar precios ) )

# productos={
#     "lapiz": 100,
#     "goma": 100,
#     "estuche": 500,
#     "plumon":1000,
# }

# while True:

#     try:
#         print('''
#         1.- Agregar articulo y precio
#         2.- Ver listado
#         3.- Borrar articulo
#         4.- Actualizar precio
#         5.- Salir
#         ''')

#         op=int(input("Seleccione un a opcion \n"))

#         match op:

#             case 1:

#                 art=input("Ingrese el nombre del articulo \n")
#                 precio=int(input ("Ingres el precio del articulo \n"))
#                 productos[art]=precio

#             case 2:

#                 for nom, precio in productos.items():
#                     print(nom, "$", precio)

#             case 3:

#                 borrar=input("¿Cual es el articulo que quiere borrar? \n")
#                 del productos[borrar]
#                 print(f"El articulo {borrar} fue borrado")

#             case 4:

#                 for nom, precio in productos.items():
#                     print(nom, "$", precio)
#                 art=input("¿Cual es el precio que quiere actualizar? \n")

#                 if art in productos:
#                     precio=int(input("Ingrese el precio nuevo: \n"))
#                     productos[art]=precio
#                 else:
#                     print("El articulo no existe")

#             case 5:

#                 print("Saliendo")
#                 break

#             case _:

#                 print("Opcion invalida")

#     except Exception as error:
#         print("Error, hiciste algo mal:", error)

# --------------------------------------------------------------------------------

# Diccionario ( Sistema log In)

# Hacer un sistema de login con diccionario
# Debe verificar si el usuario existe
# de existir le pregunta la contaseña
# y da solo 3 oportunidades para acertar
# El diccionario debe de estar previamente
# escrito antes de iniciar el sistema

# listado_usuarios=["usuario": "pipe", "pass": 3344]

# usuarios={
# "pipe": 3344,
# "lola": 6655
# }



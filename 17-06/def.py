
# def suma_print():
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print(n1+n2)

# def suma_return():
#     n1=int(input("ingrese un numero: "))
#     n2=int(input("ingrese otro numero: "))
#     return n1+n2

# resultado=suma_return()

# print(resultado)

# def calc_desc(precio, desc):
#     return precio*(desc/100)

# p=int(input("Ingrese el precio: "))
# d=int(input("Ingrese el descuento: "))
# midesc=calc_desc(p,d)
# print( "El descuento es de ", midesc)
# print("El precio a pagar es ", p-midesc )


# print(list_prod[0]["nombre"])

# print(list_prod)

# list_prod.insert(0,{"nombre":"paleta", "precio":14000})

# print(list_prod)


# productos=[

#     {"nombre": "pelota", "precio":24000},
#     {"nombre": "queso", "precio":1700},
#     {"nombre": "azucar", "precio":900},
# ]

# def producto_y_precio():
#     nom=input("Ingrese el nombre del producto: ")
#     pre=int(input("Ingrese el precio: "))
#     productos.insert(0,{"nombre":nom, "precio":pre})

# def mostrar_productos():
#     for p in productos:
#         print(p)

# def actualizar_productos():
#     for n, p in enumerate(productos):
#         print(n+1, ".- ", p)
#     for i in range(len(productos)):
#         print(i+1, ".-", productos[i])

#     opc=int(input("Seleccione el producto a actualizar"))
#     print(productos[opc-1])

#     nn=input("Ingrese nuevo Nombre")
#     np=int(input("Ingrese nuevo Precio"))

#     productos[opc-1]["nombre"]=nn
#     productos[opc-1]["precio"]=np

#     print("Articulo actualizado!")

# while True:
#     try:
#         print('''
#             1.- Agregar producto
#             2.- Mostrar Productos
#             3.- Actualizar producto
#             4.- Borrar Producto
#             5.- Salir
#             ''')
        
#         op=int(input("Seleccione una opcion: "))
#         match op:
#             case 1:
#                 producto_y_precio()

#             case 2:
#                 mostrar_productos()

#             case 3:
#                 actualizar_productos()

#             case 5:
#                 break

#             case _:
#                 print("Opcion invalida")

#     except Exception:
#         print("Solo numeros enteros")

personas=[

1:{"Nombre": "Benjamin Aguilera",
   "Telefono": 56978452084,
   "Estado civil": "Soltero"}
2:{"Nombre": "Javier Canales",
   "Telefono": 56984750937,
   "Estado civil": "Soltero"}
3:{"Nombre": "Daeveth Manriquez",
   "Telefono": 56987549612,
   "Estado civil": "Casado"}
]

personas
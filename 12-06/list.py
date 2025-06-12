productos=["Disco SSD 1TB", "Memoria Ram 8GB", "Mouse"]
precios=[70000, 30000, 15000]
carrito=[]

while True:
    print('''
        1.- Ingresar productos a la tienda
        2.- Comprar
        3.- Crear Boleta
        4.- Salir
          ''')
    op=int(input("Ingese una opcion: "))
    match op:
        case 1:
            pro=input("Ingrese el nombre del Producto: ")
            productos.append(pro)
            pre=int(input("Ingrese el Precio: "))
            precios.append(pre)
        case 2:
                for i in range(len(productos)):
                    print(i+1, ".-", productos[i], "$", precios[i] )
                pro=int(input("Selecione que quiere comprar: "))
                carrito.append(pro-1)
                print(carrito)
        case 3:
            total=0
            print("---------------0----------------")
            print("Bienvenido a PC House ")
            for i in carrito:
                  print( productos[i], "----- $", precios[i] )
                  total=total+precios[i]
            print("Es total de articulos es", len(carrito))
            print("Su total neto es ", total)
            print("Su total mas iva es ", total*1.19)
            print("---------------0----------------")

        case 4:
            print("Saliendo")
            break
        case _:
            print("opcion invalida")
    

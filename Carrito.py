
totalneto=0
cantidaddeproductos=0
while True:
    print("Este es un carrito de compras")
    print('''
    ¿Que desea hacer?
    1.- Ingresar tu nombre" 
    2.- Eligir productos a comprar" 
    3.- Sacar boleta
    4.- Salir
    ''')

    opcion=input(int())

    while True:
        match opcion:
            case 1:
                print("Ingrese su nombre")
                nom=input()
            case 2:
                print('''
                ¿Que desea llevar?  
                1.- Pasta de dientes [$2000] 
                2.- Jugo de naranja [$1500] 
                3.- Mantequilla de mani [$4000]
                4.- Crema batida [$5000]
                5.- Toallitas humedas [$2500]
                6.- Papel higienico [$4500]
                7.- Salir
                ''')

                while True:
                    match opcion:
                        case 1:
                            totalneto+=2000
                            cantidaddeproductos+=1
                        case 2:
                            totalneto+=1500
                            cantidaddeproductos+=1
                        case 3:
                            totalneto+=4000
                            cantidaddeproductos+=1
                        case 4:
                            totalneto+=5000
                            cantidaddeproductos+=1
                        case 5:
                            totalneto+=2500
                            cantidaddeproductos+=1
                        case 6:
                            totalneto+=4500
                            cantidaddeproductos+=1
                        case 7:
                            break
                        case _:
                            print("Opcion invalida.")
        
            case 3:

            case 4: break
            
            case_:


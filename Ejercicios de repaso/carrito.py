# Carrito

totalneto=0
cantidaddeproductos=0

while True:
        try:
         print("Este es un carrito de compras")
         print('''
         ¿Que desea hacer?
         1.- Ingresar tu nombre
         2.- Eligir productos a comprar
         3.- Sacar boleta
         4.- Salir
         ''')

    
         opcion=int(input())

         match opcion:
                case 1:
                       nom=(input("Ingrese su nombre \n"))
            
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
                        
                        opcion=int(input())

                        match opcion:
                                case 1:
                                        totalneto+=2000
                                        cantidaddeproductos+=1
                                        print("Se ha añadido [Pasta de dientes]")
                                case 2:
                                        totalneto+=1500
                                        cantidaddeproductos+=1
                                        print("Se ha añadido [Pasta de dientes]")
                                case 3:
                                        totalneto+=4000
                                        cantidaddeproductos+=1
                                        print("Se ha añadido [Pasta de dientes]")
                                case 4:
                                        totalneto+=5000
                                        cantidaddeproductos+=1
                                        print("Se ha añadido [Pasta de dientes]")
                                case 5:
                                        totalneto+=2500
                                        cantidaddeproductos+=1
                                        print("Se ha añadido [Pasta de dientes]")
                                case 6:
                                        totalneto+=4500
                                        cantidaddeproductos+=1
                                        print("Se ha añadido [Pasta de dientes]")
                                case 7:
                                        break
                                case _:
                                        print("Opcion invalida.")
        
                case 3:
                 print("BOLETA DE COMPRA")
                 print(f"Cliente: {nom}")
                 print(f"Productos comprados: {cantidaddeproductos}")
                 print(f"Total Neto: ${totalneto}")

                 iva=totalneto*0.19
                 total_final=totalneto+iva

                 print(f"IVA (19%): ${iva:.0f}")
                 print(f"TOTAL A PAGAR: ${total_final:.0f}")

                case 4:
                 print("Gracias por usar el sistema, vuelva pronto")
                 break
            
                case _:
                 print("Opcion invalida")

        except Exception:
              print("Solo Usar numeros enteros")
        
            
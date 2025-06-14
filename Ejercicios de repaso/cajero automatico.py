import time

def Menu():
    
    print('''
Este es un menu calculadora       

¿Que desea hacer?
1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir
5.- Salir
''')

while True:
    try:
        Menu()
        opc=int(input())

        match opc:
            case 1:
                while True:
                    try:
                        num1=int(input("Ingrese su primer numero \n"))
                        num2=int(input("Ingrese su segundo numero \n"))
                        print("Sumando numeros, espere...")
                        time.sleep(2)
                        print(f"La suma de los dos numeros es {num1+num2}")
                        break
                    except Exception:
                        print("Opcion Invalida. Solo numeros ENTEROS")
                    
            case 2:
                while True:
                    try:
                        num1=int(input("Ingrese su primer numero \n"))
                        num2=int(input("Ingrese su segundo numero \n"))
                        print("Restando numeros, espere...")
                        time.sleep(2)
                        print(f"La resta de los dos numeros es {num1-num2}")
                        break
                    except Exception:
                        print("Opcion Invalida. Solo numeros ENTEROS")
            case 3:
                while True:
                    try:
                        num1=int(input("Ingrese su primer numero \n"))
                        num2=int(input("Ingrese su segundo numero \n"))
                        print("Multiplicando numeros, espere...")
                        time.sleep(2)
                        print(f"La multiplicacion de los dos numeros es {num1*num2}")
                        break
                    except Exception:
                        print("Opcion Invalida. Solo numeros ENTEROS")
            case 4:
                while True:
                    try:
                        num1=float(input("Ingrese su primer numero \n"))
                        num2=float(input("Ingrese su segundo numero \n"))
                        print("Diviendo numeros, espere...")
                        time.sleep(2)
                        print(f"La Division de los dos numeros es {num1/num2:.1f}")
                        break
                    except Exception:
                        print("Opcion Invalida. Solo numeros ENTEROS")
            case 5:
                print("Saliendo del programa")
                break

            case _:
                print("Opcion invalida. Intentelo denuevo")
            
    except Exception:
        print("Opcion Invalida. Solo numeros ENTEROS")

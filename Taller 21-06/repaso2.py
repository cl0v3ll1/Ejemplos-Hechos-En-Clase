perros={
    1: {"Nombre": "Frida",
        "Raza": "Calico",
        "Codigo": "0012"},

    2: {"Nombre": "Max",
        "Raza": "Labrador",
        "Codigo": "0013"},
        
    3: {"Nombre": "Luna",
        "Raza": "Poodle",
        "Codigo": "0014"}
}


def mostrar_perros(dict):
    for key, perro in dict.items():
        print(f"ID: {key}, Nombre: {perro['Nombre']}, Raza: {perro['Raza']}, Codigo: {perro['Codigo']}")

while True:

    try:
        print('''
1.- Registrar un perro
2.- Mostrar perros
3.- Actualizar perro
4.- Eliminar perro
5.- Salir
''')
        
        opc=int(input("Seleccione una opcion: \n"))
                
        match opc:

            case 1:
                nombre=input("Ingrese el nombre del perro: \n")
                raza=input("Ingrese la raza del perro: \n")
                codigo=input("Ingrese el codigo del perro: \n")

                largo=list(perros.keys())[-1]
                perros[largo+1]={"Nombre": nombre,
                                 "Raza": raza,
                                 "Codigo": codigo}

            case 2:
                mostrar_perros(perros)
            
            case 3:
                mostrar_perros(perros)
                act=int(input("Ingrese el ID del perro que va a actualizar: \n"))
                if act in perros:
                    print('''
1.- Nombre
2.- Raza
3.- Codigo
''')
                    
                    dato=input("¿Qué dato va a actualizar?: \n")
                    match dato:
                        
                        case "1":
                            n = input("Ingrese el nuevo nombre: ")
                            perros[act]["Nombre"]=n
                        case "2":
                            n = input("Ingrese la nueva raza: ")
                            perros[act]["Raza"]=n
                        case "3":
                            n = input("Ingrese el nuevo código: ")
                            perros[act]["Codigo"]=n
                        case _:
                            print("Opción no válida.")
                else:
                    print("Perro no encontrado.")

            
            case 4:
                mostrar_perros(perros)
                borrar=int(input("Ingrese el ID del perro a eliminar: \n"))
                if borrar in perros:
                    del perros[borrar]
                    print(f"Perro {borrar} fue eliminado.")
                else:
                    print("Perro no encontrado.")

            
            case 5:
                print("Saliendo...")
                break
        
    except Exception as e:
        print("El error es, ", e)
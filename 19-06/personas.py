def agregarpersonas():
                
                print("Ingrese los datos de la persona")

                name=input("Ingrese su nombre: \n")

                number=int(input("Ingrese su numero: \n"))

                while True:
                    try:

                        relationship=int(input('''¿Cual es su estado civil?: 
1.- Casado 2.- Solero
\n'''))
                        
                        if relationship==1:
                            civilstate="Casado"
                            break
                            
                        elif relationship==2:
                            civilstate="Soltero"
                            break
                            
                        else:
                            print("Opcion invalida")
                    except Exception:
                        print("Valor Invalido")
                        
                while True:
                    try:

                        work=int(input('''¿Esta trabajando?: 
1.- Si 2.- No
\n'''))
                        
                        if work==1:
                            working=True
                            break
                        elif work==2:
                            working=False
                            break
                        else:
                            print("Opcion invalida")
                    except Exception:
                        print("Valor Invalido")

                age=int(input("Ingrese su edad: \n"))
                
                guh=len(personas)+1
                personas[guh]={"nombre": name,
                             "numero":number,
                             "estado civil": civilstate,
                             "trabajando": working,
                             "edad": age}

def mostrarpersonas():
      
      for n, persona in personas.items():
                    print(f'''
{persona["nombre"]}
{persona["numero"]}
{persona["estado civil"]}
{persona["trabajando"]}
{persona["edad"]}''')

personas={

    1:{"nombre": " Benjamin Aguilera",
       "numero":956784573,
       "estado civil": "Soltero",
       "trabajando": True,
       "edad": 19},

    2:{"nombre": " Daeveth Manriquez",
       "numero":931845769,
       "estado civil": "Casado",
       "trabajando": True,
       "edad": 19},

    3:{"nombre": " Diego Rivera",
       "numero":97834231,
       "estado civil": "Casado",
       "trabajando": True,
       "edad": 42}
}


while True:
    try:
        print('''
1.- Ingresar Persona
2.- Mostrar listado
3.- Actualizar persona
4.- Borrar persona
5.- Salir
''')
        op=int(input("Seleccione una opcion"))

        match op:
             
            case 1:
                agregarpersonas()
            
            case 2:
                mostrarpersonas()
                    
            case 3:
                  

#                 for k in enumerate(personas):
#                     print(k+1)
#                     for n, persona in personas.items():
#                         print(f'''
# {persona["nombre"]}
# {persona["numero"]}
# {persona["estado civil"]}
# {persona["trabajando"]}
# {persona["edad"]}''')
                
#                 act=int(input("Seleccione cual desea actualizar"))
#                 nombre=input("ingrese el nombre ")
#                 precio=int(input("ingrese el nombre del precio"))
#                 personas[act-1]["nombre"]=nombre
#                 personas[act-1]["precio"]=precio

                
#                 opc=int(input("¿Que persona desea actualizar?: \n"))
                
            case 4:

                mostrarpersonas
                    
                borrar=input("¿Que persona desea eliminar?: \n")
                del personas[borrar]
                print(f"La persona {borrar} fue eliminada")
                
            case 5:
                break
            case _:
                print("Opcion invalida")
    except Exception as e:
        print("EL error es: ", e)
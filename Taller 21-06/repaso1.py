# -------------------------------------------------------------------------------

# # Valicaciones de datos

# email=input("Ingrese su email: ")

# # verifico si el caracter @ existe en mi variable

# if "@" in email:
#     print("La variable tiene formato mail")
# else:
#     print("La variable NO tiene formato mail")

# -------------------------------------------------------------------------------

# # Validar una clave solo de nuemros enteros

# while True:
#     try:
        # clave=int(input("Ingrese su clave"))
#         break
#     except Exception:
#         print("Error, solo ingrese numeros")

# -------------------------------------------------------------------------------

# # Validar una clave por su largo , por lo menos 5

# clave=input("Ingrese su clave: ")

# # verifico que tenga al menos 5 caracteres
# # la funcion len() verifica el largo de un objeto
# # en este caso la variabble clave    

# if len(clave)>=5:
#     print("La clave tiene el largo correcto")

# else:
#     print("La clave debe tener el menos 5 caracteres")

# # Ahora verifica que tenga al menos 5 y menor o igual a 12

# if len(clave)>=5 and len(clave)<=12:
#     print("La clave tiene el largo correcto")

# else:
#     print("La clave debe tener el menos 5 caracteres y menos de 12")

# -------------------------------------------------------------------------------
  
# # Verifico si tengo mayusclas y/o minisculas
# # y tiene por lo menos un numero, y tambien el largo

# tieneMayus=False
# tieneMinus=False 
# tieneNumero=False

# while True:

#     clave=input("Ingrese su clave: ")

#     # Hacemos un recorrido de cada letra en mi clave

#     for letra in clave:
#         # Verifico si la letra es mayuscula
#         if letra.isupper():
#             tieneMayus=True
#         # Verifico que la letra es minuscula
#         if letra.islower():
#             tieneMinus=True
#         # Verifico si tiene por lo menos un numero
#         if letra.isdigit():
#             tieneNumero=True
            
            
#     if tieneMayus:
#         print("Tiene por lo menos una mayuscula")
#     else:
#         print("NO tiene por lo menos una mayuscula")

#     if tieneMinus:
#         print("tiene por lo menos una minuscula")
#     else:
#         print("NO Tiene por lo menos una miniscula")

#     if tieneNumero:
#         print("tiene por lo menos un numero")
#     else:
#         print("No tiene por lo menos un numero")


#     if len(clave)>=5 and len(clave)<=12:
#         print("La clave tiene el largo correcto")

#     else:
#         print("La clave debe tener el menos 5 caracteres y menos de 12")

#     if tieneMayus and tieneMinus and tieneNumero and len(clave)>=5 and len(clave)<=12:
#         print("La clave esta ok")
#         break


#     else:
#         print("Debe intentar nuevamente")


# -------------------------------------------------------------------------------

#Caracteres especiales en clave

# specials="!#$%&/()=?*{}[]"
# clave=input("Ingrese su clave: \n")

# for caracter in clave:
#     if caracter in specials:
#         print(f"El caracter {caracter} es especial")

# -------------------------------------------------------------------------------

  
clave="Tredf99" 

def valida_pass(clave):
    Mayuscula=False
    Minuscula=False
    Numero=False

    for palabra in clave:
        if palabra.isupper():
            Mayuscula=True
        if palabra.islower():
            Minuscula=True
        if palabra.isdigit():
            Numero=True
    if Mayuscula and Minuscula and Numero and len(clave)>=5 and len(clave)<=12:
        print("la clave está bien escrita")
        return True
    else:
        print("la clave está mal escrita")
        return False

valida_pass(clave)
'''
Crear gestion de vehiculos
Crear programa para un parking de autos
se debe ingresar
Marca, año, patente, Tipo

Marca: tipo string, se debe tipear la marca
año: tipo int , solo de 4 digitos enteros
patente: debe tener 4 letras minusculas y 2 digitos
tipo: S= sedan, C= Camioneta, M= moto

Se deve validar cada aspecto y tener un mantenedor para 
todos los vehiculos motorizados

1.- Ingresar Vehiculo c
2.- Mostrar Vehiculos r
3.- Actualizar Vehiculo u
4.- Borrar Vehiculo d
5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage extra
6.- Salir 

Usar dunciones con argumentos para poder validar
y para poder llamar las acciones dentro del menu
'''
def checkcode(patent):
    minuscula=0
    numero=0

    for letra in patent:
        if letra.islower():
            minuscula+=1
        if letra.isdigit():
            numero+=1
    if minuscula==4 and numero==2:
        print()
            



def create(dic):
    auto=input("Ingrese el color del auto: \n")
    marca=input("Ingrese la marca del auto: \n")
    año=int(input("Ingrese el año del auto: \n"))
    largo=list(dic.keys())[-1]

    dic[largo+1]={
        "auto": auto,
        "marca": marca,
        "año": año,
        "patente": "tuvw12"}
    # patente=

def read(dic):

    for n, auto in dic.items():
        print(n, auto)


def delete(dic):

    read(dic)
    borrar=int(input("¿Que auto desea borrar?: \n"))
    del dic[borrar]

autos={
    1: {
        "auto": "rojo",
        "marca": "mazda",
        "año": 2015,
        "patente": "lmno78"},

    2: {
        "auto": "azul",
        "marca": "honda",
        "año": 2020,
        "patente": "pqrs90"},

    3: {
        "auto": "negro",
        "marca": "ford",
        "año": 2018,
        "patente": "tuvw12"},
}

read(autos)
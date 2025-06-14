#Domingo de pascua

# Preguntar la cantidad de niños de niños que buscan huevitos de chocolates
# Cuando se termine la busqueda, preguntar cantos huevos encontró cada uno
# y clasificarlos de la sigueinte forma
# Menos de una docena: NOOB
# Entre una docena a 24: Master
# 25 huevos o mas : Legend

# Mostrar resumen, y mostrar la mayor cantida de huevitos encontrados por un solo niño

import random

while True:
        
        noob=0
        pro=0
        legend=0

        top=0
        
        cantniños=int(input("¿Cuantos niños van a participar en la busqueda? \n"))

        while cantniños<0:
            print("No existen niños en numeros negativos o decimales (jerk) \n" \
            "Intentalo denuevo")

            cantniños=int(input("¿Cuantos niños van a participar en la busqueda"))

        for n in range(cantniños):
            canthuevos=random.randint(5,30)
            if canthuevos>top:
                top=canthuevos
            print(f"El niño {n+1} encontro {canthuevos} huevos (eggs)")
            if canthuevos<12:
                    noob+=1
            elif canthuevos>=12 and canthuevos<=24:
                pro+=1
            else:
                legend+=1

        print(f'''
        La cantidad de noobs es {noob}
        La cantidad de pros es {pro}
        La cantidad de legends es {legend}
        ''')
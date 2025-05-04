# while - contraseña 
# contraseña=1904

# clave=int(input("Ingresa tu clave de 4 digitos "))
# while clave!=contraseña:
#     print("ERROR: clave incorrecta")
#     clave=int(input("Ingresa tu clave de 4 digitos "))

# print("Logged in")

# if - edad
# print("Ingresa tu edad")
# edad=int(input())
# if edad>=18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted es menor de edad")

# categorizar jugadores
# en una liga amateour, se paga a los jugadores de futbol
# cuando anota mas goles recibe un bono en su paga entre 1-3 goles, 4%; entre 4-6 goles 6%; 7 goles o mas 8% //
# si su equipo queda entre los 3 primeros, +3000 
# si su equipo queda entre 4-8, +2000
# si su equipo queda entre 9 y mas, +1000
# El pago base por jugador es de 5000

import random
for i in range (1,11):
    for j in range (1,11):
        goles=random.randint(1,10)
        paga=5000
        puesto=random.randint(1,10)

        print(f"El jugador {i} saco {goles} goles")

        if goles>=1 and goles<=3:
            paga+=5000*0.04
            print(f"El jugador saco un bono de {5000*0.04:.0f}")
            print(f"La paga es de {paga:.0f}")
        elif goles>=4 and goles<=6:
            paga+=5000*0.06
            print(f"El jugador saco un bono de {5000*0.06:.0f}")
            print(f"La paga es de {paga:.0f}")
        elif goles>=7 and goles<=10:
            paga+=5000*0.08
            print(f"El jugador saco un bono de {5000*0.08:.0f}")
            print(f"La paga es de {paga:.0f}")

        print(f"El equipo {j} quedo en el puesto {puesto}")

        if puesto>=1 and puesto<=3:
            paga+=3000
            print(f"El jugador {i} gano {paga:.0f}")
        elif puesto>=4 and puesto<=8:
            paga+=2000
            print(f"El jugador {i} gano {paga:.0f}")
        elif puesto>=9 and puesto<=10:
            paga+=1000
            print(f"El jugador {i} gano {paga:.0f}")

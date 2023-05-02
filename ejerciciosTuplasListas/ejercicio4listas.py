from random import randint

numerosaloteria=[0]*4

for i in range(4):
    
    numerosaloteria[i]=randint(1,9)

print(f"los numeros ganadores de la loteria son los siguientes {numerosaloteria}" )


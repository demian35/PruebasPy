print("ingrese un numero entero")
numero=int(input())

suma=0

for i in range(1,numero):
    suma=numero*(numero+1)/2
   

print(suma)

tipo=type(suma)
print(tipo)
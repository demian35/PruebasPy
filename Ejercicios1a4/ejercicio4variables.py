print("gasto de comboustible por kilometros recorridos")

print("ingrese los kilometros recorridos")
km=int(input())

print("ingrese la cantidad de combustible consumido")
lts=float(input())

combustibleConsumido=km/lts
print(f"El consumo de gasolina por km es de {combustibleConsumido} ")
tipo=type(combustibleConsumido)
print(tipo)
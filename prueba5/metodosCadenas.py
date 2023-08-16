cadena1= "Hola soy Booker Dewitt"

#metodo lower() para convertir caracteres de una cadena a minusculas
cadenaminusculas=cadena1.lower()

#funcion para transformar toda una cadena a mayusculas recibe como parametro una cadena y la regresa transformada
def converteMayus(cadena):
    cadenaMayus=cadena.upper()
    return cadenaMayus

mayus= converteMayus(cadena1)

print(mayus)
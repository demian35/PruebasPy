cadena1= "Hola soy Booker Dewitt"
cadena3="Minumerodeserieesel23124"
cadena2="123452"

#metodo lower() para convertir caracteres de una cadena a minusculas
cadenaminusculas=cadena1.lower()

#funcion para transformar toda una cadena a mayusculas recibe como parametro una cadena y la regresa transformada
def converteMayus(cadena):
    cadenaMayus=cadena.upper()
    return cadenaMayus

mayus= converteMayus(cadena1)

#metodo que verifica que una funcion es numerica
cadenaNumerica=cadena2.isnumeric()

#metodo que verifica que una cadena es alfa numerica(no acepta espacios)
cadenaAlfnum=cadena3.isalnum()


print(cadenaAlfnum)
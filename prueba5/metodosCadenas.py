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

#funcion que cuenta las ocurrencias de una cadena en una cadena
def occurrencias(cadena):
    occurrenciasCadena=cadena1.count(cadena)
    return occurrenciasCadena

numeroOcurrencias=occurrencias("Hola")

#funcion para reemplazar caracteres de una cadena recibe el candidato a reemplazar y su reemplazo
def reemplazaCaracteres(candidato,charNuevo):
    cadenaNueva=cadena1.replace(candidato,charNuevo)
    return cadenaNueva

nuevaCadena=reemplazaCaracteres(" ",",")

#funcion para dividir una cadena, le pasamos el caracter que delimitara las cadenas para dividir
def divideCadena(delimitador):
    cadenadividida=cadena1.split(delimitador)
    return cadenadividida

cadenadividida=divideCadena(" ")

#funcion que busca una cadena dentro de una cadena , regresa el indice donde esta la cadena buscada
def encuentraCadena(cadena):
    cadenaEncontrada=cadena1.find(cadena)
    return cadenaEncontrada

resultado=encuentraCadena("De")

print(resultado)

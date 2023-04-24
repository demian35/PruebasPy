#listas almacenan cualquier elemento
lista1=["cadena","cadena2",True,False,4]


#creamos una tupla de cuatro elementos
tupla=("cadena","cadena2",True,False,4)


#imprimimos lista
print(lista1)

#cambiando el valor del elemento en el indice 4
lista1[4]=True
#imprimimos elemento por el indidce donde esta almacenado un elemento
print(lista1[4])

#imprimimos nueva lista
print(lista1)

#imprimimos la tupla
print(tupla)

#imprimimos un elemento de la tupla por su indice
print(tupla[0])

#tipo de dato conjunto (set) aqui no se puede acceder a los elementos por medio de indices ni se imprimen elementos repetidos
conjunto={1,2,4,2,3,5}

print(conjunto)

#tipo de dato diccionaro la estructura es  'palabra´ : "valor(significado)"
diccionario={
    'Nombre': "demian",
    'Posicion': "Portero",
    'Club': "Club Universidad AC",
    'Edad': 36,
    'Nacionalidad':"Mexico",
    'Toma': "True"
}

#imprimimos el diccionario
print(diccionario)
tipo1=type(tupla)

#imprimimos el valor de la nacionalidad en el diccionario
print(diccionario['Nacionalidad'])

#manipulacion de dato del diccionario sumandole dos a la edad
print(diccionario['Edad'] + 2)
print(tipo1)

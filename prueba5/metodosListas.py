lista=list(["Dewitt","hola",2,3,4,False])
lista2=[4,6,3,2,4,6]

#metodo para agregar un elemento a una lista
lista.append(7)

#metodo para agregar un elemento en un indice en especifico
lista.insert(3,"Booker")

#metodo para ordenar los elementos de una lista el metodo no acepta cadenas
lista2.sort()

#metodo para eliminar elementos de una lista se le pasa el indice que queremos eliminar si no elimina el ultimo elemento
lista.pop(4)

print(lista)
print(lista2)

#imprimimos la longitud de la lista
print(len(lista))

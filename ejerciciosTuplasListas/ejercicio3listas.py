materias=["algebra","programacion", "calculo", "administracion"]

calif=[]

#asignamos un valor a cada elemento de la lista guardando los valores en ptra lista
for i in materias:  
    print("Yo estudio " + i )
    calificacion=input("cuanto sacaste en " + i +"?")
    calif.append(calificacion)

#imprimimos los valores ya asignados al elemento de la lista
for i in range(len(materias)):
    print("En " +materias[i] +"tu sacaste " + calif[i])
    


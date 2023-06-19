#metodo len devuleve caracteres que tiene una cadena


cadena1 = "ASHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"

lenn = len(cadena1)


#si usamos el len con una lista,nos dice cuantos elementos contiene en vez de cuantos caracteres
lista = list(["Mati","Calderon",16,"matiacaldeproxd56@gmail.com"])
listaa = len(lista)


#agregando un elemento a la lista con append
lista.append("argentino")


#index es para agregar un elemento pero en un orden en especifico
lista.insert(5, "escorpiano")

#extend es para agregar varios elementos
lista.extend(["cibernetico","cuarto año secundaria"])



#eliminando un elemento por su indice
#para eliminar el ultimo elemento de la lista, se pone -1,si queremos el antepenultimo ponemos -2, y asi susesivamente
lista.pop(-1)

#remover un elemento por su valor
lista.remove("argentino")


                                                                                                    #elimina todo a la mierda , .clear()
# .sort ,ordena SOLAMENTE si son numeros y booleanos,si hay cadenas de texto salta error
#.sort(reverse=true) los ordena al reves


# .reverse es para invertir una lista con cualquier elemento
lista.reverse()


print(lista)

























































































































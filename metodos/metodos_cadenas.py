#print(dir(lista))
#muestra todo lo que podemos hacer con eso

cadena1 = "ASHEEEEEEEE"
cadena2 = "noo se que poner asi voy a estar improvisando con lo que me venga a la mente 11 en estos momentos de la actualidad"

  
mayusc = cadena2.strip()
minusc = cadena1.lower()
inicial_mayus = cadena1.capitalize()

#busqueda de una cadena
#recordar siempre se arranca del 0 a contar

busqueda = cadena2.find("n")
print(busqueda)

#index si no encuentra el dato que pusiste,va a devolverte un error
busqueda2 = cadena2.index("actualidad")

#contar caracteres
contar_caracteres = len(cadena2)





#ejemplo para eliminar espacios y preguntar si es alpha 
cadena2 = "no se que poner asi voy a estar improvisando con lo que me venga a la mente 11 en estos momentos de la actualidad" 
texto_sin_espacios = cadena2.replace(" ", "")
texto_sin_espacios = mayusc.isalpha()
contar_coincidencias = cadena2.count("a")




#devuelve true si es correcto la letra con la que empieza la cadena

empieza_con= cadena2.startswith("K")
 

cadena_termina = cadena2.endswith("d")

#remplazar texto
remplazar_texto = cadena2.replace("e" , "a")

#separar con comas
#[numero] para ver que palabra esta en ese lugar
separar_palabras = cadena2.split()
print(separar_palabras [2])

















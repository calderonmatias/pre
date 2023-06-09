cadena1 = "ASHEEEEEEEE"
cadena2 = "noo se que poner asi voy a estar improvisando con lo que me venga a la mente 11 en estos momentos de la actualidad"

  
mayusc = cadena2.strip()
minusc = cadena1.lower()
inicial_mayus = cadena1.capitalize()

#busqueda de una cadena
#recordar siempre se arranca del 0 a contar

busqueda = cadena2.find("n")


#index si no encuentra el dato que pusiste,va a devolverte un error
busqueda2 = cadena2.index("actualidad")


contar_caracteres = len(cadena2)
print(contar_caracteres)











cadena2 = "no se que poner asi voy a estar improvisando con lo que me venga a la mente 11 en estos momentos de la actualidad" 
texto_sin_espacios = cadena2.replace(" ", "")
print(texto_sin_espacios)

texto_sin_espacios = mayusc.isalpha()
print(texto_sin_espacios)
contar_coincidencias = cadena2.count("a")
print(contar_coincidencias)




#devuelve true si es correcto la letra con la que empieza la cadena

empieza_con= cadena2.startswith("K")
print(empieza_con) 





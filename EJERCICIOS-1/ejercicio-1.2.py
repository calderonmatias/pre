frase = input("Ingresa una frase y saber cuantas palabras hay y en cuanto tiempo las dirias: ")
cantidad_palabras = frase.split(" ")
total_palabras = len(cantidad_palabras)
print(f"Esta frase contiene {total_palabras} palabras y las dirias en {total_palabras/2} segundos")
print(f"Dalto lo diria en {total_palabras/2*1.3} segundos")
if total_palabras > 120:
    print("Para hermano hablá menos")



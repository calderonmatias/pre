#el bucle basicamente va a iterar todo lo que este dentro de por ejemplo un lista
#se ejecuta la cantidad de elementos que haya
#sirve para recorrer una lista



import time

numeros = [1,2,3,4,5]
numeros.sort(reverse=True)


for numero in numeros:
    print(f"La funcion comenzará en: {numero}")
    #time.sleep(1)
else:
    print("------------")

for numero in numeros:
    resultado = numero*4
    print(resultado)
    
    
#range
#ejecuta desde el primer parametro hasta un numero antes del ultimo parametro
#si le pasamos un solo parametro comenzara desde el 0 hasta el parametro

for num in range(4,10):
    print(num)
    
    
#forma correcta de recorrer una lista por su indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es {indice} y su valor es {valor}")
    
    
#el else en un bucle se usa al final del bucle para agregar algo mas




#el bucle basicamente va a iterar todo lo que este dentro de por ejemplo un lista
#se ejecuta la cantidad de elementos que haya
#sirve para recorrer una lista
import time
numeros = [1,2,3,4,5]
numeros.sort(reverse=True)



for numero in numeros:
    #print(f"El cohete depegará en {numero}")
    time.sleep(1)


for numero in numeros:
    resultado = numero*4
    print(resultado)












































#creando una animacion cohete


#import time
#import sys
#
#def rocket_animation():
#    print("¡Despegue del cohete!")
#    for i in range(5, -1, -1):
#        sys.stdout.write("\rEl cohete está despegando en {} segundos.".format(i))
#        sys.stdout.flush()
#        time.sleep(1)
#
#    # Borramos la última línea impresa
#    sys.stdout.write("\r" + " " * 50 + "\r")
#    sys.stdout.flush()
#
#    for _ in range(15):
#        sys.stdout.write("\r                 ¡¡¡        ")
#        time.sleep(0.2)
#        sys.stdout.write("\r                 ¡¡¡¡       ")
#        time.sleep(0.2)
#        sys.stdout.write("\r                 ¡¡¡¡¡¡     ")
#        time.sleep(0.2)
#        sys.stdout.write("\r                 ¡¡¡¡¡¡¡¡   ")
#        time.sleep(0.2)
#        sys.stdout.write("\r                 ¡¡¡¡¡¡¡¡¡¡ ")
#        time.sleep(0.2)
#
#    print("\rEl cohete ha alcanzado su destino. ¡Éxito!")
#
#if __name__ == "__main__":
#    rocket_animation()







    









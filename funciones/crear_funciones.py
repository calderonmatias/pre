#creando una funcion simple
def contraseña():
     print("contraseña123456789")
# contraseña()

#creando una funcion con parametro

def saludar(nombre,genero):
    genero = genero.lower()
    if (genero == "mujer"):
        adjetivo = "amiga"
    elif (genero == "hombre"):
        adjetivo = "toro"
    else:
        adjetivo = "crack"
    #print(f"Hola {nombre}, todo bien {adjetivo}")        
    
saludar("mati","hombre")


#crear funcion que nos retorn valores
#en este ejemplo le pedimos num_entero[0] y el 0 en un str es la primer letra

def crear_contraseña_random(num):
    chars = "abcdefghijklmn"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2 
    c2 = num + 1
    c3 = num - 10
    c4 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c4]}{num * 2}"
    return contraseña,num

#desempaquetando la funcion
password,num = crear_contraseña_random(111)
frase1 = f"tu nueva contraseña es: {password}"
frase2 = f"el numero que se utilizo para crear la contraseña fue: {num}"

print(frase1)
print(frase2)






     
     

#usando el continue para saltear un elemento
#continue salta el dato
comidas_argentinas = ["milanesas", "asado", "locro","empanadas","tortas fritas"]
for comidas in comidas_argentinas:
    if comidas == "empanadas":
        continue
    print(f"este domingo vamos a ir a comer de los abuelos y va a haber {comidas}")
    
    
    
    
    
    
    
    #el else no se ejecuta por el break
    
    comidas_argentinas = ["milanesas", "asado", "locro","empanadas","tortas fritas"]
for comidas in comidas_argentinas:
    if comidas == "empanadas":
        #break termina el bucle en dicho elemento
        break
    else:
        print("nada mas")
        
        

#recorrer un string

cadena = "ashei en octubre se pica ags bbto prendete a la fiesta faaaerte de ruta 9 nazzeeee"

for letra in cadena:
    print(letra)
    
    
#For en una sola linea de codigo
numeros = [1,2,3,4,5]
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)




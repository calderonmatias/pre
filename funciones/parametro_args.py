def suma(nombre,*numeros):
    return f"{nombre} la suma de tus numeros es: {sum(numeros)}"

resultado = suma("mati",1,414,23,531,31)
print(resultado)
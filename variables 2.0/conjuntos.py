conjunto = set(["dato1","dato2"])


#creando un conjunto dentro de otro connjunto
#el frozenset es para meter un conjunto dentro de otro
conjunto1 = frozenset(["dato21", "dato25"])
conjunto2 = {conjunto1, "dato1512"}


#teoria de conjuntos

conjunto24 = {1,5,7,8,9}
conjunto25 = {1,5,7}


#verificando si es un subconjunto
resultado = conjunto25.issubset(conjunto24)
#metodo con <> 
resultado = conjunto25 <= conjunto24



#verificar si es un superconjunto
conjunto30 = {1,452,2525,4141,414}
conjunto31 = {1,452,2525,4141}

resultado = conjunto30.issuperset(conjunto31)
resultado = conjunto30 > conjunto31

#verificar si hay algun resultado en comun si hay un elemento va a dar false

resultado = conjunto30.isdisjoint(conjunto31)
print(resultado)

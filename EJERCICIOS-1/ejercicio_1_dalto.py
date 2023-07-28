curso_otro_minimo = 2.5
curso_otro_promedio = 4
curso_otro_maximo = 7
curso_dalto  = 1.5

#crudo
crudo_promedio = 5
crudo_dalto = 3.5


print("--------------------------")

print("El curso de Dalto dura:")
# calcular porcentajes de duracion entre curs
porcentaje_entre_dalto_otro_curso_minim = round(100 - (curso_dalto / curso_otro_minimo * 100))
porcentaje_entre_dalto_otro_curso_prom = 100 - (curso_dalto / curso_otro_promedio * 100)
porcentaje_entre_dalto_otro_curso_max = 100 - (curso_dalto *1000 // curso_otro_maximo /10)


 
print (f" - el curso de dalto dura un {porcentaje_entre_dalto_otro_curso_minim}% menos que el mas rapido de los demas cursos de python")
print (f" - el curso de dalto dura un {porcentaje_entre_dalto_otro_curso_prom}% menos que un curso promedio de python")
print (f" - el curso de dalto dura un {porcentaje_entre_dalto_otro_curso_max}% menos que el mas lento de los demas cursos de python")

print("--------------------------")

#Ejercicio B calculando % de tiempo que se remueve

tiempo_vacio_curso_promedio = 100 - (curso_otro_promedio *1000 // crudo_promedio /10)
tiempo_vacio_curso_dalto = 100 - (curso_dalto *1000 // crudo_dalto /10)
print("Tiempo que se remueve de un curso:")
print(f" - En un curso promedio se remueve un {tiempo_vacio_curso_promedio}% del total")
print(f" - En un curso promedio se remueve un {tiempo_vacio_curso_dalto}% del total")
print("--------------------------")

# cuanto tiempo seria si durara 10 horas
print("Cuanto tiempo debo ver del otro curso si durara 10 horas:")
print(f" - ver 10 horas de este curso equivale a mirar {curso_otro_promedio *100 // curso_dalto /10} horas de otro curso")
print(f" - ver 10 horas de otro curso equivale a mirar {curso_dalto *100 // curso_otro_promedio /10} horas de este curso")
print("--------------------------")














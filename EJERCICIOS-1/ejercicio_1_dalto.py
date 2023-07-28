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
porcentaje_entre_dalto_otro_curso_minim = 100 - (curso_dalto / curso_otro_minimo * 100)
porcentaje_entre_dalto_otro_curso_prom = 100 - (curso_dalto / curso_otro_promedio * 100)
porcentaje_entre_dalto_otro_curso_max = 100 - (curso_dalto / curso_otro_maximo *100)

resultado_min = round(porcentaje_entre_dalto_otro_curso_minim,2)
resultado_prom = round(porcentaje_entre_dalto_otro_curso_prom,2)
resultado_max = round(porcentaje_entre_dalto_otro_curso_max,2)

 
print (f" - el curso de dalto dura un {resultado_min}% menos que el mas rapido de los demas cursos de python")
print (f" - el curso de dalto dura un {resultado_prom}% menos que un curso promedio de python")
print (f" - el curso de dalto dura un {resultado_max}% menos que el mas lento de los demas cursos de python")

print("--------------------------")

#Ejercicio B calculando % de tiempo que se remueve

tiempo_vacio_curso_promedio = 100 - (curso_otro_promedio / crudo_promedio *100)
tiempo_vacio_curso_dalto = 100 - (curso_dalto /crudo_dalto *100)
tiempo_vacio_curso_promedio = round(tiempo_vacio_curso_promedio,2)
tiempo_vacio_curso_dalto = round(tiempo_vacio_curso_dalto,2)
print("Tiempo que se remueve de un curso:")
print(f" - En un curso promedio se remueve un {tiempo_vacio_curso_promedio}% del total")
print(f" - En un curso promedio se remueve un {tiempo_vacio_curso_dalto}% del total")
print("--------------------------")

# cuanto tiempo seria si durara 10 horas


resultado_10hs_de_otro_curso = curso_otro_promedio *100 // curso_dalto /10
resultado_10hs_de_otro_curso_dalto = curso_dalto *100 // curso_otro_promedio /10
print("Cuanto tiempo debo ver del otro curso si durara 10 horas:")
print(f" - ver 10 horas de este curso equivale a mirar {round(resultado_10hs_de_otro_curso,1)} horas de otro curso")
print(f" - ver 10 horas de otro curso equivale a mirar {round(resultado_10hs_de_otro_curso_dalto,1)} horas de este curso")
print("--------------------------")














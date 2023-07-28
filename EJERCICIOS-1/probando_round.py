curso_otro_minimo = 2.5
curso_otro_promedio = 4
curso_dalto  = 1.5
curso_otro_maximo = 7


#porcentaje_entre_dalto_otro_curso_minim = 100 - (curso_dalto / curso_otro_minimo * 100)  
#porcentaje_entre_dalto_otro_curso_prom = 100 - (curso_dalto / curso_otro_promedio * 100)
porcentaje_entre_dalto_otro_curso_max = round(curso_dalto / curso_otro_maximo,2)

#print(round(porcentaje_entre_dalto_otro_curso_minim,2))
#print (f" - el curso de dalto dura un {porcentaje_entre_dalto_otro_curso_minim}% menos que el mas rapido de los demas cursos de python")
#print (f" - el curso de dalto dura un {porcentaje_entre_dalto_otro_curso_prom}% menos que un curso promedio de python")
#print (f" - el curso de dalto dura un {porcentaje_entre_dalto_otro_curso_max}% menos que el mas lento de los demas cursos de python")
print(porcentaje_entre_dalto_otro_curso_max)
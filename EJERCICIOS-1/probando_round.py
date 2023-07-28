curso_dalto  = 1.5
curso_otro_maximo = 7



porcentaje_entre_dalto_otro_curso_max = 100 - (curso_dalto / curso_otro_maximo *100 )
dalto_curosmax = round(porcentaje_entre_dalto_otro_curso_max,2)
print(dalto_curosmax)
# keys()        nos devuelve "procesador" "placa de video",etc 
# get()         nos devuelve el valor, si escribimos pc.get("procesador") nos va a dar ryzen 5 3600
#               si no encuentra la variable,devuelve "none"
# clear()       elimina todo el diccionario
# pop()         elimina una variable        pc.pop("procesador")
# items()       es lo mismo que keys solamente que keys no se puede iterar








pc = {
  "procesador" : "ryzen 5 3600",
  "placa de video" : "RX 570",
  "memoria ram" : "16Gb",
  "fuente" : "sentey de 550w certificada",  
  "placa madre" : "Asus prime A320-MK"
    
}

#ejemplo con key
claves = pc.keys()
print(claves) 

#ejemplo con get
claves = pc.get("procesador")
print(claves) 


#ejemplo con clear
#claves = pc.clear()
#print(claves) 

#ejemplo con get
pc.pop("placa de video")
print(pc)

#ejemplo con items
dic_iterable = pc.items()
print(dic_iterable)
























 
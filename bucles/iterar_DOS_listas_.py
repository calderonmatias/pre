import time
numeros = [100000,250000,3000000 , 200000,50000]


def capitalize_list_elements(provincias):
    return [item.capitalize() for item in provincias]

# Ejemplo de uso:
provincias = ["santa Fe", "cordoba", "buenas aires","santa cruz", "salta"]
provinciass = capitalize_list_elements(provincias)
print(provinciass)

for provincia,numero in zip(provinciass,numeros):
    print("------------------")
    print(f"provincia con buena zona turista: {provincia}")
    
    print(f"habitantes de {provincia}: {numero}")
    time.sleep(1)
print("------------------")
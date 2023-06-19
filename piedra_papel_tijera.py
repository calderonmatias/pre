while True:
    a= int(input("jugador 1: 1=piedra, 2=Papel, 3=Tijeras:"))
    b=int(input("jugador 2: 1=piedra, 2=Papel, 3=Tijeras:"))
    if a == 1 and b == 3:
        print("Gana jugador 1: Piedra rompe a la tijera")
    elif a == 2 and b == 1:
        print("gana el jugador 1: papel envuelve a la piedra")
    elif a == 3 and b == 2:
        print("gana jugador 1: Tijeras cortan al papel")
    elif b == 1 and a == 3:
        print("gana el jugador 2: piedra rompe a la tijera") 
    elif b == 2 and a == 1:
        print("gana el jugador 2: papel envuelve a la piedra")
    elif b == 3 and a == 2:
        print("gana jugador 2: Tijeras cortan al papel")      
    else:
        print("Ninguno gana!")  
    
    
        
        
        
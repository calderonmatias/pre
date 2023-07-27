#creando una animacion cohete


import time
import sys

def rocket_animation():
    print("¡Despegue del cohete!")
    for i in range(5, -1, -1):
        sys.stdout.write("\rEl cohete está despegando en {} segundos.".format(i))
        sys.stdout.flush()
        time.sleep(1)

    # Borramos la última línea impresa
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()

    for _ in range(15):
        sys.stdout.write("\r                 ¡¡¡        ")
        time.sleep(0.2)
        sys.stdout.write("\r                 ¡¡¡¡       ")
        time.sleep(0.2)
        sys.stdout.write("\r                 ¡¡¡¡¡¡     ")
        time.sleep(0.2)
        sys.stdout.write("\r                 ¡¡¡¡¡¡¡¡   ")
        time.sleep(0.2)
        sys.stdout.write("\r                 ¡¡¡¡¡¡¡¡¡¡ ")
        time.sleep(0.2)

    print("\rEl cohete ha alcanzado su destino. ¡Éxito!")

if __name__ == "__main__":
    rocket_animation()

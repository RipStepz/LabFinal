import threading
import random

# 10 por zonas inicial, se va rellenando al azar hasta que llegar al limite 256
def distribuir_cristales():
    zonas = [10] * 16              # 
    restantes = 96
    while restantes > 0:
        i = random.randint(0, 15)  
        if zonas[i] < 20:          
            zonas[i] += 1
            restantes -= 1

    return zonas

CantidadExtraer = random.randint(1,3)
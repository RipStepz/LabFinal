import random

class Zonas:

    def __init__(self, Cristales):
       
       self.Cristales = Cristales
       self.Trabajadores = 0
       self.clima = random.randint(10,50)
    
    def getCristales(self):
        return self.Cristales
    
    def getTrabajadores(self):
        return self.Trabajadores
    
    def getToxicidad(self):
        return self.clima
    
    # Si retorna 0 no puedes agregar un trabajador
    def UnirTrabajador(self):
        if(self.Trabajadores >= 8):
            return 0
        self.Trabajadores += 1
        return 1
    
    def QuitarTrabajador(self):
        self.Trabajadores -=1
    

    # Si retorna 1 si se puede, si retorna 0 no se puede extraer mas
    def SePuedeExtraer(self, CantidadExtraer):
        if (self.Cristales - CantidadExtraer >= 0):
            return 1
        return 0
    
    def Extraer(self, CantidadExtraer):
        self.Cristales -= CantidadExtraer
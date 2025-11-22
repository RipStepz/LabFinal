import random
class Trabajador:

    """
    ya que este lenguaje feo no tiene tipos de datos strictos definire yo los datos aqui
    int Resistencia entre [0,100], 100 base
    Int Mochila 10 espacios, 0 base
    String Estado Casos posibles "Activo" , "Agotado" , "Intoxicado"

    int CristalesExtraidosTotales Historial de cristales extraidos por la hebra
    String ZonasVisitadas es una lista de strings con las zonas visitadas por la hebra
    int RondasTrabajadas contador de rondas trabajadas por la hebra

    """

    def __init__(self, Resistencia , Mochila):
       
        #condiciones iniciales
        self.Resistencia = Resistencia 
        self.Mochila = Mochila
        self.Estado = "Activo"

        # Historial de la hebra
        self.CristalesExtraidosTotales = 0
        self.ZonasVisitadas = ()
        self.RondasTrabajadas = 0


    def GetResistencia(self):
        return self.Resistencia
    
    def GetMochila(self):
        return self.Mochila
    
    def GetEstado(self):
        return self.Estado
    
    def RecargarResistencia(self, aunmento):
        if (self.Resistencia + aunmento >= 100):
            self.Resistencia = 100
        else:
            self.Resistencia += aunmento

    def AunmentarCristal(self, cristales):
        if (self.Mochila + cristales >= 10):
            self.Mochila = 10
        else:
            self.Mochila += cristales
    
    def Accion(self, Cristales_A_Recolectar):
        if (Cristales_A_Recolectar == 1):
            self.Resistencia -= 5
        elif(Cristales_A_Recolectar):
            self.Resistencia -= 12
        else:
            self.Resistencia -= 20
        return Cristales_A_Recolectar
    
    # Los cristales recolectados se retornan para quitarlos de la zona
    def Recolectar(self, Cristales_A_Recolectar):

        CristalesRecolectados = self.Accion(self, Cristales_A_Recolectar)
        
        self.Mochila += CristalesRecolectados
        self.CristalesExtraidosTotales += CristalesRecolectados
        return CristalesRecolectados

    def Exposicion(self, Toxicidad, TrabajadoresEnZona):
        return Toxicidad/TrabajadoresEnZona

    # Si retorna 1, se comparte, caso contrario no se puede
    def compartir(self):
        if (self.Mochila >= 3):
            self.Mochila -= 3
            return 1
        else:
            return 0
    
    def recibir(self, Aceptado):
        if (Aceptado):
            self.AunmentarCristal(self, 3)
        else:
            pass
    
    def CambiarEstado(self):
        if(self.Resistencia > 20):
            pass
        elif(0 < self and self <= 20):
            self.Estado = "Agotado"
        else:
            self.Estado = "Intoxicado"

    # Si retorna 1 significa que tiene que abandonar una ronda la pega, si retorna 0 sigue trabajando
    def Agotado(self):
        if(self.Estado == "Agotado"):
            self.RecargarResistencia(self,30)
            return 1
        return 0
    
    # Si retorna 1 matar hebra si retorna 0 sigue trabajando
    def Intoxicado(self):
        if(self.Estado == "Intoxicado"):
            return 1
        return 0
class Trabajador:

    """
    ya que este lenguaje feo no tiene tipos de datos strictos definire yo los datos aqui
    int Resistencia entre [0,100], 100 base
    Int Mochila 10 espacios, 0 base
    String Estado Casos posibles "Activo" , "Agotado" , "Intoxicado"

    int CristalesExtraidosTotales Historial de cristales extraidos por la hebra
    String ZonasVisitadas es una lista de strings con las zonas visitadas por la hebra
    int RondasTrabajadas contador de rondas trabajadas por la hebra


    Se supone que para que por ejemplo Resistencia sea privado la convencion es __Resistencia, pero tomare todos como privado
    los tratare como tal, ya que en este lenguaje tampoco existe el privado
    """

    def __init__(self, Resistencia , Mochila, Estado):
       
        #condiciones iniciales
        self.Resistencia = Resistencia 
        self.Mochila = Mochila
        self.Estado = Estado

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
    
    def Accion(self, Resistencia):
        self.Resistencia -= Resistencia
        self.RondasTrabajadas += 1
        

    def Recolectar(self, CristalesRecolectados):
        
        self.Mochila += CristalesRecolectados

    def GetEstado(self):
        return self.Estado
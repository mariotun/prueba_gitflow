class Operacion_Suma:
    """Clase para operacion suma"""

    def __init__(self,n1,n2):
        self.numero1 = n1
        self.numero2 = n2
    
    def Suma(self):
        resultado = self.numero1+self.numero2
        return resultado

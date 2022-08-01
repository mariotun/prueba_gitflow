class MayorEdad:
    """Clase para verificar si es mayor de edad"""

    def __init__(self,edad):
        self.edad = edad
    
    def comprobarEdad(self):
        if self.edad >= 18:
            print('Es mayor de edad')
        else:
            print('Es menor de edad')
        

class MensajeBienvenida:
    """Clase para dar un mensaje de bienvenida"""

    def __init__(self,nombre,apellido,mensaje):
        self.nombre = nombre
        self.apellido = apellido
        self.mensaje = mensaje
    
    def Bienvenida(self):
        mensaje = f'Muy buenas, mi nombre es {self.nombre} {self.apellido} , {self.mensaje}'
        return mensaje

        

from src import req_mario,req_alex,req_josue

def main ():
    saludo = req_mario.MensajeBienvenida('mario','tun','esta es una practica simple de gitflow.')
    print(saludo.Bienvenida())


    operacion = req_alex.Operacion_Suma(12,6)
    print(operacion.Suma())

    mayorEdad = req_josue.MayorEdad(12)
    mayorEdad.comprobarEdad()


main()


from src import req_mario,req_josue

def main ():
    saludo = req_mario.MensajeBienvenida('mario','tun','esta es una practica simple de gitflow.')
    print(saludo.Mensaje())

    mayorEdad = req_josue.MayorEdad(12)
    mayorEdad.comprobarEdad()

main()


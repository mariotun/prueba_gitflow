from src import req_mario,req_alex

def main ():
    saludo = req_mario.MensajeBienvenida('mario','tun','esta es una practica simple de gitflow.')
    print(saludo.Mensaje())

    operacion = req_alex.Operacion_Suma(12,6)
    print(operacion.Suma())

main()


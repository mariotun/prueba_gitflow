from src import req_mario

def main ():
    saludo = req_mario.MensajeBienvenida('mario','tun','esta es una practica simple de gitflow.')
    print(saludo.Mensaje())

main()


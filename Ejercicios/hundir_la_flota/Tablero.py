class Tablero:
    'prueba fetch'
    def __init__(self, tamano):
        self.dimensiones = (tamano, tamano)
        self.casillas = [[0]*tamano for _ in range(tamano)]


if __name__ == "__main__":
    tablero = Tablero(5)
    print(tablero.casillas)

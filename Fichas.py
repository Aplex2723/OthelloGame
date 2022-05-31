
class Fichas:
    
    #   METODO QUE REVISA LAS FICHAS EN EL TABLERO
    def FichasEnTablero(self, tablero, x, y, dirX, dirY, jugador):
        included = []

        if jugador == 'O':
            otroJugador = 'X'
        else:
            otroJugador = 'O'

        for dist in range(1, 8):
            posX = x + dist * dirX
            posY = y + dist * dirY

            #   Si el jugador pierde
            if posX < 0 or posX >= len(tablero) or posY < 0 or posY >= len(tablero):
                return []

            if tablero[posY][posX] == otroJugador:
                included.append((posX, posY))
            elif tablero[posY][posX] == jugador:
                return included
            else:
                return []
        return []

    #   METODO QUE MUEVE LAS FICHAS SEGUN EL TURNO DE CADA JUGADORs
    def MoverFichas(self, tablero, jugador):
        print(jugador + " es tu turno!")
            
        posibilidades = self.MovimientosPosibles(tablero, jugador)

        if len(posibilidades) == 0:
            return False

        MovimientoX = -1
        MovimientoY = -1

        while (MovimientoX, MovimientoY) not in posibilidades:
            while MovimientoX < 0 or MovimientoX >= len(tablero):
                print('Escribe tu movimiento de COLUMNA:')
                MovimientoX = int(input())
                if MovimientoX == 0:
                    print("MOVIMIENTO NO VALIDO, PRUEBA NUBAMENTE")
                MovimientoX -= 1

            while MovimientoY < 0 or MovimientoY >= len(tablero):
                print('Escribe tu movimiento de FILA:')
                MovimientoY = int(input())
                if MovimientoY == 0:
                    print("MOVIMIENTO NO VALIDO, PRUEBA NUBAMENTE")
                MovimientoY -= 1

            if (MovimientoX, MovimientoY) not in posibilidades:
                MovimientoX = -1
                MovimientoY = -1

        voltear = self.FichasParaVoltear(tablero, MovimientoX, MovimientoY, jugador)
        tablero[MovimientoY][MovimientoX] = jugador

        tablero = self.VoltearFichas(tablero, voltear, jugador)

        return tablero
    
    #   METODO QUE VOLTEA LA FICHA DEL JUGADOR DADO EN EL TABLERO
    def VoltearFichas(self, tablero, voltear, jugador):
        for pos in voltear:
            tablero[pos[1]][pos[0]] = jugador

        return tablero
from Fichas import Fichas

class Tablero(Fichas):
    #   CONSTRUCTOR DE LA CLASE, LA CUAL CREA EL TABLERO Y LO RELLENA
    def __init__(self):
        self.__tablero = []
        for x in range(8):
            self.__tablero.append([' '] * 8)	#Se guardan 8 espacios en blanco
        
        self.__tablero[3][3] = 'X'
        self.__tablero[3][4] = 'O'
        self.__tablero[4][3] = 'O'
        self.__tablero[4][4] = 'X'
    
    @property
    def Tablero(self):
        return self.__tablero
    @Tablero.setter
    def Tablero(self, tablero):
        self.__tablero = tablero

    # 	METODO QUE OBTIENE LAS POSICIONES DE LAS PIEZAS PARA SER VOLTEADAS
    def FichasParaVoltear(self, tablero, x, y, jugador):
        voltear = []

        #	Se agrega a la ultima posicion del arreglo 
        voltear.extend((self.FichasEnTablero(tablero, x, y, 1, 1, jugador)))
        voltear.extend((self.FichasEnTablero(tablero, x, y, 1, -1, jugador)))
        voltear.extend((self.FichasEnTablero(tablero, x, y, -1, 1, jugador)))
        voltear.extend((self.FichasEnTablero(tablero, x, y, 0, 1, jugador)))
        voltear.extend((self.FichasEnTablero(tablero, x, y, 0, -1, jugador)))
        voltear.extend((self.FichasEnTablero(tablero, x, y, 1, 0, jugador)))
        voltear.extend((self.FichasEnTablero(tablero, x, y, -1, 0, jugador)))
        voltear.extend((self.FichasEnTablero(tablero, x, y, -1, -1, jugador)))

        return list(set(voltear))	#	El metodo set nos sirve para eliminar valores duplicados

    #   METODO QUE VERIFICA SI EL TABLERO ESTA LLENO O NO
    def TableroLleno(self, tablero):
        estaLleno = True

        for r in tablero:
            for c in r:
                if c == ' ':
                    estaLleno = False
        return estaLleno
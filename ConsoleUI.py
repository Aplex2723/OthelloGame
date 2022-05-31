import os
# from Interfaz import Interfaz as inter
from Tablero import Tablero as inter

class ConsoleUI(inter):
    @property
    def Tablero(self):
        return self.__tablero

    @Tablero.setter
    def Tablero(self, tablero):
        self.__tablero = tablero

    @property
    def FichaBlanca(self):
        return self.__fichaBlanca
    @property
    def FichaNegra(self):
        return self.__fichaNegra

    @FichaBlanca.setter
    def FichaBlanca(self, ficha):
        self.__fichaBlanca = ficha
    @FichaNegra.setter
    def FichaNegra(self, ficha):
        self.__fichaNegra = ficha

    @property
    def Ganador(self):
        return self.__ganador

    @Ganador.setter
    def Ganador(self, gan):
        self.__ganador = gan

    #	METODO QUE IMPRIME EL TABLERO 
    def imprimirTablero(self):
        os.system("cls")
        print('  1 2 3 4 5 6 7 8 ')
        print(" ================ ")
        for r in range(len(self.__tablero)):
            s = str(r+1) + '|'
            for c in range(len(self.__tablero[r])):
                s += self.__tablero[r][c] + '|'
            print(s + str(r+1))

        print(" ================ ")
        print('  1 2 3 4 5 6 7 8 ')
        print("\n------------------------------------------")
        print('\t>PUNTUACIONES GENERALES<')
        print('Ficha Negra \"O\": ' + str(self.__fichaNegra))
        print('Ficha Blanca \"X\": ' + str(self.__fichaBlanca))
        print("------------------------------------------")
    
    #   METODO QUE IMRIME EL GANADOR SEGUN LA FICHA
    def imprimirGanador(self, ficha):
        os.system("cls")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(f'El jugador {self.__ganador} ({ficha}) ha ganado!')
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    #   METODO QUE IMPRIME SI HA UN EMPATE
    def imprimirEmpate(self):
        os.system("cls")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print('\tEmpate!')
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")

	#	METODO QUE RECUENTA EL PUNTAJE DE CADA JUGADOR
    def calcularPuntaje(self):
        fichaNegra = 0
        fichaBlanca = 0

        for r in self.__tablero:
            for c in r:
                if c == 'O': 
                    fichaNegra += 1
                elif c == 'X':
                    fichaBlanca += 1
        return (fichaBlanca, fichaNegra)




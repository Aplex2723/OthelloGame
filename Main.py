from ConsoleUI import ConsoleUI as ui
from Tablero import Tablero

class Manager(Tablero):

	#	METODO QUE INICIA EL JUEGO
	def Init(self):	
		#	El programa siempre esta en ejecucion hasta que el jugador diga que no
		run = True
		while(run):
			interfaz = ui()
			tablero = Tablero().Tablero

			jugador = 'O'
			otroJugador = 'X'

			while not self.TableroLleno(tablero):

				interfaz.Tablero = tablero
				(fichaBlanca, fichaNegra) = interfaz.calcularPuntaje()
				interfaz.FichaBlanca = fichaBlanca
				interfaz.FichaNegra = fichaNegra
				interfaz.imprimirTablero()
				
				#	Validacion si es que un jugador se quedo sin movimientos
				if len(self.MovimientosPosibles(tablero, jugador)) == 0 and len(self.MovimientosPosibles(tablero, otroJugador)) == 0: break

				tmp = self.MoverFichas(tablero, jugador)
				if not tmp == False:
					tablero = tmp
					
				(jugador, otroJugador) = (otroJugador, jugador)	

			interfaz.Tablero = tablero
			(fichaNegra, fichaBlanca) = interfaz.calcularPuntaje()

			if fichaNegra > fichaBlanca:
				interfaz.Ganador = "Negro"
				interfaz.imprimirGanador(otroJugador)
				self.SalirORevancha()
			elif fichaNegra < fichaBlanca:
				interfaz.Ganador = "Blanco"
				interfaz.imprimirGanador(jugador)
				self.SalirORevancha()
			else:
				interfaz.imprimirEmpate()
				self.SalirORevancha()

	#	METODO QUE VERIFICA QUE TODOS LOS MOVIMIENTOS DEL JUGADOR SEAN LEGALES
	def MovimientosPosibles(self, tablero, jugador):
		movimiento = []

		for x in range(len(tablero)):
			for y in range(len(tablero)):
				if not self.MovimentosLegales(tablero, y, x, jugador): 
					continue
				else:
					if len(self.FichasParaVoltear(tablero, x, y, jugador)) > 0:
						movimiento.append((x, y))
		return movimiento

	def MovimentosLegales(self, tablero, r, c, jugador):
		return tablero[r][c] == ' ' #	Devuleve true si esta vacio
	    
	def SalirORevancha(self):
		print("\nQue desea hacer ahora?")
		print("1.- Revancha")
		print("2.- Salir")
		try:
			respuesta = int(input())
			if respuesta == 1:
				self.run = True
			elif respuesta == 2:
				self.run = False
			else:			
				print("\nOPCION NO VALIDA")
				self.SalirORevancha()
		except:
			print("\nOPCION NO VALIDA")
			self.SalirORevancha()



init = Manager()
init.Init()
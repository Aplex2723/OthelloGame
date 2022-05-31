from abc import ABC, abstractmethod

class Interfaz(ABC):
    @abstractmethod
    def imprimirTablero():
        pass
    @abstractmethod
    def imprimirEmpate():
        pass
    @abstractmethod
    def calcularPuntaje():
        pass
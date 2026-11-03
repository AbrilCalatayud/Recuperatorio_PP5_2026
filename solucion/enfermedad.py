from abc import ABC, abstractmethod

class Enfermedad(ABC):
    def __init__(self, cant_celulas_amenazadas):
        super().__init__()
        self.cant_celulas_amenazadas = cant_celulas_amenazadas

    def esta_curada(self):
        return self.cant_celulas_amenazadas == 0
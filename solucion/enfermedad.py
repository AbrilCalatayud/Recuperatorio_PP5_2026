from abc import ABC, abstractmethod

class Enfermedad(ABC):
    def __init__(self, cant_celulas_amenazadas):
        super().__init__()
        self.cant_celulas_amenazadas = cant_celulas_amenazadas

    def esta_curada(self):
        return self.cant_celulas_amenazadas == 0

    @abstractmethod
    def afectar_persona(self, persona):
        pass

    def atenuar(self, dosis):
        if self.cant_celulas_amenazadas < 15:
            self.cant_celulas_amenazadas = 0
        else:
            self.cant_celulas_amenazadas -= dosis * 1

    def recibir_antibiotico(self, dosis):
        pass

    def recibir_inmunosupresor(self, dosis):
        pass

class Infecciosa(Enfermedad):
    def __init__(self, cant_celulas_amenazadas):
        super().__init__(cant_celulas_amenazadas)

    def afectar_persona(self, persona):
        persona.subir_temperatura(self.cant_celulas_amenazadas / 1000)
        self.cant_celulas_amenazadas = self.cant_celulas_amenazadas * 2

    def recibir_antibiotico(self, dosis):
        self.atenuar(dosis)

class Autoinmune(Enfermedad):
    def __init__(self, cant_celulas_amenazadas):
        super().__init__(cant_celulas_amenazadas)

    def afectar_persona(self, persona):
        persona.disminuir_celulas(self.cant_celulas_amenazadas)

    def recibir_inmunosupresor(self, dosis):
        self.atenuar(dosis)
from abc import ABC, abstractmethod

class Medicamento(ABC):
    @abstractmethod
    def accionar(self, enfermedad, dosis):
        pass

class Antibiotico(Medicamento):
    def accionar(self, enfermedad, dosis):
        enfermedad.recibir_antibiotico(dosis)

class Inmunosupresor(Medicamento):
    def accionar(self, enfermedad, dosis):
        enfermedad.recibir_inmunosupresor(dosis)
class Persona:
    def __init__(self):
        self.temperatura = 36
        self.cant_celulas = 1000000
        self.enfermedades = []

    def esta_sana(self):
        return all(enfermedad.esta_curada for enfermedad in self.enfermedades)

    def contraer_enfermedad(self, enfermedad):
        self.enfermedades.append(enfermedad)

    def subir_temperatura(self, grados_subidos):
        self.temperatura += grados_subidos
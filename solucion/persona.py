class Persona:
    def __init__(self):
        self.temperatura = 36
        self.cant_celulas = 1000000
        self.enfermedades = []
        self.vivo = True

    def esta_sana(self):
        return all(enfermedad.esta_curada for enfermedad in self.enfermedades)

    def esta_viva(self):
        return self.vivo

    def vivir_un_dia(self):
        for enfermedad in self.enfermedades:
            enfermedad.afectar_persona(self)

    def contraer_enfermedad(self, enfermedad):
        if self.vivo:
            self.enfermedades.append(enfermedad)

    def recibir_medicamento(self, medicamento, dosis):
        if self.vivo:
            for enfermedad in self.enfermedades:
                medicamento.accionar(enfermedad, dosis)

    def subir_temperatura(self, grados_subidos):
        if (self.temperatura + grados_subidos) < 42:
            self.temperatura += grados_subidos
        else:
            self.temperatura = 42
            self.vivo = False

    def disminuir_celulas(self, cantidad):
        if self.cant_celulas >= cantidad:
            self.cant_celulas -= cantidad
        else:
            self.cant_celulas = 0
            self.vivo = False
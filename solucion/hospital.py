class Hospital:
    def __init__(self, pacientes):
        self.pacientes = pacientes

    def agregar_paciente(self, persona):
        if not persona.esta_sana():
            self.pacientes.append(persona)

    def dar_alta_a_paciente(self, persona):
        if persona.esta_sana():
            self.pacientes.remove(persona)

    def sacar_paciente_fallecido(self, persona):
        if not persona.esta_viva():
            self.pacientes.remove(persona)
    
    def pasa_un_dia(self):
        for paciente in self.pacientes:
            paciente.vivir_un_dia()
            self.dar_alta_a_paciente(paciente)
            self.sacar_paciente_fallecido(paciente)
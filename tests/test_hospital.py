import pytest
from solucion.persona import Persona
from solucion.enfermedad import Infecciosa, Autoinmune, Malaria, Lupus
from solucion.medicamento import Antibiotico, Inmunosupresor, Panacea
from solucion.hospital import Hospital

def test_persona_sana_contrae_malaria_lupus_pasa_a_enferma():
    persona = Persona()
    assert persona.esta_sana() is True

    persona.contraer_enfermedad(Malaria())
    persona.contraer_enfermedad(Lupus())
    assert persona.esta_sana() is False

def test_persona_con_malaria_recibe_antibiotico_hasta_curarse():
    persona = Persona()
    persona.contraer_enfermedad(Malaria())

    while(not persona.esta_sana()):
        assert persona.esta_sana() is False
        persona.recibir_medicamento(Antibiotico(), 300)

    assert persona.esta_sana() is True

def test_ingresa_uno_con_malaria_otro_con_lupus_y_viven_un_dia_verificar_estado():
    hospital = Hospital([])

    persona1 = Persona()
    malaria = Malaria()
    persona1.contraer_enfermedad(malaria)

    persona2 = Persona()
    lupus = Lupus()
    persona2.contraer_enfermedad(lupus)

    hospital.agregar_paciente(persona1)
    hospital.agregar_paciente(persona2)
    hospital.pasa_un_dia()

    assert persona1.temperatura == 41.0
    assert persona1.cant_celulas == 1000000
    assert malaria.cant_celulas_amenazadas == 10000

    assert persona2.temperatura == 36.0
    assert persona2.cant_celulas == 998000
    assert lupus.cant_celulas_amenazadas == 2000

def test_panacea_atenua_ambos_tipos():
    persona = Persona()
    malaria = Malaria()
    lupus = Lupus()
    persona.contraer_enfermedad(malaria)
    persona.contraer_enfermedad(lupus)

    persona.recibir_medicamento(Panacea(), 100)

    assert malaria.cant_celulas_amenazadas == 3500
    assert lupus.cant_celulas_amenazadas == 500
    
def test_persona_fallecida_no_puede_contraer_enfermedad():
    persona = Persona()
    persona.disminuir_celulas(1000000) 
    #esto es solo de prueba, normalmente debería matarla una enfermedad
    assert persona.esta_viva() is False
    with pytest.raises(ValueError):
        persona.contraer_enfermedad(Malaria())

def test_persona_fallecida_no_puede_recibir_medicamento():
    persona = Persona()
    persona.disminuir_celulas(1000000) 
    #esto es solo de prueba, normalmente debería matarla una enfermedad
    assert persona.esta_viva() is False
    with pytest.raises(ValueError):
        persona.recibir_medicamento(Panacea(), 100)

def test_persona_fallecida_no_puede_vivir_un_dia():
    persona = Persona()
    persona.disminuir_celulas(1000000) 
    #esto es solo de prueba, normalmente debería matarla una enfermedad
    assert persona.esta_viva() is False
    with pytest.raises(ValueError):
        persona.vivir_un_dia()
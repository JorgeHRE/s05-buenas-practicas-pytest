import pytest

from clinlab.clasificacion import clasificar_grupo_etario


def test_clasificar_grupo_etario_caso_normal():
    definir_edad = 18
    resultado = clasificar_grupo_etario(definir_edad)
    assert resultado == "adulto" 


def test_clasificar_grupo_etario_edad_negativa_lanza_error():
    definir_edad = -5
    with pytest.raises(ValueError):
        clasificar_grupo_etario(definir_edad)  


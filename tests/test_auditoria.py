import pandas as pd
import pytest

from clinlab.auditoria import marcar_valores_implausibles


def test_marcar_valores_implausibles_caso_normal():
    serie = pd.Series([10, 20, 30, 40, 50])
    resultado = marcar_valores_implausibles(serie, minimo=15, maximo=45)
    esperado = pd.Series([True, False, False, False, True])
    pd.testing.assert_series_equal(resultado, esperado) 


def test_marcar_valores_implausibles_rango_invertido_lanza_error():
    serie = pd.Series([10, 20, 30])
    with pytest.raises(ValueError):
        marcar_valores_implausibles(serie, minimo=30, maximo=20)      
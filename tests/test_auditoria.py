import pandas as pd
import pytest

from clinlab.auditoria import detectar_fechas_imposibles, marcar_valores_implausibles
from clinlab.preprocesamiento import optimizar_dtypes


def test_marcar_valores_implausibles_caso_normal():
    serie = pd.Series([10, 20, 30, 40, 50])
    resultado = marcar_valores_implausibles(serie, minimo=15, maximo=45)
    esperado = pd.Series([True, False, False, False, True])
    pd.testing.assert_series_equal(resultado, esperado) 


def test_marcar_valores_implausibles_rango_invertido_lanza_error():
    serie = pd.Series([10, 20, 30])
    with pytest.raises(ValueError):
        marcar_valores_implausibles(serie, minimo=30, maximo=20)      


def test_detectar_fechas_imposibles_visita_antes_de_nacer(df_pacientes_malicioso):
    # Hallazgo lab 2: hay visitas registradas antes de la fecha de nacimiento
    # del paciente (p5: nace 2000-01-01, visita 1999-12-31).

    # ARRANGE: la fixture trae las fechas como strings sin parsear. Las
    # convertimos con optimizar_dtypes, igual que en el pipeline real, para
    # comparar fechas de verdad y no texto (que solo "acierta" por suerte
    # cuando el formato es YYYY-MM-DD).
    # Pedimos la fixture como argumento del test: pytest la busca en
    # conftest.py y nos pasa un DataFrame nuevo en cada test.
    df = optimizar_dtypes(
        df_pacientes_malicioso,
        columnas_categoricas=[],  # aquí no nos interesa ninguna categórica
        columnas_fecha=["fecha_nacimiento", "fecha_visita"],
    )

    # ACT: el orden de los argumentos importa: primero la visita, luego el
    # nacimiento (la función pregunta "¿visita < nacimiento?").
    resultado = detectar_fechas_imposibles(
        df["fecha_visita"],
        df["fecha_nacimiento"],
    )

    pd.testing.assert_series_equal(
        resultado,
        pd.Series([False, False, False, False, True, False, False, False], name=None),
    ) 

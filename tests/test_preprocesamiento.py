import pandas as pd

from clinlab.preprocesamiento import optimizar_dtypes


def test_optimizar_dtypes_dataframe_vacio():
    # Hallazgo lab 2: El dataframe de entrada está vacío, pero aún así se deben convertir los dtypes de las columnas especificadas. 
    df_vacio = pd.DataFrame({
        "GENDER": [],
        "BIRTHDATE": [],
    })

    resultado = optimizar_dtypes(
        df_vacio,
        columnas_categoricas=["GENDER"],
        columnas_fecha=["BIRTHDATE"],
    )

    assert list(resultado.columns) == ["GENDER", "BIRTHDATE"]
    assert isinstance(resultado["GENDER"].dtype, pd.CategoricalDtype)
    assert pd.api.types.is_datetime64_any_dtype(resultado["BIRTHDATE"])
    
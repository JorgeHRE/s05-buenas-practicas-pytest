import pandas as pd
import pytest
from pandas.errors import MergeError
from clinlab.union import unir_con_validacion


def test_unir_con_validacion_person_id_duplicado_lanza_error(df_pacientes_malicioso):
    # Hallazgo lab 2: person_id duplicado en la tabla de pacientes; un join
    # sin validar multiplicaría las filas de ese paciente en silencio.

    # ARRANGE: tabla de encuentros (lado "muchos", va a la IZQUIERDA).
    # Que p1 tenga dos visitas es normal y NO debe causar error: lo que
    # queremos atrapar es el duplicado en la tabla de pacientes.
    df_encuentros = pd.DataFrame({
        "person_id": ["p1", "p1", "p2"],
        "visita_id": ["v1", "v2", "v3"],
    })

    # La fixture hace de tabla de pacientes (lado "uno", va a la DERECHA).
    # Trae p1 repetido, así que viola la regla "m:1" (derecha única).

    # ACT + ASSERT 
    with pytest.raises(MergeError):
        unir_con_validacion(
            df_encuentros,
            df_pacientes_malicioso,
            llave_izquierda="person_id",
            llave_derecha="person_id",
            # how y validate se quedan con sus defaults ("left" y "m:1"): así
            # probamos que la protección viene activada sin tener que pedirla.
        )

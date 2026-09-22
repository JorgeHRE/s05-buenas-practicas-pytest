import pytest

from clinlab.clinico import calcular_egfr_ckd_epi


@pytest.mark.parametrize(
    "creatinina_mg_dl, edad_anios, sexo, egfr_esperado",
    [
        pytest.param(1.0, 30, "M", 104, id="Hombre, creatinina normal"),
        pytest.param(0.9, 30, "F", 88.0, id="Mujer, creatinina normal"),
        pytest.param(1.5, 75, "M", 48.0, id="Hombre, creatinina alta"),
        pytest.param(1.3, 70, "F", 44.0, id="Mujer, creatinina alta"),
        pytest.param(0.4, 20, "M", 160.0, id="Hombre, creatinina baja"),
        pytest.param(0.5, 25, "F", 133.0, id="Mujer, creatinina baja"),
        pytest.param(4.0, 55, "F", 13.0, id="Mujer, erc avanzada"),
        pytest.param(6.0, 60, "M", 10.0, id="Hombre, erc avanzada"),
    ],
)
def test_calcular_egfr_ckd_epi_contra_referencia_kidney_org(
    creatinina_mg_dl, edad_anios, sexo, egfr_esperado
):
    """
    Test for calculating eGFR using the CKD-EPI equation against reference values from kidney.org.  
    (https://www.kidney.org/professionals/gfr_calculator + CKD-EPI Creatinine (2021), Standardized Assays: Yes, Adjust for BSA: No).
    """
    result = calcular_egfr_ckd_epi(creatinina_mg_dl, edad_anios, sexo)
    assert result == pytest.approx(egfr_esperado, rel=0.01, abs=0.5)  # tolerancia relativa del 1%


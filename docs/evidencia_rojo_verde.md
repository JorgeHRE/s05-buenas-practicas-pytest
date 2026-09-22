# Evidencia del ciclo rojo → verde

Test afectado: `tests/test_clasificacion.py::test_clasificar_grupo_etario_caso_normal`
Función bajo prueba: `clasificar_grupo_etario` (`src/clinlab/clasificacion.py`)

Para generar esta evidencia, se introdujo un bug intencional en el límite
pediátrico/adulto (`< 18` cambiado por `< 19`) y se corrió la prueba antes
y después de revertirlo.

## 🔴 Rojo — con el bug intencional (`< 19` en vez de `< 18`)

```
tests/test_clasificacion.py::test_clasificar_grupo_etario_caso_normal FAILED [ 50%]
tests/test_clasificacion.py::test_clasificar_grupo_etario_edad_negativa_lanza_error PASSED [100%]

=================================== FAILURES ===================================
___________________ test_clasificar_grupo_etario_caso_normal ___________________

    def test_clasificar_grupo_etario_caso_normal():
        definir_edad = 18
        resultado = clasificar_grupo_etario(definir_edad)
>       assert resultado == "adulto"
E       AssertionError: assert 'pediátrico' == 'adulto'
E
E         - adulto
E         + pediátrico

tests/test_clasificacion.py:9: AssertionError
=========================== short test summary info ============================
FAILED tests/test_clasificacion.py::test_clasificar_grupo_etario_caso_normal - AssertionError: assert 'pediátrico' == 'adulto'
========================= 1 failed, 1 passed in 0.03s ==========================
```

## 🟢 Verde — con el límite corregido (`< 18`)

```
tests/test_clasificacion.py::test_clasificar_grupo_etario_caso_normal PASSED [ 50%]
tests/test_clasificacion.py::test_clasificar_grupo_etario_edad_negativa_lanza_error PASSED [100%]

============================== 2 passed in 0.01s ===============================
```

## Cómo reproducirlo (para capturas de pantalla propias)

1. Abrí `src/clinlab/clasificacion.py` y cambiá `if edad_anios < 18:` por
   `if edad_anios < 19:`.
2. Corré `pytest tests/test_clasificacion.py -v` — debería fallar
   `test_clasificar_grupo_etario_caso_normal`. Capturá esta pantalla (rojo).
3. Revertí el cambio (volvé a `< 18`).
4. Corré `pytest tests/test_clasificacion.py -v` de nuevo — ambos tests
   deberían pasar. Capturá esta pantalla (verde).

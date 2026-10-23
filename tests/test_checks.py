import pandas as pd
from checks import contar_nulos, contar_duplicados

def test_sin_nulos():
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": ["a", "b", "c"]
    })
    assert contar_nulos(df).sum() == 0

def test_con_nulos():
    df = pd.DataFrame({
        "A": [1, None, 3],
        "B": ["a", "b", None]
    })
    resultado = contar_nulos(df)
    assert resultado["A"] == 1
    assert resultado["B"] == 1
    assert contar_nulos(df).sum() == 2

def test_sin_duplicados():
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": ["a", "b", "c"]
    })
    assert contar_duplicados(df).sum() == 0

def test_con_duplicados():
    df = pd.DataFrame({
        "A": [1, 2, 2, 3],
        "B": ["a", "b", "b", "c"]
    })
    assert contar_duplicados(df).sum() == 1
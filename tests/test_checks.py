import pandas as pd 
from checks import contar_nulos

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

def contar_duplicados(df):
    """
    Cuenta el número de filas duplicadas en un DataFrame.
    
    Args:
        df (pd.DataFrame): El DataFrame a evaluar.
        
    Returns:
        int: Número de filas duplicadas.
    """
    return df.duplicated().sum()
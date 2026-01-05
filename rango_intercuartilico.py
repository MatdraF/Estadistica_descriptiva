from .percentil import percentil

def rango_intercuartilico(datos):
    """
    Calcula el rango intercuartílico (IQR) de una lista de valores numéricos,
    ignorando valores NaN.

    El rango intercuartílico se define como la diferencia entre el
    percentil 75 (Q3) y el percentil 25 (Q1).

    Parámetros
    ----------
    datos : list
        Lista de valores numéricos (int o float). Los valores NaN
        son ignorados en el cálculo.

    Retorna
    -------
    float
        Rango intercuartílico de los valores válidos.

    Lanza
    -----
    Las excepciones son propagadas desde la función percentil.
    """
    return percentil(datos, 75) - percentil(datos, 25)


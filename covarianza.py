import math
from .promedio import promedio
def covarianza(x, y):
    """
    Calcula la covarianza poblacional entre dos listas de valores
    numéricos, ignorando pares que contengan valores NaN.

    La covarianza mide la variación conjunta entre dos variables.

    Parámetros
    ----------
    x : list
        Primera lista de valores numéricos (int o float).
    y : list
        Segunda lista de valores numéricos (int o float).

    Retorna
    -------
    float
        Covarianza poblacional entre x e y.

    Lanza
    -----
    TypeError
        Si las listas contienen valores no numéricos (excepto NaN).
    ValueError
        Si las listas no tienen la misma longitud o no existen
        pares válidos suficientes para el cálculo.
    """
    if len(x) != len(y):
        raise ValueError("Las listas deben tener la misma longitud")

    x_validos = []
    y_validos = []

    for xi, yi in zip(x, y):
        if isinstance(xi, float) and math.isnan(xi):
            continue
        if isinstance(yi, float) and math.isnan(yi):
            continue

        if not isinstance(xi, (int, float)) or not isinstance(yi, (int, float)):
            raise TypeError("Datos no numéricos")

        x_validos.append(xi)
        y_validos.append(yi)

    n = len(x_validos)
    if n == 0:
        raise ValueError("No hay pares válidos")

    media_x = promedio(x_validos)
    media_y = promedio(y_validos)

    suma = 0
    for xi, yi in zip(x_validos, y_validos):
        suma += (xi - media_x) * (yi - media_y)

    return suma / n

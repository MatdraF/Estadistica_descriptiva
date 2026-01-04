import math

def rango(datos):
    """
    Calcula el rango de una lista de valores numéricos,
    ignorando valores NaN.

    Parámetros
    ----------
    datos : list
        Lista de valores numéricos (int o float). Los valores NaN
        son ignorados en el cálculo.

    Retorna
    -------
    float
        Rango de los valores válidos (máximo - mínimo).

    Lanza
    -----
    TypeError
        Si la lista contiene valores no numéricos (excepto NaN).
    ValueError
        Si no existen valores numéricos válidos para realizar el cálculo.
    """
    valores_validos = []

    for x in datos:
        if isinstance(x, float) and math.isnan(x):
            continue

        if not isinstance(x, (int, float)):
            raise TypeError("Datos no numéricos")

        valores_validos.append(x)

    if len(valores_validos) == 0:
        raise ValueError("No hay valores válidos")

    minimo = valores_validos[0]
    maximo = valores_validos[0]

    for x in valores_validos:
        if x < minimo:
            minimo = x
        if x > maximo:
            maximo = x

    return maximo - minimo
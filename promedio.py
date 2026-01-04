import math

def promedio(datos):
    """
    Calcula el promedio aritmético de una lista de valores numéricos,
    ignorando valores NaN.

    Parámetros
    ----------
    datos : list
        Lista de valores numéricos (int o float). Los valores NaN
        son ignorados en el cálculo.

    Retorna
    -------
    float
        Promedio aritmético de los valores válidos.

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

    return sum(valores_validos) / len(valores_validos)

import math

def varianza(datos):
    """
    Calcula la varianza poblacional de una lista de valores numéricos,
    ignorando valores NaN.

    La varianza mide la dispersión de los datos con respecto a su promedio.

    Parámetros
    ----------
    datos : list
        Lista de valores numéricos (int o float). Los valores NaN
        son ignorados en el cálculo.

    Retorna
    -------
    float
        Varianza de los valores válidos.

    Lanza
    -----
    TypeError
        Si la lista contiene valores no numéricos (excepto NaN).
    ValueError
        Si no existen valores suficientes para realizar el cálculo.
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

    media = promedio(valores_validos)

    suma = 0
    for x in valores_validos:
        suma += (x - media) ** 2

    return suma / len(valores_validos)

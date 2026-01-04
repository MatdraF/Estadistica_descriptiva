import math

def moda(datos):
    """
    Calcula la moda de una lista de valores.

    La función admite valores numéricos y strings. Los valores NaN
    son ignorados silenciosamente en el cálculo.

    Parámetros
    ----------
    datos : list
        Lista de valores numéricos o strings.

    Retorna
    -------
    list
        Lista con el o los valores modales.
        Retorna una lista vacía si no existe moda.

    Lanza
    -----
    TypeError
        Si la lista contiene valores no permitidos.
    ValueError
        Si no existen valores válidos para calcular la moda.
    """
    valores_validos = []

    for x in datos:
        if isinstance(x, float) and math.isnan(x):
            continue

        if not isinstance(x, (int, float, str)):
            raise TypeError("Valores no permitidos")

        valores_validos.append(x)

    if len(valores_validos) == 0:
        raise ValueError("No hay valores válidos")

    frecuencias = {}

    for x in valores_validos:
        if x in frecuencias:
            frecuencias[x] += 1
        else:
            frecuencias[x] = 1

    max_frecuencia = 0
    for freq in frecuencias.values():
        if freq > max_frecuencia:
            max_frecuencia = freq

    if max_frecuencia == 1:
        return []

    modas = []
    for x in frecuencias:
        if frecuencias[x] == max_frecuencia:
            modas.append(x)

    return modas

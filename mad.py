import math
import mediana
def desviacion_mediana_absoluta(datos):
    """
    Calcula la desviación mediana absoluta (MAD) de una lista de valores
    numéricos, ignorando valores NaN.

    La MAD se define como la mediana de las desviaciones absolutas
    respecto a la mediana del conjunto de datos.

    Parámetros
    ----------
    datos : list
        Lista de valores numéricos (int o float). Los valores NaN
        son ignorados en el cálculo.

    Retorna
    -------
    float
        Desviación mediana absoluta de los valores válidos.

    Lanza
    -----
    Las excepciones son propagadas desde la función mediana.
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

    med = mediana(valores_validos)

    desviaciones = []
    for x in valores_validos:
        desviaciones.append(abs(x - med))

    return mediana(desviaciones)

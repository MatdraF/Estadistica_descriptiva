import math

def percentil(datos, p):
    """
    Calcula el percentil p de una lista de valores numéricos,
    ignorando valores NaN.

    El percentil representa el valor bajo el cual se encuentra
    el p% de los datos.

    Parámetros
    ----------
    datos : list
        Lista de valores numéricos (int o float). Los valores NaN
        son ignorados en el cálculo.
    p : float
        Percentil a calcular, con 0 <= p <= 100.

    Retorna
    -------
    float
        Valor correspondiente al percentil p.

    Lanza
    -----
    TypeError
        Si la lista contiene valores no numéricos (excepto NaN).
    ValueError
        Si p no está en el intervalo [0, 100] o no existen valores válidos.
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

    if not isinstance(p, (int, float)):
        raise TypeError("El percentil debe ser numérico")

    if p < 0 or p > 100:
        raise ValueError("El percentil debe estar entre 0 y 100")

    valores_validos.sort()
    n = len(valores_validos)

    indice = (p / 100) * (n - 1)
    inferior = int(indice)
    superior = inferior + 1

    if superior >= n:
        return valores_validos[inferior]

    fraccion = indice - inferior

    return (1 - fraccion) * valores_validos[inferior] + fraccion * valores_validos[superior]
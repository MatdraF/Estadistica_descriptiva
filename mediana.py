import math
def mediana(datos):
    """
    Calcula la mediana de una lista de valores numéricos,
    ignorando valores NaN.

    Parámetros
    ----------
    datos : list
        Lista de valores numéricos (int o float). Los valores NaN
        son ignorados en el cálculo.

    Retorna
    -------
    float
        Mediana de los valores válidos.

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
               raise TypeError("Datos no numéricos ")
         
         valores_validos.append(x)
  
    valores_validos.sort()
    n = len(valores_validos)
    mitad = n // 2
    if n % 2 == 1:
        mediana = valores_validos[mitad]
    else:
        mediana = (valores_validos[mitad - 1] + valores_validos[mitad]) / 2
    return mediana


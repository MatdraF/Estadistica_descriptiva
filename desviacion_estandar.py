import math
import varianza
def desviacion_estandar(datos):
    """
    Calcula la desviación estándar poblacional de una lista de valores
    numéricos, ignorando valores NaN.

    La desviación estándar corresponde a la raíz cuadrada de la varianza
    y se expresa en las mismas unidades que los datos originales.

    Parámetros
    ----------
    datos : list
        Lista de valores numéricos (int o float). Los valores NaN
        son ignorados en el cálculo.

    Retorna
    -------
    float
        Desviación estándar de los valores válidos.

    Lanza
    -----
    Las excepciones son propagadas desde la función varianza.
    """
    
    return math.sqrt(varianza(datos))


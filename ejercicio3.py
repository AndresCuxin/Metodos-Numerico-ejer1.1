#   Codigo que implementa el calculo de errores
#   en operaciones numericas
# 
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 29/01/2025
#

# Esta es l función para poder calcular los errores dados dos valores y un valor real de referencia
def calcular_errores(x, y, valor_real):

    # Este calcula la diferencia entre los dos valores
    diferencia = x - y

    # Calcula el error absoluto
    error_abs = abs(valor_real - diferencia)

    # Calcula el error relativo
    error_rel = error_abs / abs(valor_real)

    # Convierte el error relativo en porcentaje
    error_pct = error_rel * 100

    # Aqui es donde se imprimen los resultados
    print(f"Diferencia: {diferencia}")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel}")
    print(f"Error porcentual: {error_pct}%")
    return error_abs, error_rel


# La lista de valores de prueba para poder calcular los errores
valores = [(1.0000001, 1.0000000, 0.0000001), (1.000000000000001, 1.000000000000000, 0.000000000000001)]

# Iterar sobre cada conjunto de valores y calcular errores
for x, y, real in valores:
    print(f"\nPara x={x}, y={y}:")
    calcular_errores(x, y, real)
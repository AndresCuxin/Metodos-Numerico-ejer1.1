#   Codigo que implementa un esquema numerico 
#   para determinar la precision de una maquina
# 
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 29/01/2025

# Se importa la librería numpy, aunque no se está usando en este código.
import numpy as np

# Inicialización de la variable epsilon (precisión de la máquina) con un valor de 1.0.
epsilon = 1.0
# Inicialización del contador de iteraciones en 0.
iteracion = 0
# Bucle while que se ejecuta mientras 1.0 + epsilon no sea igual a 1.0.
# La condición verifica si el valor de epsilon aún afecta el resultado de la operación.
while 1.0 + epsilon != 1.0:
    # En cada iteración, se divide epsilon entre 2, reduciendo su valor.
    epsilon /= 2
    # Se incrementa el contador de iteraciones.
    iteracion = iteracion + 1
    # Se imprime el número de iteración y el valor actual de epsilon.
    # Esto permite observar cómo disminuye epsilon a medida que se ejecutan las iteraciones.
    print(f"Iteracion: {iteracion}, Precisión de máquina: {epsilon}")

# Después de salir del bucle, epsilon es tan pequeño que ya no afecta a 1.0.
# Entonces, multiplicamos epsilon por 2 para obtener el último valor de epsilon que todavía era significativo.
epsilon *= 2
# Se imprime el valor final de epsilon, que representa la precisión de la máquina.
print(f"Precisión de máquina: {epsilon}")
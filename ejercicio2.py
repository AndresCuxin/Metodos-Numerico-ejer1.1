#   Codigo que implementa un esquema numerico 
#   para determinar la aproximacion de Leibniz
# 
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 29/01/2025
#

#primero se instalo la libreria numpy y matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Esta función sirve para poder calcular pi con la serie de Leibniz
def leibniz_pi(n):
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

# Este es el valor real de pi
true_pi = np.pi

# Los valores de N a probar
N_values = [10, 100, 1000, 10000]

# Las listas para poder almacenar los errores
errors_abs = []
errors_rel = []
errors_quad = []

print("N\tError Absoluto\tError Relativo\tError Cuadrático")
print("-" * 50)

# En donde se havc el cálculo de los errores
for N in N_values:
    approx_pi = leibniz_pi(N)
    error_abs = abs(true_pi - approx_pi)
    error_rel = error_abs / true_pi
    error_quad = error_abs ** 2
    
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    errors_quad.append(error_quad)
    
    print(f"{N}\t{error_abs:.10f}\t{error_rel:.10f}\t{error_quad:.10f}")

# Las funciones para poder hacer la graficar de los errores
plt.figure(figsize=(8, 6))
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o')
plt.plot(N_values, errors_rel, label='Error relativo', marker='s')
plt.plot(N_values, errors_quad, label='Error cuadrático', marker='^')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N (Número de términos)')
plt.ylabel('Error')
plt.legend()
plt.title('Errores en la aproximación de π con la serie de Leibniz')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
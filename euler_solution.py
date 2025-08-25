import numpy as np

# Definimos la ecuación diferencial
def f(t, y):
    return t * y

# Condición inicial
t0 = 0
y0 = 1

# Intervalo y paso
t_end = 1
h = 0.2
n_steps = int((t_end - t0)/h)

# Listas para almacenar los resultados
t_values = [t0]
y_values = [y0]

# Método de Euler
t = t0
y = y0
for i in range(n_steps):
    y = y + h * f(t, y)
    t = t + h
    t_values.append(t)
    y_values.append(y)

# Solución exacta
y_exact = [np.exp(t**2 / 2) for t in t_values]

# Mostrar resultados
print("t\tEuler\tExacta")
for t, y_e, y_ex in zip(t_values, y_values, y_exact):
    print(f"{t:.1f}\t{y_e:.5f}\t{y_ex:.5f}")

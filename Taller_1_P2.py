import numpy as np

# Datos
t = np.array([0, 25, 50, 75, 100, 125])
y = np.array([0, 32, 58, 78, 92, 100])

# Tamaños de paso
hs = np.array([25, 12.5, 6.25])

# Agregar dos puntos más en cada extremo
t = np.concatenate(([t[0] - 2 * hs[-1], t[0] - hs[-1]], t, [t[-1] + hs[-1], t[-1] + 2 * hs[-1]]))
y = np.concatenate(([y[0], y[0]], y, [y[-1], y[-1]]))

# Matriz para almacenar las aproximaciones
D = np.zeros((len(hs), len(y)))

# Aproximaciones iniciales
for i in range(len(y)):
    D[0, i] = (y[min(i + 1, len(y) - 1)] - y[max(i - 1, 0)]) / (2 * hs[0])

# Extrapolación de Richardson
for k in range(1, len(hs)):
    for i in range(len(y)):
        D[k, i] = (4 ** (k) * D[k - 1, min(i + 1, len(y) - 1)] - D[k - 1, max(i - 1, 0)]) / (4 ** (k) - 1)

# Velocidad
v = D[-1, 2:-2]

# Aceleración
a = np.zeros_like(v)
for i in range(len(v)):
    a[i] = (v[min(i + 1, len(v) - 1)] - v[max(i - 1, 0)]) / (2 * hs[-1])

# Imprimir los resultados
print("Velocidades:")
print(v)
print("Aceleraciones:")
print(a)

input('click para salir')
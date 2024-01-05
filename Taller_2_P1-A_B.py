import numpy as np
import matplotlib.pyplot as plt

# Definir la ecuación diferencial
def dydx(x, y):
    return (1 + 4*x) * np.sqrt(y)

# Definir las condiciones iniciales y el tamaño de paso
y0 = 1
h = 0.25

# Definir la función para implementar el método de Euler
def euler(dydx, x0, y0, h, num_steps):
    x = np.zeros(num_steps + 1)
    y = np.zeros(num_steps + 1)
    x[0] = x0
    y[0] = y0
    for i in range(num_steps):
        y[i+1] = y[i] + h * dydx(x[i], y[i])
        x[i+1] = x[i] + h
    return x, y

# Calcular los valores de x y y usando el método de Euler
x, y = euler(dydx, 0, y0, h, 4)

# Resultados
plt.plot(x, y, 'o-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler dy/dx = (1 + 4x)*√y')
plt.show()

input('click para salir')
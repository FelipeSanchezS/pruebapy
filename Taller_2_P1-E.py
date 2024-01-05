import numpy as np
import matplotlib.pyplot as plt

# Definir la ecuación diferencial
def dydx(x, y):
    return (1 + 4*x) * np.sqrt(y)

# Definir las condiciones iniciales y el tamaño de paso
y0 = 1
h = 0.25

# Definir la función para implementar el método de RK4
def rk(dydx, x0, y0, h, num_steps):
    x = np.zeros(num_steps + 1)
    y = np.zeros(num_steps + 1)
    x[0] = x0
    y[0] = y0
    for i in range(num_steps):
        k1 = h * dydx(x[i], y[i])
        k2 = h * dydx(x[i] + h/2, y[i] + k1/2)
        k3 = h * dydx(x[i] + h/2, y[i] + k2/2)
        k4 = h * dydx(x[i] + h, y[i] + k3)
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
        x[i+1] = x[i] + h
    return x, y

# Calcular los valores de x y y usando el método de RK4
x, y = rk(dydx, 0, y0, h, 4)

# Graficar los resultados
plt.plot(x, y, 'o-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('RK dy/dx = (1 + 4x)*√y')
plt.show()

input('click para salir')
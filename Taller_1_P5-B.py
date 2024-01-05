import numpy as np
import matplotlib.pyplot as plt

# Definimos la función f(t, y)
def f(t, y):
    return y * np.power(np.sin(t), 3)

# Definimos los métodos de RK2 y Ralston
def RK2(tn, yn, h):
    k1 = f(tn, yn)
    k2 = f(tn + h, yn + h * k1)
    return yn + h * (k1 + k2) / 2

def Ralston(tn, yn, h):
    k1 = f(tn, yn)
    k2 = f(tn + (3/4)*h, yn + (3/4)*h*k1)
    return yn + (1/3)*h*(k1 + 2*k2)

# Condiciones iniciales
t0, y0 = 0, 1

# Intervalo de integración
t_final = 3

# Paso
h = 0.1

# Número de pasos
n = int((t_final - t0) / h)

# Arrays para almacenar soluciones
t = np.zeros(n+1)
y_RK2 = np.zeros(n+1)
y_Ralston = np.zeros(n+1)

# Asignamos condiciones iniciales
t[0], y_RK2[0], y_Ralston[0] = t0, y0, y0

# Solución con el método de RK2
for i in range(n):
    y_RK2[i+1] = RK2(t[i], y_RK2[i], h)
    t[i+1] = t[i] + h

# Solución con el método de Ralston
for i in range(n):
    y_Ralston[i+1] = Ralston(t[i], y_Ralston[i], h)

# Plot
plt.plot(t, y_RK2, label='RK2')
plt.plot(t, y_Ralston, label='Ralston')
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solución de dy/dt = y*sin^3(t)')
plt.show()

input('click para salir')
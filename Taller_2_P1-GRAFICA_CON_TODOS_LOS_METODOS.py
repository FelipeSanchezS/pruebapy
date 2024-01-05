import numpy as np
import matplotlib.pyplot as plt

# Define la ecuación diferencial
def f(x, y):
    return (1 + 4*x)*np.sqrt(y)

# Define los parámetros iniciales
x0 = 0
y0 = 1
h = 0.25
n = int((1 - x0)/h) + 1

# Inicializa las listas de resultados para cada método
x = np.linspace(x0, 1, n)
y_euler = [y0]
y_heun = [y0]
y_ralston = [y0]
y_rk4 = [y0]

# Calcula las soluciones con cada método
for i in range(1, n):
    # Método de Euler
    y_euler.append(y_euler[-1] + h*f(x[i-1], y_euler[-1]))
    
    # Método de Heun
    y_pred = y_heun[-1] + h*f(x[i-1], y_heun[-1])
    y_heun.append(y_heun[-1] + (h/2)*(f(x[i-1], y_heun[-1]) + f(x[i], y_pred)))
    
    # Método de Ralston
    k1 = f(x[i-1], y_ralston[-1])
    k2 = f(x[i-1] + (3/4)*h, y_ralston[-1] + (3/4)*h*k1)
    y_ralston.append(y_ralston[-1] + (1/3)*h*(k1 + 2*k2))
    
    # Método RK4
    k1 = f(x[i-1], y_rk4[-1])
    k2 = f(x[i-1] + (1/2)*h, y_rk4[-1] + (1/2)*h*k1)
    k3 = f(x[i-1] + (1/2)*h, y_rk4[-1] + (1/2)*h*k2)
    k4 = f(x[i], y_rk4[-1] + h*k3)
    y_rk4.append(y_rk4[-1] + (h/6)*(k1 + 2*k2 + 2*k3 + k4))

# Grafica los resultados de cada método
plt.plot(x, y_euler, label='Euler')
plt.plot(x, y_heun, label='Heun')
plt.plot(x, y_ralston, label='Ralston')
plt.plot(x, y_rk4, label='RK4')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('dy/dx = (1 + 4x)*√y')
plt.show()

 
input('click para salir')
import math

# Definir la función a resolver
def f(t, y):
    return y*math.pow(math.sin(t), 3)

# Definir los parámetros
t0 = 0
tf = 3
h = 0.1

# Definir las listas para almacenar los valores de t e y
t_values = [t0]
y_values = [1]

# Definir el ciclo principal del método de Heun
while t_values[-1] < tf:
    t = t_values[-1]
    y = y_values[-1]
    y_predictor = y + h*f(t, y)
    y_corrector = y + 0.5*h*(f(t, y) + f(t + h, y_predictor))
    t_values.append(t + h)
    y_values.append(y_corrector)

# Imprimir los resultados
for i in range(len(t_values)):
    print("t = {:.1f}, y = {:.4f}".format(t_values[i], y_values[i]))

input('click para salir')
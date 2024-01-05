import math

# Función a evaluar
def f(x):
    return math.exp(x)

# Punto de evaluación
x = 2

# Tamaño del paso
h = 0.1

#(O(h^2))
fd_1 = (f(x+h) - f(x-h)) / (2*h)
print("Aproximación primera derivada (O(h^2)): {:.4f}".format(fd_1))

#(O(h^2))
sd_1 = (f(x+h) - 2*f(x) + f(x-h)) / (h**2)
print("Aproximación segunda derivada (O(h^2)): {:.4f}".format(sd_1))

#(O(h^4))
fd_2 = (-f(x+2*h) + 8*f(x+h) - 8*f(x-h) + f(x-2*h)) / (12*h)
print("Aproximación primera derivada (O(h^4)): {:.4f}".format(fd_2))

#(O(h^4))
sd_2 = (-f(x+2*h) + 16*f(x+h) - 30*f(x) + 16*f(x-h) - f(x-2*h)) / (12*h**2)
print("Aproximación segunda derivada (O(h^4)): {:.4f}".format(sd_2))

input('Click para salir')
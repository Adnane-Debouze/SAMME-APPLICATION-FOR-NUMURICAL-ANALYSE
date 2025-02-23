import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange


x = [0, 1, 2]
y = [1, 3, 2]

f = lagrange(x, y)


x_new = np.linspace(min(x) - 1, max(x) + 1, 100)
y_new = f(x_new)


fig = plt.figure(figsize=(10, 8))
plt.plot(x_new, y_new, 'b', label='Polynôme de Lagrange')
plt.plot(x, y, 'ro', label='Points de données')
plt.title('Lagrange Polynomial with scipy')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


print("Vérification des points de données :")
for i, xi in enumerate(x):
    print(f"f({xi}) = {f(xi):.2f} (attendu {y[i]})")

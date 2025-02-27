import numpy as np
import matplotlib.pyplot as plt

# 1. f(x) = 2sin(x) − x
x1 = np.linspace(0, 3, 1000)  # Définir la plage de x pour trouver les racines positives
f1 = 2 * np.sin(x1) - x1

plt.figure(figsize=(12, 6))
plt.plot(x1, f1, label='f(x) = 2sin(x) - x', color='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.title('Graphique de f(x) = 2sin(x) - x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

# Calculer les intervalles approximatifs pour la racine
x2 = np.arange(0, 3, 0.1)
f2 = 2 * np.sin(x2) - x2

root_interval = []
for i in range(len(x2) - 1):
    if f2[i] * f2[i + 1] < 0:  # La racine se trouve entre x[i] et x[i + 1]
        root_interval.append((x2[i], x2[i + 1]))

# 2. f(x) = x^3 - 6x^2 + 11x - 6
x3 = np.linspace(0, 4, 1000)  # Définir la plage de x pour trouver les racines dans [0, 4]
f3 = x3**3 - 6*x3**2 + 11*x3 - 6

plt.figure(figsize=(12, 6))
plt.plot(x3, f3, label='f(x) = x^3 - 6x^2 + 11x - 6', color='red')
plt.axhline(0, color='black', linewidth=0.5)
plt.title('Graphique de f(x) = x^3 - 6x^2 + 11x - 6')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

# Calculer f(x) à des incréments de 0.25 pour identifier les sous-intervalles
x4 = np.arange(0, 4.25, 0.25)
f4 = x4**3 - 6*x4**2 + 11*x4 - 6

root_intervals_f3 = []
for i in range(len(x4) - 1):
    if f4[i] * f4[i + 1] < 0:  # La racine se trouve entre x[i] et x[i + 1]
        root_intervals_f3.append((x4[i], x4[i + 1]))

print("Intervalle pour la racine de f(x) = 2sin(x) - x :", root_interval)
print("Intervalles pour les racines de f(x) = x^3 - 6x^2 + 11x - 6 :", root_intervals_f3)

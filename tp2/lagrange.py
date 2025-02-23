import numpy as np
import matplotlib.pyplot as plt

def lagrange_basis(x_points, i, x):
    """Calcule la base de Lagrange L_i(x)."""
    n = len(x_points)
    L = np.ones_like(x, dtype=float)
    for j in range(n):
        if j != i:
            L *= (x - x_points[j]) / (x_points[i] - x_points[j])
    return L

def lagrange_interpolation(x_points, y_points, x):
    """Calcule le polynôme d'interpolation de Lagrange en x."""
    n = len(x_points)
    P = np.zeros_like(x, dtype=float)
    for i in range(n):
        P += y_points[i] * lagrange_basis(x_points, i, x)
    return P

# Augmenter le nombre de points d'interpolation
n_points = 10  # Plus de points pour une meilleure approximation
x_points = np.linspace(-np.pi, np.pi, n_points)  # Points uniformes
# x_points = np.cos((2*np.arange(n_points) + 1) / (2 * n_points) * np.pi) * np.pi  # Points de Chebyshev (option)
y_points = np.sin(x_points)

# Évaluation sur une plage de x
x = np.linspace(-np.pi, np.pi, 500)
y_interp = lagrange_interpolation(x_points, y_points, x)

# Tracé des résultats
plt.figure(figsize=(10, 6))
plt.plot(x, y_interp, label="Polynôme interpolateur", color="blue")
plt.plot(x_points, y_points, 'ro', label="Points d'interpolation")
plt.plot(x, np.sin(x), '--', label="sin(x)", color="green")
plt.title("Interpolation polynomiale de Lagrange pour sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

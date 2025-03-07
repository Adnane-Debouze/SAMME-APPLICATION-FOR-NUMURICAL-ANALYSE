import numpy as np


def simpson_rule(x, f_values):

    n = len(x) - 1
    h = (x[-1] - x[0]) / n  # Pas

    I = f_values[0] + f_values[-1]
    I += 4 * sum(f_values[1:n:2])
    I += 2 * sum(f_values[2:n - 1:2])

    return (h / 3) * I


# Données tabulées
x_values = np.array([0, np.pi / 8, np.pi / 4, 3 * np.pi / 8, np.pi / 2])
f_values = np.array([0, 0.382683, 0.707107, 0.923880, 1])

integral_tabulated = simpson_rule(x_values, f_values)
print(f"Intégrale approximée avec les valeurs tabulées : {integral_tabulated}")


# Calcul avec la fonction exacte f(x) = sin(x)
def f(x):
    return np.sin(x)


f_exact_values = f(x_values)
integral_exact = simpson_rule(x_values, f_exact_values)
print(f"Intégrale approximée avec f(x) = sin(x) : {integral_exact}")

integral_true = 1 - np.cos(np.pi / 2)
print(f"Valeur exacte de l'intégrale : {integral_true}")

diff_tabulated = abs(integral_tabulated - integral_true)
diff_exact = abs(integral_exact - integral_true)
print(f"Erreur avec les valeurs tabulées : {diff_tabulated}")
print(f"Erreur avec f(x) = sin(x) : {diff_exact}")

import numpy as np

def convergence(x_new, x_old, epsilon):
    return np.max(np.abs(x_new - x_old)) < epsilon

def jacobi(A, b, x0, epsilon):
    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x)
    k = 0
    while True:
        k+=1
        for i in range(n):
            s1 = np.sum(A[i, :i] * x[:i])
            s2 = np.sum(A[i, i+1:] * x[i+1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if convergence(x_new, x, epsilon):
            break
        x = x_new.copy()
    return x,k

def gauss_seidel(A, b, x0, epsilon):
    n = len(b)
    x = x0.copy()
    k=0
    while True:
        k+=1
        x_new = x.copy()
        for i in range(n):
            s1 = np.sum(A[i, :i] * x[:i])
            s2 = np.sum(A[i, i+1:] * x[i+1:])
            x[i] = (b[i] - s1 - s2) / A[i, i]
        if convergence(x, x_new, epsilon):
          break
    return x,k

# Définition du système
A = np.array([[3, 1, -1], [1, 5, 2], [2, -1, -6]], dtype=float)
b = np.array([2, 17, -18], dtype=float)
x0 = np.array([0, 0, 0], dtype=float)
epsilon = 0.0001

x_jacobi,k_jacobi = jacobi(A, b, x0, epsilon)
print(f"Solution par Jacobi : {x_jacobi} en {k_jacobi} itérations")

x_gauss_seidel,k_gauss = gauss_seidel(A, b, x0, epsilon)
print(f"Solution par Gauss-Seidel : {x_gauss_seidel} en {k_gauss} itérations")

x_exact = np.linalg.solve(A,b)
print(f"Solution exacte : {x_exact}")
def jacobi_recursive(max_iterations):

    E = 0.0001
    e = float('inf') 
    x1, x2, x3 = 0.0, 0.0, 0.0 
    iteration = -1

    while e > E:
        n_x1 = (1/3) * (2 - x2 + x3)
        n_x2 = (1/5) * (17 - x1 - 2 * x3)
        n_x3 = (1/(-6)) * (-18 - 2 * x1 + x2)
        e = ((n_x1 - x1)**2 + (n_x2 - x2)**2 + (n_x3 - x3)**2)**0.5

        x1, x2, x3 = n_x1, n_x2, n_x3
        iteration += 1
        print("Iteration "+str(iteration)+" /: x1 ="+str(x1)+", x2 = "+str(x2)+", x3 = "+str(x3))

    if e <= E:
        print("Converged!")
    else:
        print("Reached maximum iterations without full convergence.")

    return x1, x2, x3
jacobi_recursive(40)
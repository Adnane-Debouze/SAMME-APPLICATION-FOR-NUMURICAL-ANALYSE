import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
x = [0, 1, 2]
y = [1, 3, 2]
L0_coeff = [1, -1.5, .5]
L1_coeff = [0, 2, -1]
L2_coeff = [0, -.5, .5]
# get the polynomial function
L0 = poly.Polynomial(L0_coeff)
L1 = poly.Polynomial(L1_coeff)
L2 = poly.Polynomial(L2_coeff)
x_new = np.arange(-1.0, 3.1, 0.1)
fig = plt.figure(figsize = (10,8))
plt.plot(x_new, L0(x_new), 'b', label = 'L0')
plt.plot(x_new, L1(x_new), 'r', label = 'L1')
plt.plot(x_new, L2(x_new), 'g', label = 'L2')
plt.plot(x, np.ones(len(x)), 'ko', x, np.zeros(len(x)), 'ko')
plt.title('Lagrange Basis Polynomials')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()
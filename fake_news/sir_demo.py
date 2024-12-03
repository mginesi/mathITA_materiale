from ipywidgets import *
import numpy as np
import matplotlib.pyplot as plt
import scipy

T = 15      # tempo finale
alpha = 2   # tasso di infezione
beta = 1    # tasso di rimozione
S_0 = 0.99  # suscettibili al tempo 0
I_0 = 0.01  # infetti al tempo 0
R_0 = 0.00  # rimossi al tempo 0

def odefun_sir(y, t, params):
    a = params[0]
    b = params[1]
    return (-a * y[0] * y[1], a * y[0] * y[1] - b * y[1], b * y[1])

t_span = np.linspace(0, T, 201)
sol = scipy.integrate.odeint(
    lambda y, t : odefun_sir(y, t, [alpha, beta]),
    [S_0, I_0, R_0], np.linspace(0, T, 201)
    )

plt.figure()
plt.plot(t_span, sol[:, 0], "-g", label="S")
plt.plot(t_span, sol[:, 1], "-y", label="I")
plt.plot(t_span, sol[:, 2], "-r", label="R")
plt.xlabel("t")
plt.legend()
plt.grid()
plt.show()

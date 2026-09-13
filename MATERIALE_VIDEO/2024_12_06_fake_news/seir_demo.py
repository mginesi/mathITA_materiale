from ipywidgets import *
import numpy as np
import matplotlib.pyplot as plt
import scipy

T = 25          # tempo finale
alpha = 3       # tasso di infezione
beta = 1        # tasso di rimozione
gamma = 2       # tasso di latenza
b = 0.01        # tasso di ingresso
sigma = 0.005   # tasso di uscita

S_0 = 0.99  # suscettibili al tempo 0
E_0 = 0.00  # latenti al tempo 0
I_0 = 0.01  # infetti al tempo 0
R_0 = 0.00  # rimossi al tempo 0

def odefun_seir(y, t, params):
    alpha = params[0]
    beta = params[1]
    gamma = params[2]
    b = params[3]
    sigma = params[4]
    dy = (
        b - alpha * y[0] * y[2] - sigma * y[0], # dS = b - α S I - σ S
        alpha * y[0] * y[2] - gamma * y[1] - sigma * y[1], # dE = α S I - γ E - σ E
        gamma * y[1] - beta * y[2] - sigma * y[2], # dI = γ E - β I - σ I
        beta * y[2] - sigma * y[3] # dR = β I - σ R
        )
    return dy

t_span = np.linspace(0, T, 201)
sol = scipy.integrate.odeint(
    lambda y, t : odefun_seir(y, t, [alpha, beta, gamma, b, sigma]),
    [S_0, E_0, I_0, R_0], np.linspace(0, T, 201)
    )

plt.figure()
plt.plot(t_span, sol[:, 0], "-g", label="S")
plt.plot(t_span, sol[:, 1], "-b", label="E")
plt.plot(t_span, sol[:, 2], "-y", label="I")
plt.plot(t_span, sol[:, 3], "-r", label="R")
plt.xlabel("t")
plt.legend()
plt.grid()
plt.show()


from ipywidgets import *
import numpy as np
import matplotlib.pyplot as plt
import scipy

T = 10
alpha = 3
beta = 1
gamma = 2
eta = 2
lmbda = 1
b = 0.01
sigma = 0.005

S_0 = 0.99  # suscettibili al tempo 0
V_0 = 0.00  # latenti al tempo 0
I_0 = 0.01  # infetti al tempo 0
R_0 = 0.00  # rimossi al tempo 0

def odefun_svir(y, t, params):
    alpha = params[0]
    beta = params[1]
    gamma = params[2]
    eta = params[3]
    lmbda = params[4]
    b = params[5]
    sigma = params[6]
    dy = (
        b - alpha * y[0] * y[2] - sigma * y[0] - lmbda * y[0], # b - alpha * S * I - sigma * S - lambda * S
        lmbda * y[0] - eta * alpha * y[1] * y[2] - sigma * y[1], # lambda * S - eta * alpha * V * I - sigma * V
        alpha * y[0] * y[2] + eta * alpha * y[1] * y[2] - beta * y[2] - sigma * y[2], # alpha * S * I + eta * alpha * V * I - beta * I - sigma * I
        beta * y[2] - sigma * y[3], # beta * I - sigma * R
        )
    return dy

t_span = np.linspace(0, T, 201)
sol = scipy.integrate.odeint(
    lambda y, t : odefun_svir(y, t, [alpha, beta, gamma, eta, lmbda,  b, sigma]),
    [S_0, V_0, I_0, R_0], np.linspace(0, T, 201)
    )

plt.figure()
plt.plot(t_span, sol[:, 0], "-g", label="S")
plt.plot(t_span, sol[:, 1], "-b", label="V")
plt.plot(t_span, sol[:, 2], "-y", label="I")
plt.plot(t_span, sol[:, 3], "-r", label="R")
plt.xlabel("t")
plt.legend()
plt.grid()
plt.show()



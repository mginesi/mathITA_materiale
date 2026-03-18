import numpy as np
from matplotlib import pyplot as plt
from metodi_un_passo import eulero_e
from metodi_un_passo import eulero_i
from metodi_un_passo import trapz

N = 1000

# Equazione del pendolo y'' = -λ y' -g/l sin(y) dove y è l'angolo che l'asta del pendolo forma con la verticale
# In forma normale, z = [y', y]
# fun (t, z) = [-λz₀ - g/l sin(z₁), z₀]
lmbda = 0.5
g = 9.81 # gravità
l = 1 # m  lunghezza dell'asta

fun = lambda t,z : np.array([-lmbda*z[0]-g/l*np.sin(z[1]), z[0]])
jfun = lambda t,z : np.array([
    [-lmbda, -g/l*np.cos(z[1])],
    [1, 0]])
y0 = np.array([0.0, np.pi/3])
t_lim = [0.0, 10.0]


(t_span, Y_span_ee) = eulero_e(fun, y0, t_lim, N)
(_, Y_span_ei) = eulero_i(fun, jfun, y0, t_lim, N)
(_, Y_span_tr) = trapz(fun, jfun, y0, t_lim, N)

# PLOT 1: andamento di y rispetto a t #
plt.figure(figsize=(5,5))
plt.plot(t_span, Y_span_ee[:, 1], label="ee")
plt.plot(t_span, Y_span_ei[:, 1], label="ei")
plt.plot(t_span, Y_span_tr[:, 1], label="tr")
plt.legend()
plt.xlabel("t")
plt.ylabel("y")

# PLOT 2: andamento di y' rispetto a t #
plt.figure(figsize=(5,5))
plt.plot(t_span, Y_span_ee[:, 0], label="ee")
plt.plot(t_span, Y_span_ei[:, 0], label="ei")
plt.plot(t_span, Y_span_tr[:, 0], label="tr")
plt.legend()
plt.xlabel("t")
plt.ylabel("y'")


# PLOT 3: ritratto di fase #
plt.figure(figsize=(5,5))
plt.plot(Y_span_ee[:, 1], Y_span_ee[:, 0], label="ee")
plt.plot(Y_span_ei[:, 1], Y_span_ei[:, 0], label="ei")
plt.plot(Y_span_tr[:, 1], Y_span_tr[:, 0], label="tr")
plt.legend()
plt.xlabel("y")
plt.ylabel("y'")

plt.show()




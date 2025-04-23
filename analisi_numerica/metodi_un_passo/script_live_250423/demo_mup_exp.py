import numpy as np
from matplotlib import pyplot as plt
from metodi_un_passo import eulero_e
from metodi_un_passo import eulero_i
from metodi_un_passo import trapz


# Testiamo il metodo su y' = ay
a = 1
fun = lambda t,y : a*y
jfun = lambda t,y : np.array([[a]])
y0 = np.array([1.0])
t_lim = [0.0, 2.0]

# E.E.
(t_span_5, Y_sol_5) = eulero_e(fun, y0, t_lim, 5)
(t_span_10, Y_sol_10) = eulero_e(fun, y0, t_lim, 10)
(t_span_20, Y_sol_20) = eulero_e(fun, y0, t_lim, 20)
(t_span_50, Y_sol_50) = eulero_e(fun, y0, t_lim, 50)

plt.figure(figsize=(5,5))
plt.plot(t_span_50, np.exp(a * t_span_50), "-k", label="sol ex")
plt.plot(t_span_5, Y_sol_5, "--", label="sol ap 5")
plt.plot(t_span_10, Y_sol_10, "--", label="sol ap 10")
plt.plot(t_span_20, Y_sol_20, "--", label="sol ap 20")
plt.plot(t_span_50, Y_sol_50, "--", label="sol ap 50")
plt.legend()

# E.I.
(t_span_5, Y_sol_5) = eulero_i(fun, jfun, y0, t_lim, 5)
(t_span_10, Y_sol_10) = eulero_i(fun, jfun, y0, t_lim, 10)
(t_span_20, Y_sol_20) = eulero_i(fun, jfun, y0, t_lim, 20)
(t_span_50, Y_sol_50) = eulero_i(fun, jfun, y0, t_lim, 50)

plt.figure(figsize=(5,5))
plt.plot(t_span_50, np.exp(a * t_span_50), "-k", label="sol ex")
plt.plot(t_span_5, Y_sol_5, "--", label="sol ap 5")
plt.plot(t_span_10, Y_sol_10, "--", label="sol ap 10")
plt.plot(t_span_20, Y_sol_20, "--", label="sol ap 20")
plt.plot(t_span_50, Y_sol_50, "--", label="sol ap 50")
plt.legend()

# trapezi
(t_span_5, Y_sol_5) = trapz(fun, jfun, y0, t_lim, 5)
(t_span_10, Y_sol_10) = trapz(fun, jfun, y0, t_lim, 10)
(t_span_20, Y_sol_20) = trapz(fun, jfun, y0, t_lim, 20)
(t_span_50, Y_sol_50) = trapz(fun, jfun, y0, t_lim, 50)

plt.figure(figsize=(5,5))
plt.plot(t_span_50, np.exp(a * t_span_50), "-k", label="sol ex")
plt.plot(t_span_5, Y_sol_5, "--", label="sol ap 5")
plt.plot(t_span_10, Y_sol_10, "--", label="sol ap 10")
plt.plot(t_span_20, Y_sol_20, "--", label="sol ap 20")
plt.plot(t_span_50, Y_sol_50, "--", label="sol ap 50")
plt.legend()



plt.show()







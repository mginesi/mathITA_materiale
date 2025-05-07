import numpy as np
from matplotlib import pyplot as plt
from metodi_un_passo import eulero_e
from metodi_un_passo import eulero_i
from metodi_un_passo import trapz

# DEFINIAMO LA FUNZIONE DI TEST #
# oscillatore armonico y'' = -A² y
# la cui soluzione è y = K sin(At + φ)

A = 1
y0 = np.array([1.0, 0.0])
TF = 10

# in forma normale f(y', y) = f(z0, z1) = [-A²z1, z0]
fun = lambda t, z : np.array([-A**2*z[1], z[0]])
jfun = lambda t, z : np.array([
    [0, -A**2],
    [1, 0]])
t_lim = [0, TF]
sol_tf = np.array([np.cos(TF), np.sin(TF)])

N_range = 2 ** np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
# inizializziamo i vettori di errore
err_ee = np.zeros(N_range.size)
err_ei = np.zeros(N_range.size)
err_tr = np.zeros(N_range.size)

for count, _N in enumerate(N_range):
    # calcoliamo la soluzione con _N passi
    (_, Y_sol_ee) = eulero_e(fun, y0, t_lim, _N)
    (_, Y_sol_ei) = eulero_i(fun, jfun, y0, t_lim, _N)
    (_, Y_sol_tr) = trapz(fun, jfun, y0, t_lim, _N)
    # calcoliamo l'errore commesso
    err_ee[count] = np.linalg.norm(sol_tf - Y_sol_ee[-1])
    err_ei[count] = np.linalg.norm(sol_tf - Y_sol_ei[-1])
    err_tr[count] = np.linalg.norm(sol_tf - Y_sol_tr[-1])

ord1 = err_ee[-1] * (N_range / N_range[-1]) ** (-1)
ord2 = err_tr[-1] * (N_range / N_range[-1]) ** (-2)

plt.figure(figsize=(5,5))
plt.loglog(N_range, err_ee, "o", label="ee")
plt.loglog(N_range, err_ei, "^", label="ei")
plt.loglog(N_range, err_tr, "*", label="tr")
plt.loglog(N_range, ord1, "-", label="ord1")
plt.loglog(N_range, ord2, "-", label="ord2")
plt.legend()
plt.xlabel("N")
plt.ylabel("err")

plt.show()




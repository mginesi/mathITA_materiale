import numpy as np
import copy

def newton_m(_fun, _jfun, _yf):
    flag_conv = False # controllo di convergenza
    count = 0
    while not flag_conv:
        count += 1
        _yf -= np.linalg.solve(_jfun(_yf), _fun(_yf))
        if np.linalg.norm(_fun(_yf)) < 1e-08:
            flag_conv = True
        if count > 1000:
            flag_conv = True
    return _yf

# Metodo di Eulero esplicito (in avanti) #
def eulero_e(fun, y0, t_lim, N):
    # fun(t, y)
    # y0 dato iniziale come np.array
    # tlim lista di due elementi (tempo iniziale e tempo finale)
    # N intero che dice quanti passi temporali utilizzare (oltre a t0)
    n_dim = y0.size # dimensionalità del vettore incognita
    # inizializziamo la soluzione
    t_span = np.linspace(t_lim[0], t_lim[1], N+1)
    Y_sol = np.zeros([N+1, n_dim])
    # calcoliamo il passo temporale
    dt = t_span[1] - t_span[0] # (t_lim[1] - t_lim[0])/(N+1)
    # aggiungiamo il dato iniziale alla matrice delle soluzioni 
    Y_sol[0] = y0
    # ciclo for col metodo
    for _n, _t in enumerate(t_span[:-1]):
        _yn = Y_sol[_n] # soluzione presente
        _tn = _t # tempo presente
        _yf = _yn + dt * fun(_tn, _yn) # metodo di Eulero
        Y_sol[_n+1] = _yf # salviamo la soluzione nella matrice

    return (t_span, Y_sol)

# Metodo di Eulero implicito (all'indietro) #
def eulero_i(fun, jfun, y0, t_lim, N):
    # fun(t, y) -> n_dim array
    # jfun(t, y) -> n_dim × n_dim array
    # y0 dato iniziale come np.array
    # tlim lista di due elementi (tempo iniziale e tempo finale)
    # N intero che dice quanti passi temporali utilizzare (oltre a t0)
    n_dim = y0.size # dimensionalità del vettore incognita
    # inizializziamo la soluzione
    t_span = np.linspace(t_lim[0], t_lim[1], N+1)
    Y_sol = np.zeros([N+1, n_dim])
    # calcoliamo il passo temporale
    dt = t_span[1] - t_span[0] # (t_lim[1] - t_lim[0])/(N+1)
    # aggiungiamo il dato iniziale alla matrice delle soluzioni 
    Y_sol[0] = y0
    # ciclo for col metodo
    for _n, _t in enumerate(t_span[:-1]):
        _yn = Y_sol[_n] # soluzione presente
        _tn = _t # tempo presente
        _tf = _t + dt # tempo futuro
        _yf = copy.deepcopy(_yn) # guess iniziale per risolvere il problema non-lineare di E.I.
        _fun = lambda y : y - (_yn + dt * fun(_tf, y)) # funzione da azzerare per avere _yf = y
        _jfun = lambda y : np.eye(n_dim) - (dt * jfun(_tf, y)) # jacobiano di _fun
        Y_sol[_n+1] = newton_m(_fun, _jfun, _yf) # la soluzione si calcola con Newton

    return (t_span, Y_sol)

# Metodo dei trapezi #
def trapz(fun, jfun, y0, t_lim, N):
    # fun(t, y) -> n_dim array
    # jfun(t, y) -> n_dim × n_dim array
    # y0 dato iniziale come np.array
    # tlim lista di due elementi (tempo iniziale e tempo finale)
    # N intero che dice quanti passi temporali utilizzare (oltre a t0)
    n_dim = y0.size # dimensionalità del vettore incognita
    # inizializziamo la soluzione
    t_span = np.linspace(t_lim[0], t_lim[1], N+1)
    Y_sol = np.zeros([N+1, n_dim])
    # calcoliamo il passo temporale
    dt = t_span[1] - t_span[0] # (t_lim[1] - t_lim[0])/(N+1)
    # aggiungiamo il dato iniziale alla matrice delle soluzioni 
    Y_sol[0] = y0
    # ciclo for col metodo
    for _n, _t in enumerate(t_span[:-1]):
        _yn = Y_sol[_n] # soluzione presente
        _tn = _t # tempo presente
        _tf = _t + dt # tempo futuro
        _yf = copy.deepcopy(_yn) # guess iniziale per risolvere il problema non-lineare di trapezi
        _fun = lambda y : y - (_yn + dt/2 * fun(_tn, _yn) + dt/2 * fun(_tf, y)) # funzione da azzerare per avere _yf = y
        _jfun = lambda y : np.eye(n_dim) - (dt/2 * jfun(_tf, y)) # jacobiano di _fun
        Y_sol[_n+1] = newton_m(_fun, _jfun, _yf) # la soluzione si calcola con Newton

    return (t_span, Y_sol)











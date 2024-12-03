from ipywidgets import *
import numpy as np
import matplotlib.pyplot as plt
import scipy

T = 200
N = 100  # suscettibili al tempo 0

def daley_kendall(N, T):
    def give_next(state):
        X = state[0]
        Y = state[1]
        denom = N - 0.5 * (Y - 1)
        prob_dens = np.array([X, 0.5*(Y-1), N+1-X-Y]) / denom
        prob_cdf = np.cumsum(prob_dens)
        x = np.random.rand()
        if x < prob_cdf[0]:
            new_state = np.array([X-1, Y+1])
        elif x < prob_cdf[1]:
            new_state = np.array([X, Y-2])
        else:
            new_state = np.array([X, Y-1])
        if any(new_state < 0):
            return state
        else:
            return new_state

    state_list = [np.array([N, 1])]
    _t = 0
    while _t <= T and state_list[-1][1] > 0:
        new_state = give_next(state_list[-1])
        state_list.append(new_state)
        _t += 1
    for _ in range(_t, T):
        state_list.append(state_list[-1])

    return state_list

def prob_passaggio_DK(N):
    M = np.zeros([N+3, N+3])
    # Antidiagonal X, N-x
    p = [0 for _ in range(N+1)]
    p[N] = 1
    for _x in range(N-1, -1, -1):
        p[_x] = p[_x+1] * 2 * (_x + 1) / (N + _x + 1)
    #p = [_p / max(p) for _p in p]
    for _n in range(N+1):
        M[_n][N-_n+1] = p[_n]
    #M[N][0] = 0
    for _d in range(N-1, -1, -1):
        for _y in range(0, _d+1):
            #_y = N - _x - 1 # TODO: loop
            _x = _d - _y
            #_x = 
            if _y == 0:
                M[_x][_y] = M[_x][2]/(2*N - 1) + (N-_x)/N * M[_x][1]
            elif _y == 1:
                M[_x][_y] = M[_x][3] / (N-1) + 2*(N - _x - 1)/(2*N-1) * M[_x][2]
            else:
                M[_x][_y] = 2*(_x+1)/(2*N-_y+2)*M[_x+1][_y-1] + (_y+1)/(2*N-_y-1)*M[_x][_y+2] + 2*(N-_x-_y)/(2*N-_y)*M[_x][_y+1]
    p_x = M[:, 0]
    return p_x

state_list = daley_kendall(N, T)
point_x = [state_list[_n][0] for _n in range(T)]
point_y = [state_list[_n][1] for _n in range(T)]
point_z = [(N+1-state_list[_n][0] - state_list[_n][1]) for _n in range(T)]

plt.figure()
plt.plot(range(T), point_x, "-g", label="S")
plt.plot(range(T), point_y, "-y", label="I")
plt.plot(range(T), point_z, "-r", label="R")
plt.xlabel("t")

plt.legend()
plt.title("evoluzione")
plt.grid()

plt.figure()
plt.title("probabilità rimangano m ignoranti")
plt.bar(range(N+3), prob_passaggio_DK(N))
plt.xlabel("m")

plt.show()




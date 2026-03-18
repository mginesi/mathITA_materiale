import numpy as np
from matplotlib import pyplot as plt

def plot_point(x_list):
    # x_list deve essere una lista di numeri
    # il dominio e le etichette sulla ascissa sono determinate dal primo elemento
    # della lista
    x_span = [_n for _n in range(len(x_list[0]))]
    xtk = ["X_" + str(_n+1) for _n in range(len(x_list[0]))]
    y_span_lst = []
    for x in x_list:
        # controlliamo che x abbia la stessa lunghezza di tutti gli elementi
        if len(x) == len(x_list[0]):
            y_span = x
            y_span_lst.append(y_span)
        else:
            RuntimeError("attenzione, non tutti i punti hanno la stessa dimensionalità")
    return (x_span, y_span_lst, xtk)

def find_line(ptA, ptB):
    # trova la rappresentazione in CP della linea che passa per A e B
    if not(len(ptA) == len(ptB)):
        RuntimeError("attenzione: i due punti devono avere lunghezza uguale")
    ndim = len(ptA)
    x_out = []
    y_out = []
    name_out = ["l_" + str(_n) + "," + str(_n+1) for _n in range(1, ndim)]
    for _n in range(ndim-1):
        y_i = ptA[_n]
        y_ip = ptA[_n+1]
        z_i = ptB[_n]
        z_ip = ptB[_n+1]
        lmbda = (-y_ip + z_ip) / ((y_i - y_ip) - (z_i - z_ip))
        _x = lmbda * (_n) + (1-lmbda) * (_n+1)
        _y = lmbda * y_i + (1-lmbda) * (y_ip)
        x_out.append(_x)
        y_out.append(_y)
    return (x_out, y_out, name_out)

def find_plane(ptA, ptB, ptC):
    # trova la rappresentazione in CP del piano che passa per A, B, e C
    if not(len(ptA) == len(ptB)):
        RuntimeError("attenzione: i due punti devono avere lunghezza uguale")
    if not(len(ptC) == len(ptB)):
        RuntimeError("attenzione: i due punti devono avere lunghezza uguale")
    (x_AB, y_AB, name_out) = find_line(ptA, ptB)
    (x_BC, y_BC, name_out) = find_line(ptB, ptC)
    (x_AC, y_AC, name_out) = find_line(ptA, ptC)
    ndim = len(ptA)
    x_plane = []
    y_plane = []
    name_out = ["p_" + str(_n) + "," + str(_n+1) + "," + str(_n+2) for _n in range(1, ndim-1)]
    for _d in range(ndim - 2):
        x1 = x_AB[_d + 0]
        x2 = x_AB[_d + 1]
        y1 = y_AB[_d + 0]
        y2 = y_AB[_d + 1]
        z1 = x_AC[_d + 0]
        z2 = x_AC[_d + 1]
        w1 = y_AC[_d + 0]
        w2 = y_AC[_d + 1]
        mtrx_inter = np.array([
            [x1-x2, z1-z2],
            [y1-y2, w1-w2]
            ])
        trm_noto_inter = np.array([
            z2-x2, w2 - y2
            ])
        lm_sol = np.linalg.solve(mtrx_inter, trm_noto_inter)
        lmda = lm_sol[0]
        mu = -lm_sol[1]
        _x_plane = lmda * x1 + (1-lmda) * x2
        _y_plane = lmda * y1 + (1-lmda) * y2
        x_plane.append(_x_plane)
        y_plane.append(_y_plane)
    return (x_plane, y_plane, name_out)












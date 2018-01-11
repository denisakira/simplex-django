import numpy as np


def canto_noroeste(oferta, demanda):
    c = np.zeros((oferta.size, demanda.size))
    i = 0
    j = 0
    auxoferta = np.copy(oferta)
    auxdemanda = np.copy(demanda)
    while i < auxoferta.size and j < auxdemanda.size:
        if auxoferta[i] > auxdemanda[j]:
            c[i][j] = auxdemanda[j]
            auxoferta[i] = auxoferta[i] - auxdemanda[j]
            j += 1
        else:
            c[i][j] = auxoferta[i]
            auxdemanda[j] = auxdemanda[j] - auxoferta[i]
            i += 1

    return c


def simplex_transporte(oferta, demanda, peso, c):
    b = []
    xB = np.copy(c)
    for i in range(oferta.size):
        for j in range(demanda.size):
            if c[i][j] != 0:
                b = np.append(b, peso[i][j])

    uv = np.zeros([b.size,(oferta.size+demanda.size)])
    k = 0
    for i in range(oferta.size):
        for j in range(demanda.size):
            if c[i][j] != 0:
                uv[k][i] = 1
                uv[k][j+oferta.size] = 1
                k += 1

    if len(uv[1,:]) != b.size:
        uv = np.delete(uv, 0, axis=1)

    x = np.linalg.solve(uv,b)
    x = np.insert(x, 0, 0)

    cr = np.copy(c)
    for i in range(oferta.size):
        for j in range(demanda.size):
            if c[i][j] == 0:
                cr[i][j] = peso[i][j] - x[i] - x[j+oferta.size]

    if min(cr) >= 0:
        return

    min_index = np.unravel_index(cr.argmin(), cr.shape)
    check_u = False
    check_v = False
    u = min_index[0]
    v = min_index[1]
    d_u = u
    d_v = v
    check = False
    ciclo_pos = [cr[u][v]]
    ciclo_neg = []
    p_ciclo_neg = []
    p_ciclo_pos = []
    while not check:
        while not check_u:
            d_u += 1
            if d_u >= oferta.size:
                d_u = 0
            if c[d_u][v] != 0:
                check_u = True
                ciclo_neg = np.append(ciclo_neg, cr[d_u][v])
                p_ciclo_neg.append([d_u, v])

        while not check_v:
            d_v += 1
            if d_v >= demanda.size:
                d_v = 0
            if c[u][d_v] != 0:
                check_v = True
                ciclo_neg = np.append(ciclo_neg, cr[u][d_v])
                p_ciclo_neg.append([u, d_v])

        if check_u and check_v:
            if c[d_u][d_v] != 0:
                check = True
                ciclo_pos = np.append(ciclo_pos, cr[d_u][d_v])
                p_ciclo_pos = [d_u, d_v]
            else:
                check_u = False
                check_v = False

    min_cn = float(min(ciclo_neg))
    min_index_cn = int(np.argmin(ciclo_neg))
    max_index_cn = int(np.argmax(ciclo_neg))

    min_index_c = p_ciclo_neg[min_index_cn]
    max_index_c = p_ciclo_neg[max_index_cn]

    aux = cr[min_index_c[0]][min_index_c[1]]
    cr[min_index_c[0]][min_index_c[1]] = -cr[u][v]
    cr[u][v] = aux

    cr[max_index_c[0]][max_index_c[1]] = float(cr[max_index_c[0]][max_index_c[1]]) - min_cn
    cr[d_u][d_v] = float(cr[d_u][d_v]) + min_cn

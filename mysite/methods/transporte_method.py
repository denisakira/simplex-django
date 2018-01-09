import numpy as np


def canto_noroeste(oferta, demanda):
    c = np.zeros((oferta.size, demanda.size))
    i = 0
    j = 0
    while i < oferta.size and j < demanda.size:
        if oferta[i]>demanda[j]:
            c[i][j] = demanda[j]
            oferta[i] = oferta[i] - demanda[j]
            j += 1
        else:
            c[i][j] = oferta[i]
            demanda[j] = demanda[j] - oferta[i]
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
    k=0
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

    minIndex = np.unravel_index(cr.argmin(), cr.shape)

    check_u = False
    check_v = False
    u = minIndex[0]
    v = minIndex[1]
    check = False
    ciclo_pos = [c[u][v]]
    ciclo_neg = []

    while not check:
        if not check_u:
            u += 1
            if c[u][v] != 0:
                check_u = True
                ciclo_neg = np.append(ciclo_neg, c[u][v])

        if not check_v:
            v += 1
            if c[u][v] != 0:
                check_v = True
                ciclo_neg = np.append(ciclo_neg, c[u][v])

        if ciclo_pos and ciclo_neg:
            pass

        check = True


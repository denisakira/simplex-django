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


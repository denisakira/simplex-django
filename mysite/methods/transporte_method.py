import numpy as np


def canto_noroeste(oferta, demanda):
    c = np.zeros((oferta.size,demanda.size))
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

    print(c)
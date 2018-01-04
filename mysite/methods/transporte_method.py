import numpy as np
import pandas as pd

def canto_noroeste(oferta, demanda):
    c = np.zeros((oferta.size,demanda.size))
    i=0
    j=0
    while i < oferta.size and j < demanda.size:
        if oferta[i]>demanda[j]:
            c[i][j] = demanda[j]
            aux = oferta[i] - demanda[j]
            j+=1
        else:
            c[i][j] = oferta[i]
            aux = demanda[j] - oferta[i]
            i+=1

    print(c)
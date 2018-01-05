import numpy as np


def no_ficticio(obj):
    oferta = obj[0]
    demanda = obj[1]
    peso = obj[2]

    if oferta.sum() > demanda.sum():
        demanda = np.append(demanda, (oferta.sum() - demanda.sum()))
        k = 0
        aux = []
        for i in peso:
            i = np.append(i,0)
            aux.append(i)
            k+=1
        peso = aux
    elif oferta.sum() < demanda.sum():
        oferta = np.append(oferta, (demanda.sum() - oferta.sum()))
        peso = np.append(peso, [np.zeros(demanda.size)], axis=0)

    obj = [oferta, demanda, peso]
    return obj


def get_transporte_data(of,dem, p):
    oferta = []
    for i in of:
        oferta = np.append(oferta,np.fromiter(iter(i.values()), dtype=float))

    demanda = []
    for i in dem:
        demanda = np.append(demanda, np.fromiter(iter(i.values()), dtype=float))

    peso = []
    for i in p:
        peso = np.append(peso, np.fromiter(iter(i.values()), dtype=float))
    peso = np.reshape(peso, (oferta.size,demanda.size))

    obj = [oferta, demanda, peso]
    obj = no_ficticio(obj)

    return obj
import numpy as np


def no_ficticio(obj):
    oferta = obj[0]
    demanda = obj[1]

    if oferta.sum() > demanda.sum():
        demanda = np.append(demanda, (oferta.sum() - demanda.sum()))
    else:
        oferta = np.append(oferta, (demanda.sum() - oferta.sum()))

    obj = [oferta,demanda]
    return obj


def get_transporte_data(of,dem):
    oferta = []
    for i in of:
        oferta = np.append(oferta,np.fromiter(iter(i.values()), dtype=float))

    demanda = []
    for i in dem:
        demanda = np.append(demanda, np.fromiter(iter(i.values()), dtype=float))

    obj = [oferta, demanda]
    obj = no_ficticio(obj)

    print(obj)

    return obj
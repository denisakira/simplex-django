import numpy as np

def simplex(cN,cB,N,B,b):
    try:
        xB = np.linalg.solve(B, b)

        Lambda = np.linalg.solve((np.transpose(B)), cB)

        cNr = []

        aux = np.transpose(N)

        for i in range(2):
            cNr.append(cN[i] - np.dot(np.asarray(Lambda), np.transpose(aux[i:i + 1])))


        if np.ndarray.min(np.asarray(cNr)) > 0:
            return xB

        indexN = np.argmin(cNr)

        y = np.linalg.solve(B, aux[indexN])

        if y.any() < 0:
            return [0,0]

        E = []
        for i in range(2):
            E.append(xB[i] / y[i])

        indexB = np.argmin(E)

        Nt = np.transpose(N)
        Bt = np.transpose(B)

        Nfinal = np.array(Nt)
        Bfinal = np.array(Bt)
        cBfinal = np.array(cB)
        cNfinal = np.array(cN)

        auxN = Nt[indexN]
        auxB = Bt[indexB]
        auxcB = cB[indexB]
        auxcN = cN[indexN]

        Nfinal[indexN] = auxB
        Bfinal[indexB] = auxN
        cNfinal[indexN] = auxcB
        cBfinal[indexB] = auxcN

        B = np.transpose(Bfinal)
        N = np.transpose(Nfinal)
        cB = cBfinal
        cN = cNfinal

        xB = simplex(cN, cB, N, B, b)

        return xB

    except np.linalg.linalg.LinAlgError as err:
        if 'Singular matrix' in err.message:
            return [0,0]
        else:
            raise




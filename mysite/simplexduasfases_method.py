import numpy as np
from .simplex import simplex_v2
def simplexduasfases_method(m,c,b,cB,A,cR,cA,cRA,cAB):
    if m.get('z')=='max':
        #MAXIMIZACAO
        cR = c - np.dot(cB,A)

        cRA = cA - np.dot(cAB,A)

        z=0
        for i in range(len(cB)):
            z = z + b[i]*cAB[i]

        if cRA.all()>=0:
            z=simplex_v2(m,c,b,cB,A,cR)
            return -z

        indexN = np.argmin(cRA)

        bA = []
        for i in range(len(b)):
            if A[i][indexN] == 0:
                return None
            else:
                bA.append(b[i]/A[i][indexN])

        if max(bA)<0:
            return float("inf")

        mask = np.ma.masked_less_equal(bA,0)
        indexB = np.argmin(mask)

        aux0 = []
        aux1 = []
        for i in range(len(A[0])):
            aux0.append(A[indexB][i]/A[indexB][indexN])
        b[indexB] = b[indexB]/A[indexB][indexN]

        for i in range(len(A[0])):
            aux1.append(A[not indexB][i] - aux0[i]*A[not indexB][indexN])
        b[not indexB] = b[not indexB] - b[indexB]*A[not indexB][indexN]

        cB[indexB] = c[indexN]

        cAB[indexB] = cA[indexN]

        A = [aux0,aux1]

        z = simplexduasfases_method(m,c,b,cB,A,cR,cA,cRA,cAB)

        return z

    #MINIMIZACAO
    elif m.get('z')=='min':
        #MAXIMIZACAO
        cR = c - np.dot(cB,A)

        cRA = cA - np.dot(cAB,A)

        z=0
        for i in range(len(cB)):
            z = z + b[i]*cAB[i]

        if cRA.all()>=0:
            z=simplex_v2(m,c,b,cB,A,cR)
            return z

        indexN = np.argmin(cRA)

        bA = []
        for i in range(len(b)):
            if A[i][indexN] == 0:
                return None
            else:
                bA.append(b[i]/A[i][indexN])

        if max(bA)<0:
            return float("inf")

        mask = np.ma.masked_less_equal(bA,0)
        indexB = np.argmin(mask)

        aux0 = []
        aux1 = []
        for i in range(len(A[0])):
            aux0.append(A[indexB][i]/A[indexB][indexN])
        b[indexB] = b[indexB]/A[indexB][indexN]

        for i in range(len(A[0])):
            aux1.append(A[not indexB][i] - aux0[i]*A[not indexB][indexN])
        b[not indexB] = b[not indexB] - b[indexB]*A[not indexB][indexN]

        cB[indexB] = c[indexN]

        cAB[indexB] = cA[indexN]

        A = [aux0,aux1]

        z = simplexduasfases_method(m,c,b,cB,A,cR,cA,cRA,cAB)

        return z


def simplex3duasfases_method():
    pass
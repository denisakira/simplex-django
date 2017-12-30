import numpy as np
from mysite.methods.simplex_method import simplex_v2, simplex3_v2

def simplexduasfases_method(m,c,b,cB,A,cR,cA,cRA,cAB):
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
    aux2 = []
    for i in range(len(A[0])):
        aux0.append(A[indexB][i]/A[indexB][indexN])
    b[indexB] = b[indexB]/A[indexB][indexN]

    for j in range(len(A)):
        if j!=indexB:
            for i in range(len(A[0])):
                aux1.append(A[j][i] - aux0[i] * A[j][indexN])
            b[j] = b[j] - b[indexB] * A[j][indexN]
            aux2.append(aux1)
            del aux1
            aux1=[]

    cB[indexB] = c[indexN]

    k=0
    for i in range(len(A)):
        if i == indexB:
            A[i] = aux0
        else:
            A[i] = aux2[k]
            k+=1

    z = simplexduasfases_method(m,c,b,cB,A,cR,cA,cRA,cAB)

    return z


def simplex3duasfases_method(m,c,b,cB,A,cR,cA,cRA,cAB):
    # MAXIMIZACAO
    cR = c - np.dot(cB, A)

    cRA = cA - np.dot(cAB, A)

    z = 0
    for i in range(len(cB)):
        z = z + b[i] * cB[i]

    if min(cR) >= 0:
        z=simplex3_v2(m,c,b,cB,A,cR)
        return z

    indexN = np.argmin(cRA)

    bA = []
    for i in range(len(b)):
        if A[i][indexN] == 0:
            return None
        else:
            bA.append(b[i] / A[i][indexN])

    if max(bA) < 0:
        return float("inf")

    mask = np.ma.masked_less_equal(bA, 0)
    indexB = np.argmin(mask)

    aux0 = []
    aux1 = []
    aux2 = []
    for i in range(len(A[0])):
        aux0.append(A[indexB][i] / A[indexB][indexN])
    b[indexB] = b[indexB] / A[indexB][indexN]
    for j in range(len(A)):
        if j != indexB:
            for i in range(len(A[0])):
                aux1.append(A[j][i] - aux0[i] * A[j][indexN])
            b[j] = b[j] - b[indexB] * A[j][indexN]
            aux2.append(aux1)
            del aux1
            aux1 = []

    cB[indexB] = c[indexN]

    k=0
    for i in range(len(A)):
        if i == indexB:
            A[i] = aux0
        else:
            A[i] = aux2[k]
            k+=1

    cAB[indexB] = cA[indexN]

    z = simplex3duasfases_method(m, c, b, cB, A, cR,cA,cRA,cAB)

    return z

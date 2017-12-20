import numpy as np

def simplex_v2(m,c,b,cB,A,cR):
    if m.get('z')=='max':
        #MAXIMIZACAO
        cR = c - np.dot(cB,A)

        z=0
        for i in range(len(cB)):
            z = z + b[i]*cB[i]

        if min(cR)>=0:
            return -z

        indexN = np.argmin(cR)

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

        A = [aux0,aux1]

        z = simplex_v2(m,c,b,cB,A,cR)

        return z

    #MINIMIZACAO
    elif m.get('z')=='min':
        cR = c - np.dot(cB,A)

        z=0
        for i in range(len(cB)):
            z = z + b[i]*cB[i]

        if min(cR)>=0:
            return z

        indexN = np.argmin(cR)

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

        A = [aux0,aux1]

        z = simplex_v2(m,c,b,cB,A,cR)

        return z

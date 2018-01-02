from mysite.methods.simplex_method import simplex_v2
import numpy as np
from mysite.handlers.data_handler import add_restr

def gomory_method(m,c,b,cB,A,cR):
    #Multiplicação vetorial
    cR = c - np.dot(cB,A)
    z=0
    for i in range(len(cB)):
        z = z + b[i]*cB[i]

    if min(cR)>=0:
        #Verifica se b possui somente valores inteiros
        cont = 0
        for i in range(b.size):
            if b[i]%1<=0.0001 or b[i]%1==0:
                cont+=1

        if cont == b.size:
            if m.get('z') == 'max':
                return -z
            else:
                return z

        #Chama o método que adiciona restrições e atualiza os dados
        obj = add_restr(A,b,c,cB)
        A = obj[0]
        b = obj[1]
        c = obj[2]
        cB = obj[3]

        z = gomory_method(m,c,b,cB,A,cR)
        return z

    #IndexN = valor mínimo do Custo Reduzido (cR)
    indexN = np.argmin(cR)

    #bA = b/A --> escolher o menor positivo
    bA = []
    for i in range(len(b)):
        if A[i][indexN] == 0:
            bA.append(999999)
        else:
            bA.append(b[i]/A[i][indexN])

    if max(bA)<0:
        return float("inf")
    if min(bA) == 999999:
        return None
    #Eliminar os valores menores que 0
    mask = np.ma.masked_less(bA,0)
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

    z = gomory_method(m,c,b,cB,A,cR)
    return z

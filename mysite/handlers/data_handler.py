import numpy as np

def get_data(m):
    M = 9999
    x1 = float(m.get('x1'))
    x2 = float(m.get('x2'))
    x3 = 0
    x4 = 0
    x5 = M
    x6 = M

    if m['rx3'] == '>' and m['rx4'] == '>':
        c = [x1, x2, x3, x4, x5, x6]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x5')), float(m.get('r1x6'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x5')), float(m.get('r2x6'))]

    elif m['rx3'] == '>' and m['rx4'] == '<':
        c = [x1, x2, x3, x4, x5]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x5'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x5'))]
    elif m['rx3'] == '<' and m['rx4'] == '>':
        c = [x1, x2, x3, x4, x5]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x6'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x6'))]
    else:
        c = [x1, x2, x3, x4]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4'))]

    A = [r1, r2]
    Obj = [c,A]

    return Obj

def get_datav2(m):
    M = 9999
    x1 = float(m.get('x1'))
    x2 = float(m.get('x2'))
    x3 = 0
    x4 = 0
    x5 = M
    x6 = M

    r1 = np.array([float(m.get('r1x1')), float(m.get('r1x2'))])
    r2 = np.array([float(m.get('r2x1')), float(m.get('r2x2'))])
    c = np.array([x1,x2])

    if m['rx3'] == '>':
        c = np.append(c,[x3,x5])
        r1 = np.append(r1,[float(m.get('r1x3')),float(m.get('r1x5'))])
        r2 = np.append(r2[float(m.get('r2x3')),float(m.get('r2x5'))])
    elif m['rx3'] == '<':
        c = np.append(c,[x3])
        r1 = np.append(r1,[float(m.get('r1x3'))])
        r2 = np.append(r2,[float(m.get('r2x3'))])
    elif m['rx3'] == '=':
        pass

    if m['rx4'] == '>':
        c = np.append(c,[x4,x6])
        r1 = np.append(r1,[float(m.get('r1x4')),float(m.get('r1x6'))])
        r2 = np.append(r2,[float(m.get('r2x4')),float(m.get('r2x6'))])
    elif m['rx4'] == '<':
        c = np.append(c,[x4])
        r1 = np.append(r1,float(m.get('r1x4')))
        r2 = np.append(r2,float(m.get('r2x4')))
    elif m['rx4'] == '=':
        pass

    A = [r1,r2]
    obj = [c,A]

    return obj

def get_data3(m):
    M = 9999
    x1 = float(m.get('x1'))
    x2 = float(m.get('x2'))
    x3 = 0
    x4 = 0
    x5 = M
    x6 = M
    x7 = 0
    x9 = M

    if m['rx3'] == '>' and m['rx4'] == '>' and m['rx7'] == '>':
        c = [x1, x2, x3, x4, x5, x6, x7, x9]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x5')), float(m.get('r1x6')),
              float(m.get('r1x7')), float(m.get('r1x9'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x5')), float(m.get('r2x6')),
              float(m.get('r2x7')), float(m.get('r2x9'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x5')), float(m.get('r3x6')),
              float(m.get('r3x7')), float(m.get('r3x9'))]


    elif m['rx3'] == '>' and m['rx4'] == '>' and m['rx7'] == '<':
        c = [x1, x2, x3, x4, x5, x6, x7]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x5')), float(m.get('r1x6')),
              float(m.get('r1x7'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x5')), float(m.get('r2x6')),
              float(m.get('r2x7'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x5')), float(m.get('r3x6')),
              float(m.get('r3x7'))]

    elif m['rx3'] == '>' and m['rx4'] == '<' and m['rx7'] == '>':
        c = [x1, x2, x3, x4, x5, x7, x9]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x5')),
              float(m.get('r1x7')), float(m.get('r1x9'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x5')),
              float(m.get('r2x7')), float(m.get('r2x9'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x5')),
              float(m.get('r3x7')), float(m.get('r3x9'))]

    elif m['rx3'] == '>' and m['rx4'] == '<' and m['rx7'] == '<':
        c = [x1, x2, x3, x4, x5, x7]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x5')),
              float(m.get('r1x7'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x5')),
              float(m.get('r2x7'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x5')),
              float(m.get('r3x7'))]

    elif m['rx3'] == '<' and m['rx4'] == '>' and m['rx7'] == '>':
        c = [x1, x2, x3, x4, x6, x7, x9]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x6')),
              float(m.get('r1x7')), float(m.get('r1x9'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x6')),
              float(m.get('r2x7')), float(m.get('r2x9'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x6')),
              float(m.get('r3x7')), float(m.get('r3x9'))]
    elif m['rx3'] == '<' and m['rx4'] == '>' and m['rx7'] == '<':
        c = [x1, x2, x3, x4, x6, x7]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x6')),
              float(m.get('r1x7'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x6')),
              float(m.get('r2x7'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x6')),
              float(m.get('r3x7'))]
    else:
        c = [x1, x2, x3, x4, x7]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x7'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x7'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x7'))]

    A = [r1,r2,r3]

    obj = [c,A]

    return obj

def get_data_duasfases(m):
    M = 9999
    x1 = float(m.get('x1'))
    x2 = float(m.get('x2'))
    x3 = 0
    x4 = 0
    x5 = M
    x6 = M

    if m['rx3'] == '>' and m['rx4'] == '>':
        c = [x1, x2, 0, 0, 0, 0]
        cA = [0, 0, 0, 0, 1, 1]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x5')), float(m.get('r1x6'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x5')), float(m.get('r2x6'))]

    elif m['rx3'] == '>' and m['rx4'] == '<':
        c = [x1, x2, 0, 0, 0]
        cA = [0, 0, 0, 0, 1]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x5'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x5'))]
    elif m['rx3'] == '<' and m['rx4'] == '>':
        c = [x1, x2, 0, 0, 0]
        cA = [0, 0, 0, 0, 1]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x6'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x6'))]
    else:
        c = [x1, x2, 0, 0]
        cA = [0, 0, 0, 0]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4'))]

    A = [r1,r2]

    obj = [c,cA,A]

    return obj

def get_data_duasfases3(m):
    M = 9999
    x1 = float(m.get('x1'))
    x2 = float(m.get('x2'))
    x3 = 0
    x4 = 0
    x5 = M
    x6 = M
    x7 = 0
    x9 = M

    if m['rx3'] == '>' and m['rx4'] == '>' and m['rx7'] == '>':
        c = [x1, x2, 0, 0, 0, 0, 0, 0]
        cA = [0, 0, 0, 0, 1, 1, 0, 1]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x5')), float(m.get('r1x6')),
              float(m.get('r1x7')), float(m.get('r1x9'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x5')), float(m.get('r2x6')),
              float(m.get('r2x7')), float(m.get('r2x9'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x5')), float(m.get('r3x6')),
              float(m.get('r3x7')), float(m.get('r3x9'))]
    elif m['rx3'] == '>' and m['rx4'] == '>' and m['rx7'] == '<':
        c = [x1, x2, 0, 0, 0, 0, 0]
        cA = [0, 0, 0, 0, 1, 1, 0]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x5')), float(m.get('r1x6')),
              float(m.get('r1x7'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x5')), float(m.get('r2x6')),
              float(m.get('r2x7'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x5')), float(m.get('r3x6')),
              float(m.get('r3x7'))]
    elif m['rx3'] == '>' and m['rx4'] == '<' and m['rx7'] == '>':
        c = [x1, x2, 0, 0, 0, 0, 0]
        cA = [0, 0, 0, 0, 1, 0, 1]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x5')),
              float(m.get('r1x7')), float(m.get('r1x9'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x5')),
              float(m.get('r2x7')), float(m.get('r2x9'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x5')),
              float(m.get('r3x7')), float(m.get('r3x9'))]
    elif m['rx3'] == '>' and m['rx4'] == '<' and m['rx7'] == '<':
        c = [x1, x2, 0, 0, 0, 0]
        cA = [0, 0, 0, 0, 1, 0]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x5')),
              float(m.get('r1x7'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x5')),
              float(m.get('r2x7'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x5')),
              float(m.get('r3x7'))]
    elif m['rx3'] == '<' and m['rx4'] == '>' and m['rx7'] == '>':
        c = [x1, x2, 0, 0, 0, 0, 0]
        cA = [0, 0, 0, 0, 1, 0, 1]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x6')),
              float(m.get('r1x7')), float(m.get('r1x9'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x6')),
              float(m.get('r2x7')), float(m.get('r2x9'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x6')),
              float(m.get('r3x7')), float(m.get('r3x9'))]
    elif m['rx3'] == '<' and m['rx4'] == '>' and m['rx7'] == '<':
        c = [x1, x2, 0, 0, 0, 0]
        cA = [0, 0, 0, 0, 1, 0]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x6')),
              float(m.get('r1x7')), float(m.get('r1x9'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x6')),
              float(m.get('r2x7')), float(m.get('r2x9'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x6')),
              float(m.get('r3x7')), float(m.get('r3x9'))]

    else:
        c = [x1, x2, 0, 0, 0]
        cA = [0, 0, 0, 0, 0]
        r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
              float(m.get('r1x4')), float(m.get('r1x7'))]
        r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
              float(m.get('r2x4')), float(m.get('r2x7'))]
        r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
              float(m.get('r3x4')), float(m.get('r3x7'))]

    A = [r1,r2,r3]
    obj = [c,cA,A]

def add_restr(A,b,c,cB):
    M = 9999

    for i in range(len(c)):
        if c[i]==M:
            indexDel = i
            c = np.delete(c,i,0)
            A = np.delete(A,i,1)


    # Em loop:
    # Pega o index do menor valor de b. Se for inteiro, cria uma máscara excluindo esse valor
    # Se não, sai do loop, e indexInt será o index.
    check = False
    while check != True:
        indexInt = np.argmin(b)
        if b[indexInt] % 1 == 0:
            b = np.ma.masked_where(b == b[indexInt], b)
        else:
            check = True

    #Atribui os valores encontrados a variáveis que compõe a nova linha de restrição
    AInt = np.array(A[indexInt]) % 1
    AInt = np.append(AInt,[-1,1])
    bInt = b[indexInt] % 1

#    tam = tamanho do eixo 0 (linhas) de A
#    São adicionados dois 0's para cada linha de A, representando o espaço para as novas
#    variáveis, que já foram adicionadas em AInt
    tam = np.size(A,0)
    A = np.append(A,np.array(tam*[[0,0]]), axis=1)

    A = np.append(A, [AInt], axis=0)
    b = np.append(b, bInt)
    c = np.append(c,[0,M])
    cB = np.append(cB,M)

    obj = [A,b,c,cB]

    return obj
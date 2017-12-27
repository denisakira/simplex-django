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

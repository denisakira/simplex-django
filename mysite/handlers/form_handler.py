def get_formdata(form):
    m = {}
    for i in form.data:
        if i == 'r1x1':
            m['r1x1'] = form[i].value()
        elif i == 'r1x2':
            m['r1x2'] = form[i].value()
        elif i == 'r2x1':
            m['r2x1'] = form[i].value()
        elif i == 'r2x2':
            m['r2x2'] = form[i].value()
        elif i == 'b1':
            m['b1'] = form[i].value()
        elif i == 'b2':
            m['b2'] = form[i].value()
        elif i == 'maxmin':
            if form[i].value() == "Max":
                m['z'] = 'max'
                m['x1'] = -float(form['x1'].value())
                m['x2'] = -float(form['x2'].value())
                cN = [m['x1'], m['x2']]
            else:
                m['z'] = 'min'
                m['x1'] = float(form['x1'].value())
                m['x2'] = float(form['x2'].value())
                cN = [m['x1'], m['x2']]
        elif i == 'maiormenorR1':
            if form[i].value() == ">=":
                m['rx3'] = '>'
                m['r1x3'] = -1
                m['r2x3'] = 0
                m['r1x5'] = 1
                m['r2x5'] = 0
            elif form[i].value() == "<=":
                m['rx3'] = '<'
                m['r1x3'] = 1
                m['r2x3'] = 0
            elif form[i].value() == "=":
                m['rx3'] = '='
        elif i == 'maiormenorR2':
            if form[i].value() == ">=":
                m['rx4'] = '>'
                m['r1x4'] = 0
                m['r2x4'] = -1
                m['r1x6'] = 0
                m['r2x6'] = 1
            elif form[i].value() == "<=":
                m['rx4'] = '<'
                m['r1x4'] = 0
                m['r2x4'] = 1
            elif form[i].value() == '=':
                m['rx4'] = '='
    return m

def get_formdata3(form):
    m = {}
    for i in form.data:
        if i == 'r1x1':
            m['r1x1'] = form[i].value()
        elif i == 'r1x2':
            m['r1x2'] = form[i].value()
        elif i == 'r2x1':
            m['r2x1'] = form[i].value()
        elif i == 'r2x2':
            m['r2x2'] = form[i].value()
        elif i == 'r3x1':
            m['r3x1'] = form[i].value()
        elif i == 'r3x2':
            m['r3x2'] = form[i].value()
        elif i == 'b1':
            m['b1'] = form[i].value()
        elif i == 'b2':
            m['b2'] = form[i].value()
        elif i == 'b3':
            m['b3'] = form[i].value()
        elif i == 'maxmin':
            if form[i].value() == "Max":
                m['z'] = 'max'
                m['x1'] = -float(form['x1'].value())
                m['x2'] = -float(form['x2'].value())
                cN = [m['x1'], m['x2']]
            else:
                m['z'] = 'min'
                m['x1'] = float(form['x1'].value())
                m['x2'] = float(form['x2'].value())
                cN = [m['x1'], m['x2']]

        elif i == 'maiormenorR1':
            if form[i].value() == ">=":
                m['rx3'] = '>'
                m['r1x3'] = -1
                m['r2x3'] = 0
                m['r3x3'] = 0
                m['r1x5'] = 1
                m['r2x5'] = 0
                m['r3x5'] = 0
            elif form[i].value() == "<=":
                m['rx3'] = '<'
                m['r1x3'] = 1
                m['r2x3'] = 0
                m['r3x3'] = 0
            elif form[i].value() == '=':
                m['rx4'] = '='

        elif i == 'maiormenorR2':
            if form[i].value() == ">=":
                m['rx4'] = '>'
                m['r1x4'] = 0
                m['r2x4'] = -1
                m['r3x4'] = 0
                m['r1x6'] = 0
                m['r2x6'] = 1
                m['r3x6'] = 0
            elif form[i].value() == "<=":
                m['rx4'] = '<'
                m['r1x4'] = 0
                m['r2x4'] = 1
                m['r3x4'] = 0
            elif form[i].value() == '=':
                m['rx4'] = '='

        elif i == 'maiormenorR3':
            if form[i].value() == ">=":
                m['rx7'] = '>'
                m['r1x7'] = 0
                m['r2x7'] = 0
                m['r3x7'] = -1
                m['r1x9'] = 0
                m['r2x9'] = 0
                m['r3x9'] = 1
            elif form[i].value() == "<=":
                m['rx7'] = '<'
                m['r1x7'] = 0
                m['r2x7'] = 0
                m['r3x7'] = 1
            elif form[i].value() == '=':
                m['rx4'] = '='

    return m


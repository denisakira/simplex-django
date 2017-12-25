# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import SimplexForm
from .simplex import simplex_v2,simplex3_v2
from .simplexduasfases_method import simplexduasfases_method, simplex3duasfases_method

# Create your views here.

def index(request):
    return render(request, 'mysite/index.html')


def thanks(request):
    return render(request, 'mysite/thanks.html')

def gomory(request):
    return render(request, 'mysite/gomory.html')

def simplex3(request):
    return render(request, 'mysite/simplex3.html')

def simplexduasfases(request):
    return render(request, 'mysite/simplexduasfases.html')

def simplex3duasfases(request):
    return render(request, 'mysite/simplex3duasfases.html')


def get_simplex(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SimplexForm(request.POST)
        # recebe todos os valores do form
        m = {}
        M=9999
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

        x1 = float(m.get('x1'))
        x2 = float(m.get('x2'))
        x3 = 0
        x4 = 0
        x5=M
        x6=M

        if m['rx3']=='>' and m['rx4']=='>':
            c=[x1,x2,x3,x4,x5,x6]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x5')),float(m.get('r1x6'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x5')),float(m.get('r2x6'))]

        elif m['rx3']=='>' and m['rx4']=='<':
            c=[x1,x2,x3,x4,x5]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x5'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x5'))]
        elif m['rx3']=='<' and m['rx4']=='>':
            c=[x1,x2,x3,x4,x5]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x6'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x6'))]
        else:
            c = [x1,x2,x3,x4]
            r1 = [float(m.get('r1x1')),float(m.get('r1x2')),float(m.get('r1x3')),
                  float(m.get('r1x4'))]
            r2 = [float(m.get('r2x1')),float(m.get('r2x2')),float(m.get('r2x3')),
                  float(m.get('r2x4'))]

        # primeira iteracao
        cB = [0, 0]

        b = [float(m.get('b1')), float(m.get('b2'))]

        A = [r1, r2]

        cR = [0,0]

        z = simplex_v2(m,c,b,cB,A,cR)

        if z==None:
            z = "não há solução"
        # check whether it's valid:
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        return render(request,'mysite/simplex.html',
                      {'z': z})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SimplexForm()

    return render(request, 'mysite/simplex.html', {'form': form})


def get_simplex3(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SimplexForm(request.POST)
        # recebe todos os valores do form
        m = {}
        M=9999
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


        x1 = float(m.get('x1'))
        x2 = float(m.get('x2'))
        x3 = 0
        x4 = 0
        x5=M
        x6=M
        x7 = 0
        x9 = M

        if m['rx3']=='>' and m['rx4']=='>' and m['rx7']=='>':
            c=[x1,x2,x3,x4,x5,x6,x7,x9]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x5')),float(m.get('r1x6')),
                  float(m.get('r1x7')), float(m.get('r1x9'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x5')),float(m.get('r2x6')),
                  float(m.get('r2x7')), float(m.get('r2x9'))]
            r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
                  float(m.get('r3x4')),float(m.get('r3x5')),float(m.get('r3x6')),
                  float(m.get('r3x7')), float(m.get('r3x9'))]


        elif m['rx3']=='>' and m['rx4']=='>' and m['rx7']=='<':
            c=[x1,x2,x3,x4,x5,x6,x7]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x5')),float(m.get('r1x6')),
                  float(m.get('r1x7'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x5')),float(m.get('r2x6')),
                  float(m.get('r2x7'))]
            r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
                  float(m.get('r3x4')), float(m.get('r3x5')), float(m.get('r3x6')),
                  float(m.get('r3x7'))]

        elif m['rx3']=='>' and m['rx4']=='<' and m['rx7']=='>':
            c=[x1,x2,x3,x4,x5,x7,x9]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x5')),
                  float(m.get('r1x7')), float(m.get('r1x9'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x5')),
                  float(m.get('r2x7')), float(m.get('r2x9'))]
            r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
                  float(m.get('r3x4')), float(m.get('r3x5')),
                  float(m.get('r3x7')), float(m.get('r3x9'))]

        elif m['rx3'] == '>' and m['rx4'] == '<' and m['rx7'] == '<':
            c = [x1, x2, x3, x4, x5,x7]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')), float(m.get('r1x5')),
                  float(m.get('r1x7'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')), float(m.get('r2x5')),
                  float(m.get('r2x7'))]
            r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
                  float(m.get('r3x4')), float(m.get('r3x5')),
                  float(m.get('r3x7'))]

        elif m['rx3']=='<' and m['rx4']=='>' and m['rx7']=='>':
            c=[x1,x2,x3,x4,x6,x7,x9]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x6')),
                  float(m.get('r1x7')), float(m.get('r1x9'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x6')),
                  float(m.get('r2x7')), float(m.get('r2x9'))]
            r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
                  float(m.get('r3x4')), float(m.get('r3x6')),
                  float(m.get('r3x7')), float(m.get('r3x9'))]
        elif m['rx3'] == '<' and m['rx4'] == '>' and m['rx7'] == '<':
            c = [x1, x2, x3, x4, x6, x7]
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
            c = [x1,x2,x3,x4,x7]
            r1 = [float(m.get('r1x1')),float(m.get('r1x2')),float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x7'))]
            r2 = [float(m.get('r2x1')),float(m.get('r2x2')),float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x7'))]
            r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
                  float(m.get('r3x4')), float(m.get('r3x7'))]

        # primeira iteracao
        cB = [0, 0, 0]

        b = [float(m.get('b1')), float(m.get('b2')),float(m.get('b3'))]

        A = [r1, r2, r3]

        cR = [0,0]

        z = simplex3_v2(m,c,b,cB,A,cR)
        if z==None:
            z = "não há solução"
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return render(request,'mysite/simplex.html',
                          {'z': z})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SimplexForm()

    return render(request, 'mysite/simplex.html', {'form': form})


def get_simplexduasfases(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SimplexForm(request.POST)
        # recebe todos os valores do form
        m = {}
        M=9999
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

        x1 = float(m.get('x1'))
        x2 = float(m.get('x2'))
        x3 = 0
        x4 = 0
        x5=M
        x6=M

        if m['rx3']=='>' and m['rx4']=='>':
            c=[x1,x2,0,0,0,0]
            cA = [0,0,0,0,1,1]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x5')),float(m.get('r1x6'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x5')),float(m.get('r2x6'))]

        elif m['rx3']=='>' and m['rx4']=='<':
            c=[x1,x2,0,0,0]
            cA = [0,0,0,0,1]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x5'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x5'))]
        elif m['rx3']=='<' and m['rx4']=='>':
            c=[x1,x2,0,0,0]
            cA = [0,0,0,0,1]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x6'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x6'))]
        else:
            c = [x1,x2,0,0]
            cA = [0,0,0,0]
            r1 = [float(m.get('r1x1')),float(m.get('r1x2')),float(m.get('r1x3')),
                  float(m.get('r1x4'))]
            r2 = [float(m.get('r2x1')),float(m.get('r2x2')),float(m.get('r2x3')),
                  float(m.get('r2x4'))]

        # primeira iteracao
        cB = [0, 0]

        cAB = [0,0]

        b = [float(m.get('b1')), float(m.get('b2'))]

        A = [r1, r2]

        cR = [0,0]

        cRA = [0,0]

        z = simplexduasfases_method(m,c,b,cB,A,cR,cA,cRA,cAB)

        if z==None:
            z = "não há solução"
        # check whether it's valid:
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        return render(request,'mysite/simplex.html',
                      {'z': z})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SimplexForm()

    return render(request, 'mysite/simplex.html', {'form': form})

def get_simplex3duasfases(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SimplexForm(request.POST)
        # recebe todos os valores do form
        m = {}
        M=9999
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


        x1 = float(m.get('x1'))
        x2 = float(m.get('x2'))
        x3 = 0
        x4 = 0
        x5=M
        x6=M
        x7 = 0
        x9 = M

        if m['rx3']=='>' and m['rx4']=='>' and m['rx7']=='>':
            c=[x1,x2,0,0,0,0,0,0]
            cA = [0,0,0,0,1,1,0,1]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x5')),float(m.get('r1x6')),
                  float(m.get('r1x7')), float(m.get('r1x9'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x5')),float(m.get('r2x6')),
                  float(m.get('r2x7')), float(m.get('r2x9'))]
            r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
                  float(m.get('r3x4')),float(m.get('r3x5')),float(m.get('r3x6')),
                  float(m.get('r3x7')), float(m.get('r3x9'))]


        elif m['rx3']=='>' and m['rx4']=='>' and m['rx7']=='<':
            c=[x1,x2,0,0,0,0,0]
            cA=[0,0,0,0,1,1,0]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x5')),float(m.get('r1x6')),
                  float(m.get('r1x7'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x5')),float(m.get('r2x6')),
                  float(m.get('r2x7'))]
            r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
                  float(m.get('r3x4')), float(m.get('r3x5')), float(m.get('r3x6')),
                  float(m.get('r3x7'))]

        elif m['rx3']=='>' and m['rx4']=='<' and m['rx7']=='>':
            c=[x1,x2,0,0,0,0,0]
            cA = [0,0,0,0,1,0,1]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x5')),
                  float(m.get('r1x7')), float(m.get('r1x9'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x5')),
                  float(m.get('r2x7')), float(m.get('r2x9'))]
            r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
                  float(m.get('r3x4')), float(m.get('r3x5')),
                  float(m.get('r3x7')), float(m.get('r3x9'))]

        elif m['rx3'] == '>' and m['rx4'] == '<' and m['rx7'] == '<':
            c = [x1, x2, 0, 0, 0,0]
            cA = [0,0,0,0,1,0]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')), float(m.get('r1x5')),
                  float(m.get('r1x7'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')), float(m.get('r2x5')),
                  float(m.get('r2x7'))]
            r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
                  float(m.get('r3x4')), float(m.get('r3x5')),
                  float(m.get('r3x7'))]

        elif m['rx3']=='<' and m['rx4']=='>' and m['rx7']=='>':
            c=[x1,x2,0,0,0,0,0]
            cA = [0,0,0,0,1,0,1]
            r1 = [float(m.get('r1x1')), float(m.get('r1x2')), float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x6')),
                  float(m.get('r1x7')), float(m.get('r1x9'))]
            r2 = [float(m.get('r2x1')), float(m.get('r2x2')), float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x6')),
                  float(m.get('r2x7')), float(m.get('r2x9'))]
            r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
                  float(m.get('r3x4')), float(m.get('r3x6')),
                  float(m.get('r3x7')), float(m.get('r3x9'))]
        elif m['rx3'] == '<' and m['rx4'] == '>' and m['rx7'] == '<':
            c = [x1, x2, 0, 0, 0, 0]
            cA = [0,0,0,0,1,0]
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
            c = [x1,x2,0,0,0]
            cA = [0,0,0,0,0]
            r1 = [float(m.get('r1x1')),float(m.get('r1x2')),float(m.get('r1x3')),
                  float(m.get('r1x4')),float(m.get('r1x7'))]
            r2 = [float(m.get('r2x1')),float(m.get('r2x2')),float(m.get('r2x3')),
                  float(m.get('r2x4')),float(m.get('r2x7'))]
            r3 = [float(m.get('r3x1')), float(m.get('r3x2')), float(m.get('r3x3')),
                  float(m.get('r3x4')), float(m.get('r3x7'))]

        # primeira iteracao
        cB = [0, 0, 0]

        b = [float(m.get('b1')), float(m.get('b2')),float(m.get('b3'))]

        A = [r1, r2, r3]

        cR = [0,0]
        cRA = [0,0]

        z = simplex3duasfases_method(m,c,b,cB,A,cR,cA,cRA,cAB)
        if z==None:
            z = "não há solução"
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return render(request,'mysite/simplex.html',
                          {'z': z})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SimplexForm()

    return render(request, 'mysite/simplex.html', {'form': form})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SimplexForm
from .method import simplex

# Create your views here.

def index(request):
    return render(request, 'mysite/index.html')


def thanks(request):
    return render(request, 'mysite/thanks.html')


def get_simplex(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SimplexForm(request.POST)
        # recebe todos os valores do form
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
                    m['x1'] = -float(form['x1'].value())
                    m['x2'] = -float(form['x2'].value())
                    cN = [m['x1'], m['x2']]
                else:
                    m['x1'] = float(form['x1'].value())
                    m['x2'] = float(form['x2'].value())
                    cN = [m['x1'], m['x2']]
            elif i == 'maiormenorR1':
                if form[i].value() == ">=":
                    m['r1x3'] = -1
                    m['r2x3'] = 0
                elif form[i].value() == "<=":
                    m['r1x3'] = 1
                    m['r2x3'] = 0
            elif i == 'maiormenorR2':
                if form[i].value() == ">=":
                    m['r1x4'] = 0
                    m['r2x4'] = -1
                elif form[i].value() == "<=":
                    m['r1x4'] = 0
                    m['r2x4'] = 1

        # primeira iteracao
        cB = [0, 0]

        N = [[float(m.get('r1x1')), float(m.get('r1x2'))],
             [float(m.get('r2x1')), float(m.get('r2x2'))]]
        B = [[float(m.get('r1x3')), float(m.get('r1x4'))],
             [float(m.get('r2x3')), float(m.get('r2x4'))]]
        b = [float(m.get('b1')), float(m.get('b2'))]
        para = 3
        xB = simplex(cN,cB,N,B,b)
        # check whether it's valid:
        z=sum(xB)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return render(request,'mysite/simplex.html',
                          {'context': xB,
                           'z':z})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SimplexForm()

    return render(request, 'mysite/simplex.html', {'form': form})

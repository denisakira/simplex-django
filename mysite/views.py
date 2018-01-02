# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import SimplexForm
from mysite.methods.simplex_method import simplex_v2,simplex3_v2
from mysite.methods.simplexduasfases_method import simplexduasfases_method, simplex3duasfases_method
from mysite.methods.gomory_method import gomory_method
from mysite.handlers.form_handler import get_formdata, get_formdata3
from mysite.handlers.data_handler import get_data, get_data3, get_data_duasfases, \
    get_data_duasfases3, get_datav2
import numpy as np
# Create your views here.

def index(request):
    return render(request, 'mysite/index.html')

def simplex3(request):
    return render(request, 'mysite/simplex3.html')

def simplexduasfases(request):
    return render(request, 'mysite/simplexduasfases.html')

def simplex3duasfases(request):
    return render(request, 'mysite/simplex3duasfases.html')

def gomory(request):
    return render(request, 'mysite/gomory.html')

def gomory3(request):
    return render(request, 'mysite/gomory3.html')

def get_simplex(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SimplexForm(request.POST)
        # recebe todos os valores do form
        m = get_formdata(form)
        Obj = get_datav2(m)

        c=np.array(Obj[0])
        A=np.array(Obj[1])

        # primeira iteracao
        cB = [0, 0]

        b = np.array([float(m.get('b1')), float(m.get('b2'))])

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
        m = get_formdata3(form)
        obj = get_data3(m)

        c = obj[0]
        A = np.array(obj[1])

        # primeira iteracao
        cB = [0, 0, 0]

        b = np.array([float(m.get('b1')), float(m.get('b2')),float(m.get('b3'))])

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
        m = get_formdata(form)
        obj = get_data_duasfases(m)

        c = np.array(obj[0])
        cA = np.array(obj[1])
        A = np.array(obj[2])

        # primeira iteracao
        cB = [0, 0]

        cAB = [0,0]

        b = np.array([float(m.get('b1')), float(m.get('b2'))])


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
        m = get_formdata3(form)
        obj = get_data_duasfases3(m)
        c = np.array(obj[0])
        cA = np.array(obj[1])
        A = np.array(obj[2])
        # primeira iteracao
        cB = [0, 0, 0]

        b = np.array([float(m.get('b1')), float(m.get('b2')),float(m.get('b3'))])

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

def get_gomory(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SimplexForm(request.POST)
        # recebe todos os valores do form
        m = get_formdata(form)
        obj = get_datav2(m)
        c = np.array(obj[0])
        A = np.array(obj[1])

        # primeira iteracao
        cB = np.array([0, 0])
        b = np.array([float(m.get('b1')), float(m.get('b2'))])
        cR = [0,0]
        z = gomory_method(m,c,b,cB,A,cR)
        if z==None:
            z = "não há solução"

        return render(request,'mysite/simplex.html',
                      {'z': z})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SimplexForm()

    return render(request, 'mysite/simplex.html', {'form': form})

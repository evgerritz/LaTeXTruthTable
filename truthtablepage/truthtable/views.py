from django.shortcuts import render
from src import *

def index(request):
    context = {}
    return render(request, 'truthtable/index.html', context)

def result(request):
    if request.method == 'POST':
        pf = request.POST.get('pf', None)
        result = main.maketable(pf)
        return render(request, 'truthtable/result.html', {'pf':pf, 'result':result})
    else:
        return render(request, 'truthtable/index.html')

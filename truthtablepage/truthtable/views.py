from django.shortcuts import render
import sympy
import shutil
from src import *

def index(request):
    context = {}
    return render(request, 'truthtable/index.html', context)

def result(request):
    if request.method == 'POST':
        pf = request.POST.get('pf', None)
        result_text = main.maketable(pf)
        img_path = 'temp.png'
        sympy.preview(result_text, viewer='file', filename=img_path, output='png')
        shutil.move(img_path, 'truthtable/static/images/' + img_path)
        return render(request, 'truthtable/result.html', {'pf':pf, 'result_text':result_text, 'img_path': img_path})
    else:
        return render(request, 'truthtable/index.html')

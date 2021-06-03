from django.shortcuts import render

def index(request):
    context = {'test_var': 'wowza'}
    return render(request, 'truthtable/index.html', context)

def user_input(request):
    context = {}
    try:
        context['raw_pf'] = request.POST['pf']
    except KeyError:
        return render(request, 'truthtable/index.html', {
            'error_message': "no pf entered",
        })
    else:
        return HttpResponseRedirect('/truthtable/result/')

def result(request, pf):
    result = 
    return render(request, 'polls/result.html', {'pf':pf, 'result':result})

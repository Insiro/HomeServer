from django.shortcuts import render
from epic7.models import tips, notic as notics
from django.forms.models import model_to_dict
from django.db.models import Q
# Create your views here.


def index(request):
    noticLit = notics.objects.filter(important=True)
    hintLit = tips.objects.filter(important=True)
    return render(request, 'e7index.html', {'notics': noticLit, 'hints': hintLit})


def tiplit(request):
    lit = tips.objects.all()
    hitlist = {'datas': lit,'table':'tips'}
    return render(request, 'e7list.html', hitlist)


def search(request):
    req = request.GET
    for r in req:
        r.replace('<', "&lt")
    print(req)
    datas = {'kq': None, 'notic': list(), 'tips': list()}
    if 'kq' in req:
        kq = req.get('kq')
        kq = kq.split(' ')
        searchC = Q(name=None)
        for k in kq:
            searchC = Q(name__icontains=k) | Q(writer__icontains=k) | searchC
        datas['kq'] = ' '.join(kq)
        datas['notic'] = notics.objects.all().filter(searchC)
        datas['tips'] = tips.objects.all().filter(searchC)
    return render(request, 'e7search.html', datas)


def notic(request):
    lit = notics.objects.all()
    hitlist = {'datas': lit,'table':'notic'}
    return render(request, 'e7list.html', hitlist)


def post(request):
    return render(request, 'e7post.html')


def detail(request):
    data = {'id': None, 'table': None, 'data': None}
    req = request.GET
    for r in req:
        r.replace('<', '&lt;').replace('>', '&rt;')
    data = {'id': None, 'table': None}
    if 'table' in req and 'id' in req:
        data['table'] = req.get("table")
        data['id'] = req.get("id")
    return render(request, 'e7detail.html', data)

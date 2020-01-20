from django.shortcuts import render
from home.models import projects, Kategorie, project_Img
import home.models as homeModel
from django.forms.models import model_to_dict
from django.db.models import Q

# Create your views here.


def index(request):
    lagList = homeModel.usableLanguages.objects.all()
    skillList = homeModel.skill.objects.all()
    return render(request, 'index.html', {"lang":lagList, "skills":skillList})


def search(request):
    req = request.GET
    data = {'projectlist': None, 'kq': None}
    for r in req:
        r.replace('<', "&lt")
    if 'kq'in req:
        kq = req.get('kq')
        kq = kq.split(' ')
        data['kq'] = ' '.join(kq)
        search_filter = Q(name=None)
        for k in kq:
            search_filter = Q(name__icontains=k) | search_filter
        data['projectlist'] = projects.objects.all().filter(search_filter)
    return render(request, 'search.html', data)


def blank(request):
    return render(request, 'about.html')


def info(request):
    return render(request, 'info.html')


def detail(request):
    getData = request.GET
    for r in getData:
        r.replace('<', "&lt")
    datas = {'id': 0, 'kate': None, 'Dat': None, 'img': None}
    if 'id'in getData:
        ID = getData.get('id')
        datas['id'] = ID
        datas['Dat'] = model_to_dict(projects.objects.get(id=int(ID)))
        datas['Dat']['context'] =(""+datas['Dat']['context']).replace("\r\n","</br>")
        kate = model_to_dict(Kategorie.objects.get(id=datas['Dat']['kate']))
        datas['kate'] = kate['name']
        datas['img'] = project_Img.objects.filter(projects_id=int(ID))
    return render(request, 'detail.html', datas)


def _404(request):
    return render(request, '404.html')


def elem(request):
    return render(request, 'elements.html')


def project(request):
    prolit = projects.objects.all()
    kate = Kategorie.objects.all()
    return render(request, 'project.html', {'projectlist': prolit, 'kate': kate})


def contact(request):
    return render(request, 'contact.html')


def blog(request):
    return render(request, 'blog.html')

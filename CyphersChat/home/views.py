from django.shortcuts import render
from home.models import projects, Kategorie,project_Img
from django.forms.models import model_to_dict

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    req = request.GET
    for r in req:
        r.replace('<',"&lt")
    if 'kq'in req:
        keyword = request.get('kq')
    return render(request, 'search.html')

def blank(request):
    return render(request, 'about.html')

def info(request):
    return render(request, 'info.html')

def detail(request):
    getData = request.GET
    for r in getData:
        r.replace('<',"&lt")
    datas = {'id':0,'kate':None,'Dat':None,'img':None}
    if 'id'in getData:
        ID = getData.get('id')
        datas['id'] = ID
        datas['Dat'] = model_to_dict(projects.objects.get(id = int(ID)))
        kate = model_to_dict(Kategorie.objects.get(id = datas['Dat']['kate']))
        datas['kate']=kate['name']
        datas['img'] = project_Img.objects.filter(projects_id=int(ID))
    return render(request, 'about.html',datas)

def _404(request):
    return render(request, '404.html')

def table(request):
    req = request.GET
    for r in req:
        r.replace('<',"&lt")
    table = req.get('table')
    return render(request, 'Tables.html',{'kq':table})

def project(request):
    prolit = projects.objects.all()
    kate = Kategorie.objects.all()
    return render(request, 'project.html',{'projectlist':prolit, 'kate':kate})

def contact(request):
    return render(request, 'contact.html')

def singleProject(request):
    return render(request, 'singleProject.html')
    
def blog(request):
    return render(request, 'blog.html')

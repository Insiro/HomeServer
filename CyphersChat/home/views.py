from django.shortcuts import render
from home.models import projects, Kategorie,project_Img

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    getData = request.GET
    return render(request, 'search.html',getData)

def blank(request):
    return render(request, 'about.html')

def info(request):
    return render(request, 'info.html')

def detail(request):
    getData = request.GET
    if 'id'in getData:
        pass;
    return render(request, 'about.html',getData)
    #if project_id!=None or project_id!=0:
        #img = project_Img.

def _404(request):
    return render(request, '404.html')

def table(request):
    table = request.GET.get('table')
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

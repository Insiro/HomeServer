from django.shortcuts import render
from home.models import projects, Kategorie,project_Img

# Create your views here.
def index(request):
    return render(request, 'index.html')
def search(request):
    kq = request.GET.get('kq')
    return render(request, 'search.html',{'kq':kq})
def blank(request):
    return render(request, 'about.html')
def detail(request):
    project_id = request.GET('id')
    #if project_id!=None or project_id!=0:
        #img = project_Img.
    return render(request, 'about.html')
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

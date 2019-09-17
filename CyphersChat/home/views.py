from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')
def search(request):
    kq = request.GET.get('kq')
    return render(request, 'search.html',{'kq':kq})
def blank(request):
    return render(request, 'about.html')
def detail(request):
    return render(request, 'about.html')
def _404(request):
    return render(request, '404.html')
def table(request):
    table = request.GET.get('table')
    return render(request, 'Tables.html',{'kq':table})
def project(request):
    return render(request, 'project.html')
def contact(request):
    return render(request, 'contact.html')
def singleProject(request):
    return render(request, 'singleProject.html')
def blog(request):
    return render(request, 'blog.html')

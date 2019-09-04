from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')
def search(request):
    kq = request.GET.get('kq')
    return render(request, 'search.html',{'kq':kq})
def blank(request):
    return render(request, 'blank.html')
def detail(request):
    return render(request, 'detail.html')
def _404(request):
    return render(request, '404.html')
def table(request):
    table = request.GET.get('table')
    return render(request, 'Tables.html',{'kq':table})
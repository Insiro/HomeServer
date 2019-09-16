from django.shortcuts import render
from epic7.models import tips, notic
# Create your views here.
def index(request):
    lit = notic.objects.all()
    imporlit = tips.objects.filter(important = True)
    return  render(request, 'e7index.html', {'notic':lit, 'hints':imporlit})
def tiplit(request):
    lit = tips.objects.all()
    hitlist = {'hintlist':lit}
    return render(request, 'e7tips.html', hitlist)
def search(request):
    kq = request.GET.get('kq')
    return render(request, 'e7search.html',{'kq':kq})
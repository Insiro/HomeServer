from django.shortcuts import render
import epic7.models as e7Models
# Create your views here.
def index(request):
    noticLit = e7Models.notic.objects.filter(important = True)
    hintLit = e7Models.tips.objects.filter(important = True)
    return  render(request, 'e7index.html', {'notics':noticLit, 'hints':hintLit})
def tiplit(request):
    lit = e7Models.tips.objects.all()
    hitlist = {'hintlist':lit}
    return render(request, 'e7tips.html', hitlist)
def search(request):
    kq = request.GET.get('kq')
    return render(request, 'e7search.html',{'kq':kq})
def notic(request):
    lit = e7Models.notic.objects.all()
    hitlist = {'hintlist':lit}
    return render(request, 'e7notic.html',hitlist)
def post(request):
    return render(request, 'post.html')
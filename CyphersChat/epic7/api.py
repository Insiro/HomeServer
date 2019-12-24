from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import epic7.models as e7Models
from django.forms.models import model_to_dict


def info(request):
    req = request.GET
    for r in req:
        r.replace('<', "&lt")
    table = req.get("table")
    id = req.get("id")
    if(table == 'notic'):
        data = e7Models.notic.objects.get(id=int(id))
    elif(table == 'tips'):
        data = e7Models.tips.objects.get(id=int(id))
    else:
        data = get_object_or_404(e7Models.tips , pk=0)
    return JsonResponse(model_to_dict(data), json_dumps_params={'ensure_ascii': False})

def allRank(requests):
    url = "https://api.epicsevendb.com/api/hero/"
    req = requests.GET
    Cname = req.get('Cname')
    url = url + Cname
    data = {'s':0}
    return JsonResponse({"data": data}, json_dumps_params={'ensure_ascii': False})

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import epic7.models as e7Models
from django.forms.models import model_to_dict
def info(request):
    req = request.GET
    table = req.get("table")
    id = req.get("id")
    if(table == 'notic'):
        data = e7Models.notic.objects.get(id = int(id))
    elif(table == 'tips'):
        data = e7Models.tips.objects.get(id = int(id))
    else:
       data = get_object_or_404()
    return JsonResponse(model_to_dict(data),  json_dumps_params={'ensure_ascii': False})

# def allRank(requests):
#     requests.GET.get("")
#     count = 10
#     start = 0
#     global apiUrl
#     global apikey
#     Url = apiUrl+"ranking/ratingpoint?offset=" + \
#         str(start) + '&limit=' + str(count)+apikey
#     req = reqs.get(Url)
#     if req.status_code != 200 and req.status_code != 201:
#         print('Not respone ' + str(req.status_code))
#         return JsonResponse({'data': None})
#     dat = req.json()['rows']
#     data = list()
#     for dats in dat:
#         data.append({'nick': dats['nickname'], 'rank': dats['rank'],
#                      'RP': dats['ratingPoint'], 'grade': dats['grade']})
#     return JsonResponse({"data": data},  json_dumps_params={'ensure_ascii': False})
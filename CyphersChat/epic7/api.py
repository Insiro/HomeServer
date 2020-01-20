from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import epic7.models as e7Models
from django.forms.models import model_to_dict
from django.core import serializers
from django.contrib.auth.hashers import make_password


def info(request):
    req = request.GET
    for r in req:
        r.replace('<', "&lt")
    table = req.get("table")
    id = req.get("id")
    if(table == 'notic'):
        data =  e7Models.notic.objects.get(id=int(id))
        data = model_to_dict(data)
        print(data)
    elif(table == 'tips'):
        data = model_to_dict(e7Models.tips.objects.get(id=int(id)))
        print(data)
        data['image'] = str(data['image'])
        # dataDic["img"] = str(list(model_to_dict(i)for i in img_))
    else:
        data = get_object_or_404(e7Models.tips, pk=0)
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def allRank(requests):
    url = "https://api.epicsevendb.com/api/hero/"
    req = requests.GET
    Cname = req.get('Cname')
    url = url + Cname
    data = {'s': 0}
    return JsonResponse({"data": data}, json_dumps_params={'ensure_ascii': False})


def authorize(request):
    if request.method == 'POST':
        uid = request.POST['id']
        upw = request.POST['pw']
        us = get_object_or_404(e7Models.user, UID=uid, UPW=make_password(upw))
        request.session['isSigned'] = True
        request.session['uid'] = uid
        request.session['name'] = us.name
        return JsonResponse({"result": "success"})
    return JsonResponse({"result": "fail"})

def isAuthrized(request):
    if request.session.get('isSigned'):
        return JsonResponse({"result":True})
    return JsonResponse({"result":False})




def changePWD(request):
    if request.method == 'POST':
        UID = request.POST['id']
        UPW = make_password(request.POST['pw'])
        NEW = request.POST['newUPW']
        get_object_or_404(e7Models.user, UID=UID, UPW=make_password(
            UPW)).update(UPW=make_password(NEW))
        return JsonResponse({"result": "success"})
    return JsonResponse({"result": "fail"})


def register(request):
    if request.method == 'POST':
        if not(UID and UPW and name):
            return JsonResponse({"result": "fail"})
        e7Models.user(
            UID=request.POST['id'],
            UPW=make_password(request.POST['pw']),
            name=request.POST['name'],
            Signed=False).save()
    return JsonResponse({"result": "success"})

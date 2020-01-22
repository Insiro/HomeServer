from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import epic7.models as e7Models
from django.forms.models import model_to_dict
from django.core import serializers
from django.contrib.auth.hashers import make_password


def getNotic(request):
    data = model_to_dict(e7Models.notic.objects.get(id=1))
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def getReisterNotic(request):
    data = model_to_dict(e7Models.notic.objects.get(id=3))
    data['contents']
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def getTip(request):
    data = list()
    for item in e7Models.tips.objects.all():
        data.append({"name": item.name, "writer": item.writer, "_id": item.id})
    return JsonResponse({"data": data}, json_dumps_params={'ensure_ascii': False})


def getBotSkills(request):
    data = list()

    for item in e7Models.BotSkills.objects.all():
        data.append({"skill": item.Skill, "target": item.target})
    return JsonResponse({"data": data}, json_dumps_params={'ensure_ascii': False})

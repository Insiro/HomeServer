from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import requests as reqs
import json
from bs4 import BeautifulSoup
# Create your views here.

hostname = 'http://cyphers.nexon.com'
apikey = '&apikey=UrGRg0ai58uj7J1GYFjy1ZfU9kzxBHY5'
apiUrl = 'https://api.neople.co.kr/cy/'
status = 0
season = 15
charactor = {'로라스': 'loras', '휴톤': 'huton', '루이스': 'louis', '타라': 'tara', '트리비아': 'trivia', '카인': 'cain',
             '레나': 'rena', '드렉슬러': 'drexler', '도일': 'doyle', '토마스': 'thomas', '나이오비': 'niobe', '시바포': 'shiva',
             '시바': 'shiva', '시바 포': 'shiva', '웨슬리': 'wesley', '스텔라': 'stella', '엘리셔': 'alicia', '클레어': 'clare',
             '다이무스': 'deimus', '이글': 'eagle', '미를렌': 'marlene', '샬럿': 'charlotte', '윌라드': 'willard', '레이튼': 'lleyton',
             '미쉘': 'michelle', '린': 'rin', '빅터': 'viktor', '카를로스': 'carlos', '호타루': 'hotaru', '트릭시': 'trixie',
             '히카로드': 'ricardo', '까미유': 'camille', '자네트': 'jannette', '피터': 'peter', '아이작': 'issac', '레베카': 'rebecca',
             '엘리': 'ellie', '마틴': 'martin', '브로스': 'bruce', '미아': 'mia', '드니스': 'denise', '제레온': 'gereon', '루시': 'lucy',
             '티엔': 'tian', '하랑': 'harang', 'J': 'j', 'j': 'j', '제이': 'j', '벨져': 'belzer', '리첼': 'richel', '리사': 'risa',
             '릭': 'rick', '제키엘': 'jekiel', '탄야': 'tanya', '캐럴': 'carol', '라이샌더': 'lysander', '루드빅': 'ludwig',
             '멜빈': 'melvin', '디아나': 'diana', '클리브': 'clive', '헬레나': 'helena', '에바': 'eva', '론': 'ron', '레오노르': 'leonor',
             '시드니': 'sidney'
             }


def api(requests):
    return JsonResponse({"list": ['UserID', 'charRank', 'todayCyphers', 'UserInfo', 'allRanking', 'rating (rating, normal, all)']})


def getUserID(requests, name):
    data = getuser_id(name)
    return JsonResponse({'data': data})


def getuser_id(name):
    global apiUrl
    global apikey
    Url = apiUrl + 'players?nickname='+name+apikey
    req = reqs.get(Url)
    if req.status_code != 200 and req.status_code != 201:
        print('Not respone ' + str(req.status_code))
        return None
    data = req.json()['rows']
    if len(data) == 0:
        return None
    return data[0]["playerId"]


def charRank(requests, charname):
    if charname not in charactor.keys():
        return None
    Url = 'http://cyphers.nexon.com/cyphers/article/ranking/charac/'+str(season)+'/' + \
        charactor.get(charname) + '/win/day/1'

    req = reqs.get(Url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    tags = '#rankCharacForm > div.rank_board.mar_b10 > table > tbody > tr'
    data = list()
    for tag in soup.select(tags):
        td = tag.select('tr > td')
        his = td[4].text.split('전')[1][1:].split('승')
        history = [his[0], his[1][1:-1]]
        data.append({'rank':   ''.join(filter(str.isdigit, td[0].text.replace(td[0].span.text, ''))), 'nick': td[1].text,
                     'level': td[2].text[:-1], 'record': history})
    print(data)
    return JsonResponse({"data": data},   json_dumps_params={'ensure_ascii': False})


def todayCyphers(requests):
    global hostname
    html = reqs.get('http://cyphers.nexon.com/cyphers/article/today2/1').text
    soup = BeautifulSoup(html, 'html.parser')
    today = soup.find('div', class_='today_box')
    data = list()
    for lit in today.select('ul > li'):
        p = lit.select('li > p')
        data.append({'title': p[0].a.text, 'link': hostname +
                     p[0].a['href'], 'writer': p[1].text[1:-1]})
    return JsonResponse({"data": data},  json_dumps_params={'ensure_ascii': False})


def getUserInfo(requests, name):
    global apiUrl
    global apikey
    ID = getuser_id(name)
    if ID == None:
        return JsonResponse({'data': None})
    Url = apiUrl + 'players/'+ID+'?'+apikey
    req = reqs.get(Url)
    if req.status_code != 200 and req.status_code != 201:
        print('Not respone ' + str(req.status_code))
        return JsonResponse({'data': None})
    dat = req.json()
    if len(dat) == 0:
        print('No data')
        return JsonResponse({'data': None})
    data = {'name':name, 'clan':dat['clanName'], 'RP':dat['ratingPoint'], 'tier':dat['tierName'], 'record':dat['records']}
    return JsonResponse({"data": data},  json_dumps_params={'ensure_ascii': False})


def allRanking(requests, args):

    ar = args.split('&')
    if len(ar) == 1:
        if ar[0][:6] == 'count=' and ar[0][6:].isdigit():
            count = int(ar[0][6:])
            start = 0
        elif ar[0][:6] == 'start='and ar[0][6:].isdigit():
            start = int(ar[0][6:])-1
            count = 10
        else:
            print('input error', ar[0])
            return JsonResponse({"data": None})
    elif len(ar) == 2:
        if ar[0][:6] == 'count=' and ar[1][:6] == 'start=' and ar[0][6:].isdigit() and ar[1][6:].isdigit():
            count = int(ar[0][6:])
            start = int(ar[1][6:])-1
        elif ar[1][:6] == 'count=' and ar[0][:6] == 'start=' and ar[0][6:].isdigit() and ar[1][6:].isdigit():
            count = int(ar[1][6:])
            start = int(ar[0][6:])-1
        else:
            print('input error', ar[0], ar[1])
            return JsonResponse({"data": None})
    else:
        return JsonResponse({"data": None})
    global apiUrl
    global apikey
    start = start if start < 1000 else 999
    count = count if count < 1000 else 1000
    count = count if start+count < 1000 else 1000-start
    Url = apiUrl+"ranking/ratingpoint?offset=" + \
        str(start) + '&limit=' + str(count)+apikey
    req = reqs.get(Url)
    if req.status_code != 200 and req.status_code != 201:
        print('Not respone ' + str(req.status_code))
        return JsonResponse({'data': None})
    dat = req.json()['rows']
    data = list()
    for dats in dat:
        data.append({'nick': dats['nickname'], 'rank': dats['rank'],
                     'RP': dats['ratingPoint'], 'grade': dats['grade']})
    return JsonResponse({"data": data},  json_dumps_params={'ensure_ascii': False})


def allRank(requests):
    count = 10
    start = 0
    global apiUrl
    global apikey
    Url = apiUrl+"ranking/ratingpoint?offset=" + \
        str(start) + '&limit=' + str(count)+apikey
    req = reqs.get(Url)
    if req.status_code != 200 and req.status_code != 201:
        print('Not respone ' + str(req.status_code))
        return JsonResponse({'data': None})
    dat = req.json()['rows']
    data = list()
    for dats in dat:
        data.append({'nick': dats['nickname'], 'rank': dats['rank'],
                     'RP': dats['ratingPoint'], 'grade': dats['grade']})
    return JsonResponse({"data": data},  json_dumps_params={'ensure_ascii': False})

def rating(requests, args):
    arg = args.split('&')
    if len(arg) == 1:
        if args[:5] != 'name=':
            print('input error', args)
            return JsonResponse({"data": None})
        name = args[5:]
        types = 0
    elif len(arg) == 2:
        if arg[0][:5] == 'name=' and arg[1][:5] == 'type='and arg[1][5:].isdigit():
            name = arg[0][5:]
            types = int(arg[1][5:])
        elif arg[0][:5] == 'type=' and arg[1][:5] == 'name=' and arg[0][5:].isdigit():
            name = arg[1][1]
            types = int(arg[0][5:])
            if types != 0 or types != 1:
                types = 0
        else:
            return JsonResponse({"data": None})
    else:
        return JsonResponse({"data": None})
    Type = ['rating', 'normal']
    global apiUrl
    global apikey
    ID = getuser_id(name)
    if ID == None:
        return None
    Url = apiUrl+'players/'+ID+'/matches?gameTypeId='+Type[int(types)]+apikey
    req = reqs.get(Url)
    if req.status_code != 200 and req.status_code != 201:
        print('Not respone ' + str(req.status_code))
        return JsonResponse({'data': None})
    dat = req.json()
    if 'matches' not in dat.keys():
        return JsonResponse({'data': None})
    data = {'grade': dat['grade'], 'clan': dat['clanName'], 'RP': dat['ratingPoint'],
            'tier': dat['tierName'], 'records': dat['records'], 'matches': None}
    mats = list()
    for mat in dat['matches']['rows']:
        PI = mat['playInfo']
        mats.append({'date': mat['date'], 'result': PI['result'], 'party': PI['partyUserCount'],
                     'char': PI['characterName'], 'level': PI['level'], 'kill': PI['killCount'], 'death': PI['deathCount'], 'assist': PI['assistCount'], 'attack': PI['attackPoint'], 'damage': PI['damagePoint'], 'playTime': PI['playTime']})
    data['matches'] = mats
    return JsonResponse({"data": data},  json_dumps_params={'ensure_ascii': False})

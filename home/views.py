from django.shortcuts import render, HttpResponse
from pprint import pprint
import random

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return HttpResponse('Welcoome to Django !')
    
# def dinner(request):
#     dinner = ['치킨', '짜장면', '등심', '갈비살']
#     return HttpResponse(f'오늘의 저녁은? {random.choice(dinner)}')

def dinner(request):
    menus = ['치킨', '짜장면', '등심', '갈비살']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'menus': menus, 'pick': pick})
from django.shortcuts import render
import datetime, os, requests

nowday=datetime.date.today()
byeday=datetime.date(2019, 2, 28)
graduationday=datetime.date(2019, 5, 28)

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    key = "키는 숨긴다."
    url = "https://api.openweathermap.org/data/2.5/weather?q=Daejeon,kr&lang=kr&APPID=" + key
    req = requests.get(url).json()
    temp_min = int(req["main"]["temp_min"]) - 273
    temp_max = int(req["main"]["temp_max"]) - 273
    temp_des = req["weather"][0]["description"]
    return render(request, 'utilities/today.html', {"min":temp_min, "max": temp_max, "des": temp_des})
    
def bye(request):
    delta = byeday - nowday
    return render(request, 'utilities/bye.html', {"delta": delta.days})
    
def graduation(request):
    delta = graduationday - nowday
    return render(request, 'utilities/graduation.html', {"delta": delta.days})
    
def ascii_make(request):
    ascii_original = request.GET.get("ascii_original")
    font_value = request.GET.get("select_box")
    url = f"http://artii.herokuapp.com/make?text={ascii_original}&font={font_value}"
    req = requests.get(url).text
    return render(request, 'utilities/ascii_make.html', {"req": req})

def ascii_new(request):
    return render(request, 'utilities/ascii_new.html')
    
    
def original(request):
    return render(request, 'utilities/original.html')

def translated(request):
    naver_client_id = os.getenv("NAVER_CLIENT_ID")
    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")
    
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    # 네이버에 Post 요청을 위해서 필요한 내용들
    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }
    data = {
        "source": "ko",
        "target": "en",
        "text": request.GET.get("original_text")
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    print(papago_response)
    reply_text = papago_response["message"]["result"]["translatedText"]
    return render(request, 'utilities/translated.html', {"reply_text": reply_text})
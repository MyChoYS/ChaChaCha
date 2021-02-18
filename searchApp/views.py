from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from searchApp.models import Academy, Academy_town, TestSite
from bbsApp.models import Academy_review

# 학원 검색
def services1(request) : #학원검색 첫 화면
        sidos = Academy.objects.all()
        context = {"sidos": sidos,'method':'get'}
        return render(request, 'services1.html', context)

def services1_city(request,city) : #지역 입력, Academy_town 테이블 참조 주의!!
        sidos = Academy_town.objects.all()
        dosi = city
        context = {"sidos": sidos, 'method': 'get','dosi':dosi}
        return render(request, 'services1_city.html', context)

def services1_town(request,city,town) : #지역입력, 시/구
        sidos = Academy.objects.all()
        dosi = city
        gugun = town
        context = {"sidos": sidos,'method':'get','dosi':dosi,'gugun':town}
        return render(request, 'services1_town.html', context)

def services1_name(request,city,town,name) : #지역,시/구,학원명입력
        sidos = Academy.objects.all()
        dosi = city
        gugun = town
        academy = name
        context = {"sidos": sidos,'method':'get','dosi':dosi,'gugun':town,'academy':name}
        return render(request, 'services1_name.html', context)

def services1_search(request,city,town,name): #학원내용 출력
    sidos = Academy.objects.all() #get post?
    dosi = city
    gugun = town
    academy = name
    context = {"sidos": sidos, 'method': 'get', 'dosi': dosi, 'gugun': town,'academy':name}
    return render(request, 'services1_search.html', context)


# 내 주변 학원 검색 (맵)
def services2(request) :
    mylocation = Academy.objects.all()
    academyReview = Academy_review.objects.all()
    context = {
        'Academy':mylocation,
        "academyReview": academyReview,
    }
    return render(request, 'services2.html', context)


# 내 주변 시험장 검색 (맵)
def services3(request) :
    mylocation = TestSite.objects.all()
    context = {
        'TestSite':mylocation,
    }
    return render(request, 'services3.html', context)

    ## thisUserMoments = mymoment.objects.filter(user=randomuserid, score__gte=4).order_by('-momentcreatedate', '-score')[0:4]
# 지도 테스트 나중에 지우기

def tt(request):
    mylocation = Academy.objects.all()
    context = {
        'Academy': mylocation,
    }
    return render(request, 'tt.html', context)


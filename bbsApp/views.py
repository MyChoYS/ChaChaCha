from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Academy_review, TestSite_review
from .models import Academy, TestSite
from searchApp.models import Academy_town
from django.http import  JsonResponse

from django.http import HttpResponse
from django.template import loader

# 학원 리뷰 보기
def review_academy(request):
    page = request.GET.get('page', 1)

    academyReview = Academy_review.objects.all()
    reviewPaginator = Paginator(academyReview, 5)
    reviewlistpage = reviewPaginator.get_page(page)

    context = {"academyReview": reviewlistpage}
    return render(request, 'review_academy.html', context)

# 시험장 리뷰 보기
def review_testsite(request):
    page = request.GET.get('page', 1)

    testsiteReview = TestSite_review.objects.all()
    reviewPaginator = Paginator(testsiteReview, 5)
    reviewlistpage = reviewPaginator.get_page(page)

    context = {"testsiteReview": reviewlistpage}
    return render(request, 'review_testsite.html', context)

def read_academy(request):
    pk = request.GET['pk']
    review = Academy_review.objects.get(pk=pk)
    context = {"review": review}
    return render(request, 'read_academy.html', context)

def read_testsite(request):
    pk = request.GET['pk']
    review = TestSite_review.objects.get(pk=pk)
    context = {"review": review}
    return render(request, 'read_testsite.html', context)

# 학원 리뷰 수정
def update_academy(request, id=0):
    if request.method == "GET":
        pk = request.GET['pk']
        review = Academy_review.objects.get(pk=pk)
        context = {"review": review}
        return render(request, 'update_academy.html', context)
    else:
        review = Academy_review.objects.get(pk=id)
        if review.password != request.POST['password']:
            context = {"review": review, "msg": "비밀번호가 틀렸습니다"}
            return render(request, 'update_academy.html', context)
        review.title = request.POST['title']
        review.content = request.POST['content']
        academy_name = request.POST['a_name']
        academy_id = Academy.objects.get(name=academy_name)
        review.academy_id = academy_id
        review.save()
        return redirect("review_academy")

# 시험장 리뷰 수정
def update_testsite(request, id=0):
    if request.method == "GET":
        pk = request.GET['pk']
        review = TestSite_review.objects.get(pk=pk)
        context = {"review": review}
        return render(request, 'update_testsite.html', context)
    else:
        review = TestSite_review.objects.get(pk=id)
        if review.password != request.POST['password']:
            context = {"review": review, "msg": "비밀번호가 틀렸습니다"}
            return render(request, 'update_testsite.html', context)
        review.title = request.POST['title']
        review.content = request.POST['content']
        testsite_name = request.POST['t_name']
        testsite_id = TestSite.objects.get(name=testsite_name)
        review.testsite_id = testsite_id
        review.save()
        return redirect("review_testsite")

# 학원 리뷰 삭제
def delete_academy(request):
    pk = request.GET['pk']

    delete_object = Academy_review.objects.get(pk=pk)
    delete_object.delete()
    return redirect("review_academy")

# 시험장 리뷰 삭제
def delete_testsite(request):
    pk = request.GET['pk']

    delete_object = TestSite_review.objects.get(pk=pk)
    delete_object.delete()
    return redirect("review_testsite")

# 학원 리뷰 작성
def create_academy(request):
    if request.method == "POST":
        title = request.POST['title']
        password = request.POST['password']
        content = request.POST['content']
        academy_name = request.POST['a_name']
        academy_id = Academy.objects.get(name=academy_name)
        data = Academy_review(title=title, password=password, content=content, academy_id=academy_id)
        data.save()

        return redirect("review_academy")
    else:
        context = {"flag":1}
        return render(request, 'create_academy.html', context)

# 시험장 리뷰 작성
def create_testsite(request):
    if request.method == "POST":
        title = request.POST['title']
        password = request.POST['password']
        content = request.POST['content']
        testsite_name = request.POST['t_name']
        testsite_id = TestSite.objects.get(name=testsite_name)
        data = TestSite_review(title=title, password=password, content=content, testsite_id=testsite_id)
        data.save()
        return redirect("review_testsite")

    else:
        context = {"flag": 1}
        return render(request, 'create_testsite.html', context)

# 학원 시군구
def get_academy_town(request):
    value = request.GET['value']
    academy = Academy_town.objects.all()
    townList = []
    for a in academy:
        if a.town_name==value:
            townList.append(a.city_name)

    return JsonResponse({"townList": townList})

# 학원 이름
def get_academy_name(request):
    value = request.GET['value']
    academy = Academy.objects.all()
    nameList = []
    for a in academy:
        if a.address_town==value:
            nameList.append(a.name)
    return JsonResponse({"nameList": nameList})

# 시험장 이름
def get_testsite_name(request):
    testsite = TestSite.objects.all()
    nameList = []
    for t in testsite:
        nameList.append(t.name)
    return JsonResponse({"nameList": nameList})

def get_academy_password(request):
    pk = request.GET['pk']
    review = Academy_review.objects.get(pk=pk)
    return JsonResponse({"result": review.password})

def get_testsite_password(request):
    pk = request.GET['pk']
    review = TestSite_review.objects.get(pk=pk)
    return JsonResponse({"result": review.password})

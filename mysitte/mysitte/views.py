# i have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse("girija bansal")
    #  return render(request,'index.html')
    params = {'name':'girija','place':'india'}
    return render(request, 'index.html',params)
def index1(request):
    return HttpResponse('''<a href="https://www.facebook.com/">facebook</a>''')
def removepunc(request):
    return HttpResponse("removepunc")
def capfirst(request):
    return HttpResponse("capitalfirst")
def newlineremove(request):
    return HttpResponse("newlineremove")
def spaceremove(request):
    return HttpResponse("spaceremove")
def charcount(request):
    return HttpResponse("<a href='http://127.0.0.1:8000/spaceremove/'>go to that page</a>")
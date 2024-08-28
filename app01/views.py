from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('欢迎kant使用django')

def index2(request):
    #render会展示html内容
    return render(request,'test.html')

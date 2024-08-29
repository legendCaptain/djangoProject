from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('欢迎kant使用django')

def index2(request):
    #render会展示html内容
    return render(request,'test.html')

def test_base(request):
    context = {
        'title': 'My Custom Title',
        'header': 'Welcome to My Website',
        'content': 'This is my custom content'
    }
    return render(request, 'base.html', context)
"""
def test_base(request):#也可以这么写
    return render(request, 'base.html', {
        'title': 'My Custom Title',
        'header': 'Welcome to My Website',
        'content': 'This is my custom content'
    })
"""
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'articles/index.html')


def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    nickname = request.GET.get('nickname')
    context = {
        'nickname' : nickname
    }
    return render(request, 'articles/catch.html', context)
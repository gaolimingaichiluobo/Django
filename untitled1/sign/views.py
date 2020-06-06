from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello Django!")


# 登录请求
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            # HttpResponseRedirect:类似于在url中重新访问这个页面
            return HttpResponseRedirect('/event_manage/')
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})


# 签到页面处理
def event_manage(request):
    return render(request, 'event_manage.html')

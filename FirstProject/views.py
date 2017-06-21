from django.shortcuts import render
from eee import  models
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.http import HttpResponse
def LOGIN(request):
    return render(request,'background.html')
def home(request):
    personlist = models.Information.objects.filter()
    return render(request,'home.html', {'personlist': personlist})
def add(request):
        admin = request.GET['a']
        password = request.GET['b']
        admin = str(admin)
        password = str(password)
        list = models.Admincheck.objects.filter()
        for i in list:
            d = str(i.admin)
            e = str(i.password)
            if admin == d:
                if password == e:
                     #return HttpResponse(u"信息分析团队欢迎你")
                    personlist = models.Information.objects.filter()
                    #response = HttpResponseRedirect('')
                    response= render(request, 'home.html', {'personlist': personlist})
                    response.set_cookie('admin', admin, 3600)
                    return response
                    #return render(request, 'home.html', {'personlist': personlist})
                else:
                    return HttpResponse(u"密码错误 ：（")
            else:
                continue
        return HttpResponse(u"用户名不存在 ：（")
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient


from endapp.models import TUser, Xinxibiao1, Qinxi
from endapp.send_mail import sendmail
import random,string
# Create your views here.
def login(request):
    return render(request,'login.html')
def main(request):

    return render(request,'main.html')
def introduce(request):
    return render(request,'introduce.html')
def menu(request):
    num = request.GET.get("num")
    # l = []
    infos = Qinxi.objects.all()
    print(infos)
    # for i in infos:
    #     # print(i, 44)
    #     l.append(i)
    pagtor = Paginator(infos, per_page=4)
    pcount = pagtor.num_pages  # 这是要传给前端的总页数
    print(pcount, 149)
    count = pagtor.count
    print(count, 88)
    if not num:
        num = 1
        page = pagtor.page(num)
        print(page, 151)
        return render(request, 'menu.html', {"page": page,"num":num, "pcount": pcount, "count": count})
    else:
        page = pagtor.page(1)
        print(page, 151)
        return render(request, 'menu.html',
                      {"page": page, "pcount": pcount, "count": count,"num":num})  # 有传过来页码


    # return render(request,'menu.html')
def query(request):
    def mydefault(u):
        if isinstance(u,Qinxi):
            return {"id":u.id,"name":u.name,'sex':u.sex,'hunfou':u.hunfou,'age':str(u.age),"birthday":u.birthday,'education':u.education,'guojia':u.guojia,"politics":u.politics,'jobjiny':u.jobjiny,'current_address':u.current_address,"phone":u.phone,'email':u.email,'job_wanted':u.job_wanted,"jobsite":u.jobsite,'expect_job':u.expect_job,'job_nature':u.job_nature,"expect_vocation":u.expect_vocation,'salary':u.salary,'education_experience':u.education_experience,'school':u.school,'specialty':u.specialty}

    e = Qinxi.objects.all()
    # print(e)
    number = request.GET.get('number')
    if not number:
        number = 1
    pagtor = Paginator(e, per_page=10)
    page = pagtor.page(number)
    pcount = pagtor.num_pages  # 这是要传给前端的总页数
    print(pcount, 149)
    count = pagtor.count
    # psum = pagtor.num_pages
    # ye = page.paginator.page_range
    # print(ye,'203')
    return JsonResponse({"use":list(page)},json_dumps_params={"default":mydefault})


def query1(request):
    querya=request.GET.get('query')
    print(querya,'211')
    def mydefault(u):
        if isinstance(u,Qinxi):
            return {"id":u.id,"name":u.name,'sex':u.sex,'hunfou':u.hunfou,'age':str(u.age),"birthday":u.birthday,'education':u.education,'guojia':u.guojia,"politics":u.politics,'jobjiny':u.jobjiny,'current_address':u.current_address,"phone":u.phone,'email':u.email,'job_wanted':u.job_wanted,"jobsite":u.jobsite,'expect_job':u.expect_job,'job_nature':u.job_nature,"expect_vocation":u.expect_vocation,'salary':u.salary,'education_experience':u.education_experience,'school':u.school,'specialty':u.specialty}


    e = Qinxi.objects.filter(expect_job__contains=querya)
    print(e,'217')
    number = request.GET.get('number')
    if not number:
        number = 1
    pagtor = Paginator(e, per_page=10)

    # page = pagtor.page(2)
    page = pagtor.page(number)
    pcount = pagtor.num_pages  # 这是要传给前端的总页数
    print(pcount, 149)
    count = pagtor.count
    # psum = pagtor.num_pages
    return JsonResponse({"use":list(page)},json_dumps_params={"default":mydefault})


def register(request):
    return render(request,'register.html')
def register1(request):
    email1 = request.POST.get('email')
    username = request.POST.get('txt_username')
    txt_mobile = request.POST.get('txt_mobile')
    print(txt_mobile)
    pasword = request.POST.get('txt_repassword')
    fs = TUser.objects.filter(email=email1)
    youxian = request.session.get('mobile')
    print(youxian,pasword,username)
    if fs:
        return HttpResponse('注册失败邮箱已存在！')
    if txt_mobile==youxian:
        TUser.objects.create(email=email1, nickname=username, password=pasword, aass='1')
    print(email1,username,pasword)
    return redirect('endapp:login')
def login1(request):
    username = request.POST.get('userid')
    pasword = request.POST.get('password')
    phone = request.POST.get('phone')
    phone1 = request.session.get('phone')
    print(username,pasword)
    print(phone)
    try:
        if phone1==phone:
            fs = TUser.objects.get(nickname=username,password=pasword,aass='1')
    except:
        return HttpResponse('登录失败！页面上火星了还没回来')
         # return redirect('endapp:login')
    if fs:
        return redirect('endapp:main')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def mail(request):
    print(123)
    a=request.GET.get('id')
    request.session['email1'] = a
    print(a,'123')
    # a1='17319366584@sina.cn'
    if a:
        ma=id_generator()
        request.session['mobile']=ma
        c=sendmail(ma,a)
        print('11')
    return HttpResponse(123)
def phone(request):
    a=request.GET.get('id')
    print(a)
    ma = id_generator()
    request.session['phone'] = ma


    clnt = YunpianClient('1f72317602ff1631e5b889358d107603')
    param = {YC.MOBILE: ''+str(a)+'', YC.TEXT: '您的验证码是'+ma+''}
    r = clnt.sms().single_send(param)

    return HttpResponse(123)

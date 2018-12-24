from django.shortcuts import render, redirect
# from . import models
from blog import models
from .forms import UserForm, RegisterForm


def index(request):
    pass
    return render(request, 'index.html')


def login(request):
    if request.session.get('is_login', None):           # 不允许重复登录
        return redirect('/blog/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "所有字段都必须填写！"
        if login_form.is_valid():                          # 使用表单类自带的is_valid()方法一步完成数据验证工作
            username = login_form.cleaned_data['username']     # 从表单对象的cleaned_data数据字典中获取表单的具体值
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True          # 往session字典内写入用户状态和数据
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/blog/index')
                else:
                    message = "密码错误！"
            except:
                message = "用户不存在！"
        """
        locals()函数，它返回当前所有的本地变量字典，
        我们可以偷懒的将这作为render函数的数据字典参数值，
        就不用费劲去构造一个形如{'message':message, 'login_form':login_form}的字典了
        """
        return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index')
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():                             #is_valide()验证数据 ,获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "两次密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:                                     # 用户名唯一
                    message = "用户已存在，请重输其他用户名！"
                    return render(request, 'register.html', locals())
                same_name_user = models.User.objects.filter(email=email)
                if same_name_user:          # 邮箱地址唯一
                    message = "邮箱地址已注册，请使用其他邮箱！"
                    return render(request, 'register.html', locals())

                # 如果一切正常，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login')
    register_form = RegisterForm()
    return render(request, 'register.html', locals())

    return render(request, 'register.html')


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index')
    request.session.flush()                 # 删除当前的会话数据和会话cookie,在用户退出后，删除会话
    '''
    或者用：
    del request.session['is_login']
    '''
    return redirect('/index')

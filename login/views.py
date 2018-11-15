from django.shortcuts import render,redirect
from login import models
from login import forms
# Create your views here.

def index(request):
	pass
	return render(request, 'login/index.html')

def login(request):
	#不允许重复登陆，直接到index页面
	if request.session.get('is_login', None):
		return redirect("/index/")
	if request.method == "POST":
		login_form = forms.UserForm(request.POST)
		message = "请检查填写的内容!"
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			try:
				user = models.User.objects.get(name=username)
				if user.password == password:
					request.session['is_login'] = True
					request.session['user_id'] = user.id
					request.session['user_name'] = user.name
			
					return redirect('/index/')
				else:
					message = "密码不正确!"	
			except:
				message = "用户不存在!"
		return render(request, 'login/login.html', locals())
	
	login_form = forms.UserForm()
	return render(request, 'login/login.html', locals())

def register(request):
	if request.session.get('is_login', None):
		#登陆状态不允许注册
		return redirect("/index/")
	if request.method == "POST":
		register_form = forms.RegisterForm(request.POST)
		print(request.POST)
		message = "请检查填写的内容！"
		if register_form.is_valid():
			username = register_form.cleaned_data['username']
			password1 = register_form.cleaned_data['password1']
			password2 = register_form.cleaned_data['password2']
			email = register_form.cleaned_data['email']
			sex = register_form.cleaned_data['sex']
			if password1 != password2:
				message = "两次输入的密码不相同!"
				return render(request, 'login/register.html', locals())
			else:
				same_name_user = models.User.objects.filter(name=username)
				if same_name_user:
					message = '用户名已存在，请重新输入用户名!'
					return render(request, 'login/register.html', locals())
				same_email_user = models.User.objects.filter(email=email)
				if same_email_user:
					message = '该邮箱已被注册，请重新输入邮箱!'
					return render(request, 'login/register.html', locals())
				#条件满足创建用户
				new_user = models.User()
				new_user.name = username
				new_user.password = password1
				new_user.email = email
				new_user.sex = sex
				new_user.save()	
				return redirect('/login/')
	register_form = forms.RegisterForm()
	return render(request, 'login/register.html', locals())

def logout(request):
	if not request.session.get('is_login', None):
		#如果本来就未登陆，也就没有登陆一说
		return redirect("/index/")
	request.session.flush()
	#或者使用下面的方法
	# del request.session['is_login']
	# del request.session['user_id']
	# del request.session['user_name']
	return redirect("/index/")


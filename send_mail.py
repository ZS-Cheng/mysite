import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
if __name__ == '__main__':
	subject, from_email, to = '来自127.0.0.1的测试邮件', '2934137033@qq.com', 'zhangshuncheng@soundai.com'
	text_content = '欢迎访问127.0.0.1，这是ldap站点'
	html_content = '<p>欢迎访问<a href="http://127.0.0.1:8000" target=blank</a>,这里是ldap站点!</p>'
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()

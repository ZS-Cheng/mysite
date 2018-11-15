from django.http import HttpResponse

import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>"
def hello(request):
	return HttpResponse("Hello world")

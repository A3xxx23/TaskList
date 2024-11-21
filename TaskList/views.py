from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def home(request):
    return HttpResponse('<h1>Angel Aquino</h1>')

def calendarTemplate(request):
    template = loader.get_template('calendar.html')
    return HttpResponse(template.render())
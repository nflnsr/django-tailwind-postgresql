from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist

# Create your views here.
def index(request):
    no = 1
    lists = Todolist.objects.all()
    return render(request, '../templates/projects/index.html', {'lists': lists, 'no': no})
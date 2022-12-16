from django.shortcuts import render
from django.http import HttpResponse
from .models import Todolist
from datetime import date

# Create your views here.
def index(request):
    lists = Todolist.objects.all()
    # create function to get date now
    today = date.today()

    return render(request, '../templates/projects/index.html', {'lists': lists, 'today': today})
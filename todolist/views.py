from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Todolist
from datetime import date
from .forms import TodolistForm 

# Create your views here.
def index(request):
    lists = Todolist.objects.all()
    context = {}

    today = date.today()
    form = TodolistForm()
    if request.method == 'POST':
        form = TodolistForm(request.POST)
        if form.is_valid():
            form.save()
            print('form data: ', request.POST)
            return redirect('index')

    context['lists'] = lists
    context['today'] = today
    return render(request, '../templates/projects/index.html', context)

def edit(request, id):
    todo = Todolist.objects.get(id=id)
    form = TodolistForm(instance=todo)
    priority = form['priority'].value()
    task = form['task'].value()
    date_created = date.today()
    if request.method == 'POST':
        form = TodolistForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form, 'task': task, 'priority': priority, 'date_created': date_created}
    return render(request, '../templates/projects/update.html', context) 

def delete(request, id):
    todo = Todolist.objects.get(id=id)
    form = TodolistForm(instance=todo)
    task = form['task'].value()
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    context = {'todo': todo, 'task': task}
    return render(request, '../templates/projects/delete.html', context)



# def add(request):
#     if request.method == 'POST':
#         form = TodolistForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = TodolistForm()
#         return render(request, '../templates/projects/create.html', {'form': form})





# def edit(request, id):
#     list = Todolist.objects.get(id=id)
#     if request.method == 'POST':
#         form = TodolistForm(request.POST, instance=list)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = TodolistForm(instance=list)
#         return render(request, '../templates/projects/edit.html', {'list': list, 'form': form})
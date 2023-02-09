from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Todolist
from datetime import date
from .forms import TodolistForm
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
# import superclass
from django.db import transaction, DatabaseError

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Create account successful.')
            return redirect('index')
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
            return redirect('register')
    context = {'form': form}
    return render(request, '../templates/projects/register.html', context)


class Login(LoginView):
    template_name = '../templates/projects/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


def index(request):
    try:
        user = request.user
        lists = Todolist.objects.all().filter(user=user.id)
        username = str(user)
        today = date.today()
        form = TodolistForm()
        if request.method == 'POST':
            form = TodolistForm(request.POST)
            # submit user id
            print('user id: ', user.id)
            if form.is_valid():
                form.save()
                print('form data: ', request.POST)
                return redirect('index')

        context = {'lists': lists, 'form': form, 'today': today, 'user': user, 'username': username.capitalize()}
        print(user.id)
        return render(request, '../templates/projects/index.html', context)
    except OperationalError:
        return HttpResponse('Database is not connected.')
    return HttpResponse('Database is not connected.')

    # @login_required
    # def display_user_data(request):
    #     user = request.user
    #     data = retrieve_user_data(user)
    #     return render(request, 'user_data.html', {'data': data})

def edit(request, id):
    user = request.user.id
    print('user id: ', user)
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

    context = {'form': form, 'task': task,
               'priority': priority, 'date_created': date_created}
    return render(request, '../templates/projects/update.html', context)


def delete(request, id):
    todo = Todolist.objects.get(id=id)
    form = TodolistForm(instance=todo)
    task = form['task'].value()
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    context = {'todo': todo, 'task': task}
    return render(request, '../templates/projects/index.html', context)


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

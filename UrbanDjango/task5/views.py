# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import ContentForm


# Create your views here.


def sign_up_by_html(request):
    info = {'error': []}
    i = 0
    users = ['Boris', 'Grisha', 'Nastiy', 'Nataliy']
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username not in users and password == repeat_password and int(age) >= 18:
            users.append(username)
            return HttpResponse(f'Приветствуем {username}')
        elif username in users:
            i += 1
            info[f'error {i}'] = (
                HttpResponse('Change your username',
                             status=400, reason='the username is used'))
            return HttpResponse('Change your username',
                                status=400, reason='the username is used')
        elif password != repeat_password:
            i += 1
            info[f'error {i}'] = (
                HttpResponse("passwords don't match",
                             status=400, reason='re-enter the passwords'))
            return HttpResponse("passwords don't match",
                                status=400, reason='re-enter the passwords')
        elif int(age) < 18:
            i += 1
            info[f'error {i}'] = (
                HttpResponse('You must be over 18',
                             status=400, reason='registration from the age of 18'))
            return HttpResponse('You must be over 18',
                                status=400, reason='registration from the age of 18')
    context = {'info': info}
    return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    info = {'error': []}
    i = 0
    users = ['Boris', 'Grisha', 'Nastiy', 'Nataliy']
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username not in users and password == repeat_password and int(age) >= 18:
                users.append(username)
                return HttpResponse(f'Приветствуем {username}')

            elif username in users:
                i += 1
                info[f'error {i}'] = HttpResponse(
                    'Этот логин уже занят', status=400, reason='repeated login')
                return HttpResponse('Этот логин уже занят',
                                    status=400, reason='repeated login')

            elif password != repeat_password:
                i += 1
                info[f'error {i}'] = HttpResponse(
                    'Этот логин уже занят', status=400, reason='repeated login')
                return HttpResponse('Пароли не совпадают',
                                    status=400, reason='non-identical passwords')

            elif int(age) < 18:
                i += 1
                info[f'error {i}'] = HttpResponse(
                    f'Регистрация разрешена с 18ти лет', status=400,
                    reason='insufficient age')

                return HttpResponse(
                    f'Регистрация разрешена с 18ти лет', status=400,
                    reason='insufficient age')
    else:

        form = ContentForm()
        context = {'info': info, 'form': form}
        return render(request, 'registration_page.html', context)

from django.shortcuts import render


# Create your views here.
def building_func(request):
    return render(request, 'third_task/building.html')


# Для записи в тэгах заголовок и списки записал через словарь.
# В соответствующих тэгах - имена переменных
def pipe_func(request):
    title = "Трубы стальные"
    list_1 = 'Масса одного погонного метра'
    list_2 = 'Перевести дюймы в метры'
    list_3 = 'Содержание легированных добавок'
    context = {'title': title, 'text_1': list_1, 'text_2': list_2, 'text_3': list_3}

    return render(request, 'third_task/pipe.html', context)


def brick_func(request):
    return render(request, 'third_task/brick.html')

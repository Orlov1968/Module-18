from django.shortcuts import render


# Create your views here.
def main_page(request):
    title = "Главная страница"
    link1 = "Главная"
    link2 = "Магазин"
    link3 = 'Корзина'
    context = {'title': title, 'link1': link1, 'link2': link2, 'link3': link3}
    return render(request, 'platform.html', context)


def store(request):
    title = 'Ассортимент'
    buy = 'Купить'
    games = ['Hexson', 'Tanks','Mario brothers',]
    back = 'Вернуться обратно'
    context = {'title': title, "buy": buy, 'games': games, 'back': back}
    return render(request, 'games.html', context)


def korzina(request):
    title = 'Корзина'
    back = 'Вернуться обратно'
    context = {'title': title, 'back': back}
    return render(request, 'cart.html', context)

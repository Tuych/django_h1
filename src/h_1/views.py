from django.shortcuts import render


def h_1_main(request):
    context = {
        'title': 'homework 1',
        'info': "Моя первая работа в Джанго",
    }
    return render(request, 'h_1/index.html', context)

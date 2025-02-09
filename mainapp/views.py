import math
from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


def info1_view(request):
    return render(request, 'info1.html')


# mainapp/views.py
def solution_view(request):
    """
    Решение задачи 1012: проверяем, выполняются ли неравенства:
    1) A < B < C
    2) A < B > C
    И выводим, какое из них выполняется, или что ни одно не выполняется.
    """
    result = None
    if request.method == 'POST':
        try:
            A = float(request.POST.get('A'))
            B = float(request.POST.get('B'))
            C = float(request.POST.get('C'))

            # Проверка неравенств
            if A < B < C:
                result = "Выполняется неравенство A < B < C"
            elif A < B > C:
                result = "Выполняется неравенство A < B > C"
            else:
                result = "Ни одно из указанных неравенств не выполняется"
        except (TypeError, ValueError):
            result = "Ошибка в введённых данных!"

    context = {
        'result': result
    }
    return render(request, 'solution.html', context)


def about_view(request):
    """
    Страница "Я и моя образовательная программа".
    Данные берём из словарей.
    """
    student_info = {
        'full_name': 'Печененко Александр Владимирович',
        'photo': 'mainapp/images/avatar.jpg',
        'email': 'avpechenenko@edu.hse.ru',
        'phone': '+7 (800) 555-35-35'
    }

    program_info = {
        'title': 'Разработка web-приложений на Python',
        'description': 'Учебная программа по освоению web-приложений на Python.',
        'manager': {
            'full_name': 'Марширов Виктор Викторович',
            'photo': 'mainapp/images/manager.jpg',
            'email': 'vmarshirov@hse.ru'
        },
        'leader': {
            'full_name': 'Марширов Виктор Викторович',
            'photo': 'mainapp/images/leader.jpg',
            'email': 'vmarshirov@hse.ru'
        }
    }

    classmates = [
        {
            'full_name': 'Панькин Владислав Сергеевич',
            'photo': 'mainapp/images/student1.jpg',
            'email': 'student1@example.com',
            'phone': '+7 (900) 123-45-11'
        },
        {
            'full_name': 'Новацкий Иван Дмитриевич',
            'photo': 'mainapp/images/student2.jpg',
            'email': 'idnovatskiy@edu.hse.ru',
            'phone': '+7 (900) 123-45-22'
        },
    ]

    context = {
        'student': student_info,
        'program': program_info,
        'classmates': classmates,
    }
    return render(request, 'about.html', context)

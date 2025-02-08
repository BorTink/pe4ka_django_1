import math
from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


def info1_view(request):
    return render(request, 'info1.html')


def solution_view(request):
    """
    Решение задачи 1004: Можно ли в квадратном зале площадью S
    поместить круглую сцену радиусом R так, чтобы от стены
    до сцены был проход не менее K?

    Формула проверки: 2R + 2K <= sqrt(S)
    """
    result = None
    if request.method == 'POST':
        try:
            S = float(request.POST.get('S'))
            R = float(request.POST.get('R'))
            K = float(request.POST.get('K'))
            side = math.sqrt(S)

            if 2 * R + 2 * K <= side:
                result = "Можно: сцена помещается с нужными проходами."
            else:
                result = "Нельзя: сцена слишком велика или проходы слишком широкие."
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
        'full_name': 'Иванов Иван Иванович',
        'photo': 'img/avatar.jpg',
        'email': 'ivanov@example.com',
        'phone': '+7 (900) 123-45-67'
    }

    program_info = {
        'title': 'Разработка web-приложений на Python',
        'description': 'Учебная программа по освоению Django, Flask и других web-технологий на Python.',
        'manager': {
            'full_name': 'Петров Пётр Петрович',
            'photo': 'img/manager.jpg',
            'email': 'petrov@example.com'
        },
        'leader': {
            'full_name': 'Сидоров Сидор Сидорович',
            'photo': 'img/leader.jpg',
            'email': 'sidorov@example.com'
        }
    }

    classmates = [
        {
            'full_name': 'Сокурсник 1',
            'photo': 'img/student1.jpg',
            'email': 'student1@example.com',
            'phone': '+7 (900) 123-45-11'
        },
        {
            'full_name': 'Сокурсник 2',
            'photo': 'img/student2.jpg',
            'email': 'student2@example.com',
            'phone': '+7 (900) 123-45-22'
        },
    ]

    context = {
        'student': student_info,
        'program': program_info,
        'classmates': classmates,
    }
    return render(request, 'about.html', context)

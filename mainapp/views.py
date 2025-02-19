import math
from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


def info1_view(request):
    return render(request, 'info1.html')


def solution_view(request):
    """
    Решение задачи:
    На первой строке ввода: записи о переработках, вида "<имя>,<день>,<часы>"
    разделённые символом "|".
    На второй строке: день недели, по которому нужно подсчитать количество записей.

    Вывести целое число — количество записей для заданного дня.
    """
    result = None  # Результат (количество записей)
    if request.method == 'POST':
        # Пытаемся получить данные из формы
        records_line = request.POST.get('records')
        day_input = request.POST.get('day')

        if records_line and day_input:
            # Разделяем строку по символу '|'
            records_list = records_line.split('|')

            # Переменная-счётчик для подходящих записей
            count = 0

            # Обрабатываем каждую запись
            for record in records_list:
                # Каждая запись: "Имя,деньНедели,часы"
                parts = record.split(',')
                # Проверяем, что частей три
                if len(parts) == 3:
                    name = parts[0].strip()
                    day_of_record = parts[1].strip()
                    hours = parts[2].strip()  # не обязательно нужно конвертировать в int для подсчёта факта "записи"

                    # Если день совпадает, увеличиваем счётчик
                    if day_of_record.lower() == day_input.lower():
                        count += 1
                else:
                    # Если формат записи неверный, можно либо игнорировать, либо сообщать об ошибке
                    pass

            result = f"Количество записей: {count}"
        else:
            result = "Пожалуйста, заполните обе строки ввода."

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

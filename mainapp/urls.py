from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),                   # Главная
    path('info1/', views.info1_view, name='info1'),           # Информационная страница
    path('solution/', views.solution_view, name='solution'),  # Алгоритмическая задача
    path('about/', views.about_view, name='about'),           # Страница "Я и моя образовательная программа"
]

# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1100, 600)
#

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


# Рисуем треугольник
def triangle(point):
    for angle_0 in range(10, 251, 120):
        v = sd.get_vector(start_point=point, angle=angle_0, length=100, width=2)
        v.draw()
        point = v.end_point


triangle(point=sd.get_point(100, 100))


# Рисуем квадрат
def square(point):
    for angle_1 in range(15, 286, 90):
        v = sd.get_vector(start_point=point, angle=angle_1, length=100, width=2)
        v.draw()
        point = v.end_point


square(point=sd.get_point(800, 100))


# Рисуем пятиугольник
def pentagon(point):
    for angle_2 in range(10, 299, 72):
        v = sd.get_vector(start_point=point, angle=angle_2, length=100, width=2)
        v.draw()
        point = v.end_point


pentagon(point=sd.get_point(100, 400))


# Рисуем шестиугольник
def hexagon(point):
    for angle_3 in range(10, 361, 60):
        v = sd.get_vector(start_point=point, angle=angle_3, length=100, width=2)
        v.draw()
        point = v.end_point


hexagon(point=sd.get_point(800, 400))


# Вторая часть
def figures(point, angle, length, number_parties):
    """Общая функция рисования фигур"""
    angle_changes = 360 / number_parties
    start_point = point

    for i in range(number_parties):
        angle += angle_changes

        v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)
        v.draw()

        start_point = v.end_point
    sd.line(start_point=point, end_point=start_point, width=3)


def triangle(point, angle, length):
    """ Эта функция рисует треугольник"""

    figures(point=point, angle=angle, length=length, number_parties=3)


triangle(point=sd.get_point(150, 150), angle=0, length=100)


def square(point, angle, length):
    """ Эта функция рисует квадрат"""

    figures(point=point, angle=angle, length=length, number_parties=4)


square(point=sd.get_point(400, 150), angle=0, length=100)


def pentagon(point, angle, length):
    """ Эта функция рисует пятиугольник"""

    figures(point=point, angle=angle, length=length, number_parties=5)


pentagon(point=sd.get_point(150, 400), angle=0, length=100)


def hexagon(point, angle, length):
    """ Эта функция рисует шестиугольник"""

    figures(point=point, angle=angle, length=length, number_parties=6)


hexagon(point=sd.get_point(400, 400), angle=0, length=100)

# # Неоптимальная версия второй части
# def triangle(point, angle_0):
#     v1 = sd.get_vector(start_point=point, angle=angle_0, length=100, width=3)
#     v1.draw()
#     # Объявляем глобальные переменные конечной точки вектора для каждой фигуры
#     global point_0
#     point_0 = v1.end_point
#     global point_1
#     point_1 = v1.end_point
#     global point_2
#     point_2 = v1.end_point
#     global point_3
#     point_3 = v1.end_point
#
#
# point_0 = sd.get_point(250, 150)  # Рисуем треугольник
# angle = 10
# for i in range(3):
#     angle += 120
#     sd.sleep(0.2)
#
#     triangle(point=point_0, angle_0=angle)
#
# point_1 = sd.get_point(800, 150)  # Рисуем квадрат
# angle = 10
# for i in range(4):
#     angle += 90
#     sd.sleep(0.2)
#
#     triangle(point=point_1, angle_0=angle)
#
# point_2 = sd.get_point(800, 400)  # Рисуем шестиугольник
# angle = 10
# for i in range(6):
#     angle += 60
#     sd.sleep(0.2)
#     triangle(point=point_2, angle_0=angle)
#
# point_3 = sd.get_point(250, 400)  # Рисуем пятиугольник
# angle = 10
# for i in range(5):
#     angle += 72
#     sd.sleep(0.2)
#
#     triangle(point=point_3, angle_0=angle)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()

# Зачёт!

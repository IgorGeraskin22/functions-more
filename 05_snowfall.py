# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 700)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок (x, y)
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


# n = 20  # количество снежинок
# x_list = []  # создаем пустой список координаты х
# y_list = []  # создаем пустой список координаты у
#
# for _ in range(n):
#     x_point = random.randrange(50, 950, 100)  # создаем рандомные координаты x с шагом
#     y_points = sd.random_number(600, 700)  # создаем рандомные координаты y
#     x_list.append(x_point)  # запись координат х в список
#     y_list.append(y_points)  # запись координат у в список
#
#
# def snow(center, length, color):
#     """Функция рисования снежинки"""
#     sd.snowflake(center, length, color)
#
#
#
# while True:
#     # sd.clear_screen()
#     for i in range(n):
#         point = sd.get_point(x_list[i], y_list[i])  # задаем координаты
#         snow(center=point, length=30, color=sd.background_color)  # вызываем ф-цию рисования снежинки
#         y_list[i] -= 30
#         if y_list[i] < 30:
#             break
#
#         point1 = sd.get_point(x_list[i], y_list[i])
#         snow(center=point1, length=30, color=sd.COLOR_WHITE)  # вызываем ф-цию рисования снежинки
#
#         sd.sleep(0.05)
#     if sd.user_want_exit():
#         break
# sd.pause()

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге. То есть ветер то справо то слева
# - сделать сугроб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
n = 30
x_list = []
y_list = []
length_list = []


def list_entry():
    """Функция записи в списки"""
    for _ in range(n):
        x_point_0 = sd.random_number(0, 1200)
        y_point_0 = sd.random_number(500, 1200)
        length_random_0 = sd.random_number(10, 30)
        x_list.append(x_point_0)
        y_list.append(y_point_0)
        length_list.append(length_random_0)


def snow(center, length, color):
    """Функция рисование снежинки"""
    sd.snowflake(center, length, color)


while True:
    """Бесконечный цикл отрисовки снежинок"""
    sd.start_drawing()
    list_entry()
    for i in range(n):
        point = sd.get_point(x_list[i], y_list[i])
        snow(center=point, length=length_list[i], color=sd.background_color)

        if y_list[i] < 30:  # если выполняется условие,то:
            y_list[i] = sd.random_number(500, 1200)  # переопределяем значения координат(начинаем
            # сново рисоват сверху).
            snow(center=point, length=length_list[i], color=sd.COLOR_WHITE)  # рисуем снежинку.
            list_entry()  # функция записи значений в списки.

        y_list[i] -= 10
        x_list[i] -= sd.random_number(-15, 15)  # качание снежинки.

        point_2 = sd.get_point(x_list[i], y_list[i])
        snow(center=point_2, length=length_list[i], color=sd.COLOR_WHITE)
    sd.finish_drawing()
    sd.sleep(0.1)

    if sd.user_want_exit():
        break

sd.pause()

# Зачёт!

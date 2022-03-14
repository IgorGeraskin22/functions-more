# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1100, 600)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

def branch(point, angle, length, delta_0):
    if length < 10:  # Условие по требованию преподователя
        # if length < 2: # При таком условии рисуется дерево как в примере задания.
        return
    v = sd.get_vector(start_point=point, angle=angle, length=length)
    v.draw(color=sd.COLOR_GREEN)
    next_point = v.end_point
    next_angle = angle - delta_0
    next_length = length * .75
    branch(point=next_point, angle=next_angle, length=next_length, delta_0=delta_0)
    next_angle = angle + delta_0
    branch(point=next_point, angle=next_angle, length=next_length, delta_0=delta_0)


branch(point=sd.get_point(300, 30), angle=90, length=100, delta_0=30)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

# В данной функции задача решена с помощью модулей random.uniform и random.randint.
# Применить sd.random_number() не получилось - возвращает None. Пока не знаю как применить правильно этот модуль.
def branch(point, angle, length, delta_0):
    if length < 3:
        return
    v = sd.get_vector(start_point=point, angle=angle, length=length)
    v.draw(color=sd.COLOR_GREEN)
    next_point = v.end_point

    lower_limit_length = 0.75 - (0.75 * 20 / 100)  # 20% от коэффициента 0.75 - нижний предел диапазона.
    upper_limit_length = 0.75 + (0.75 * 20 / 100)  # 20% от коэффициента 0.75 - верхний предел диапазона.
    random_length = random.uniform(lower_limit_length, upper_limit_length)  # случайнай коэффициент между верхним и
    # нижним пределом диапазона.
    next_length = length * random_length  # рандомная длина веточки.

    lower_limit_angle = delta_0 - (delta_0 * 40 / 100)  # 40% от 30- ти градусов - нижний предел диапазона.
    upper_limit_angle = delta_0 + (delta_0 * 40 / 100)  # 40% от 30- ти градусов - верхний предел диапазона.
    random_angle = random.randint(lower_limit_angle, upper_limit_angle)  # случайный градус между верхним и
    # нижним пределом диапазона.
    next_angle = angle - random_angle  # случайное отклонение  угла от 30 - ти градусов.

    branch(point=next_point, angle=next_angle, length=next_length, delta_0=delta_0)

    random_length = random.uniform(lower_limit_length, upper_limit_length)  #
    next_length = length * random_length  # Можно и без использование этих выражений, но с ними больше хауса)

    next_angle = angle + random_angle
    branch(point=next_point, angle=next_angle, length=next_length, delta_0=delta_0)


branch(point=sd.get_point(450, 30), angle=90, length=100, delta_0=30)
sd.pause()

# Зачёт!

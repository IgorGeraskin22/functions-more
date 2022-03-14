# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def figures(point, angle, length, number_parties):
    """Общая функция рисования фигур"""

    angle_changes = 360 / number_parties
    start_point = point

    for i in range(number_parties):
        angle += angle_changes

        v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)

        v.draw(color=color_dict[enter_color]['color'])

        start_point = v.end_point
    sd.line(start_point=point, end_point=start_point, width=3, color=color_dict[enter_color]['color'])


# Пожалуйста, покажите как должен выглядеть правильный код.
# В дальнейшем уже буду знать как правильно структуировать
def triangle(point, angle, length):
    """ Эта функция рисует треугольник"""

    figures(point=point, angle=angle, length=length, number_parties=3)


def square(point, angle, length):
    """ Эта функция рисует квадрат"""

    figures(point=point, angle=angle, length=length, number_parties=4)


def pentagon(point, angle, length):
    """ Эта функция рисует пятиугольник"""

    figures(point=point, angle=angle, length=length, number_parties=5)


def hexagon(point, angle, length):
    """ Эта функция рисует шестиугольник"""

    figures(point=point, angle=angle, length=length, number_parties=6)


color_dict = {
    '0': {'name': 'красный', 'color': sd.COLOR_RED},
    '1': {'name': 'оранжевый', 'color': sd.COLOR_ORANGE},
    '2': {'name': 'желтый', 'color': sd.COLOR_YELLOW},
    '3': {'name': 'зеленый', 'color': sd.COLOR_GREEN},
    '4': {'name': 'морская волна', 'color': sd.COLOR_CYAN},
    '5': {'name': 'голубой', 'color': sd.COLOR_BLUE},
    '6': {'name': 'пурпурный', 'color': sd.COLOR_PURPLE}
}
print('Возможные цвета: ')
print(
    '0 : red\n'
    '1 : orange\n'
    '2 : yellow\n'
    '3 : green\n'
    '4 : cyan\n'
    '5 : blue\n'
    '6 : purple\n'
)

while True:
    enter_color = (input('Введите желаемый цвет > '))
    if enter_color in color_dict:
        """Проверим,если ли введенный ключ в словаре"""
        break

    else:
        print('Вы ввели не корректный номер!')

        """Если ключ введен не правильно,то просим пользователя ввести заново"""

triangle(point=sd.get_point(150, 150), angle=0, length=100)
square(point=sd.get_point(400, 150), angle=0, length=100)
pentagon(point=sd.get_point(150, 400), angle=0, length=100)
hexagon(point=sd.get_point(400, 400), angle=0, length=100)

sd.pause()

# Зачёт!

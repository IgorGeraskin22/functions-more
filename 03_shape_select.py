import simple_draw as sd


def drawing_figures(point, angle, length, number_parties):
    """Общая функция рисования фигур"""

    angle_changes = 360 / number_parties
    start_point = point

    for i in range(number_parties):
        angle += angle_changes

        v = sd.get_vector(start_point=start_point, angle=angle, length=length, width=3)

        v.draw(color=sd.COLOR_ORANGE)

        start_point = v.end_point
    sd.line(start_point=point, end_point=start_point, width=3, color=sd.COLOR_ORANGE)


def triangle(point, angle, length):
    """Функция рисования треугольника"""
    drawing_figures(point=point, angle=angle, length=length, number_parties=3)


def square(point, angle, length):
    """Функция рисования квадрата"""
    drawing_figures(point=point, angle=angle, length=length, number_parties=4)


def pentagon(point, angle, length):
    """Функция рисования пятиугольника"""
    drawing_figures(point=point, angle=angle, length=length, number_parties=5)


def hexagon(point, angle, length):
    """Функция рисования шестиугольника"""
    drawing_figures(point=point, angle=angle, length=length, number_parties=6)


dict_figures = {
    '0': {'name': 'треугольник', 'figure': triangle},
    '1': {'name': 'квадрат', 'figure': square},
    '2': {'name': 'пятиугольник', 'figure': hexagon},
    '3': {'name': 'шестиугольник', 'figure': pentagon},

}

print('Возможные фигуры: ')
print(
    '0 : треугольник\n'
    '1 : квадрат\n'
    '2 : пятиугольник\n'
    '3 : шестиугольник\n'

)

while True:
    enter_figures = input('Введите желаемую фигуру > ')
    if enter_figures in dict_figures:
        break

    else:
        print('Вы ввели не корректный номер!')

figures = (dict_figures[enter_figures]['figure'])

figures(point=sd.get_point(300, 300), angle=0, length=100)
sd.pause()

# Зачёт!

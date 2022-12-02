class BoardOutError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} лежит за пределами игрового поля. Введите двузначное число, каждая цифра которого от 1 до 6, включительно."


class NonEmptyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Выбраная ячейка - {self.value} - непустая. Стрелять можно только в пустые ячейки."


class ShipLocationError(Exception):
    def __init__(self, length, front, direction):
        self.length = length
        self.front = front
        self.direction = direction

    def __str__(self):
        self.front = (self.front[0] + 1, self.front[1] + 1)
        direction_word = {
            1: 'Вправо',
            2: 'Вниз'
        }
        return f"Указанные параметры - длина ({self.length}), положение носа корабля {self.front} и направление ({direction_word[self.direction]}) не позволяют корректно разместить корабль на игровом поле."


class Dot:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    @property
    def show(self):
        return (self.row, self.col)


class Ship:
    def __init__(self, length, front, direction, life):
        self.length = length
        self.front = front
        self.direction = direction
        self.life = life

    def dots(self):
        ship_cells = []
        direction_vector = {
            1: (0, 1),
            2: (1, 0)
        }

        for i in range(self.length):
            cell = (self.front[0] + direction_vector[self.direction][0] * (i), \
                    self.front[1] + direction_vector[self.direction][1] * (i))
            ship_cells.append(cell)
        return ship_cells


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


class Board:
    POSSIBLE_CELLS = []
    for i in range(6):
        for j in range(6):
            POSSIBLE_CELLS.append((i, j))
    #     print(POSSIBLE_CELLS)

    player_shots_left = []
    for i in POSSIBLE_CELLS:
        player_shots_left.append(Dot(*i))
    #     print(len(player_shots_left))

    start_cells_conditions = [['o' for i in range(6)] for i in range(6)]

    __s = u'\u220E'  # код квадрата в системе unicode

    def __init__(self, hid, cells_conditions=start_cells_conditions, ships=[], alive_ships=7):
        self.cells_conditions = cells_conditions  # list
        self.ships = ships  # list with all ships
        self.hid = hid  # bool
        self.alive_ships = alive_ships  # int

    def add_ship(self, ship):  # ставит корабль на доску (если ставить не получается, выбрасываем исключения)
        for i in range(len(ship.dots())):
            if ship.dots()[i] in self.contoured_ships():
                raise ShipLocationError(ship.length, ship.front, ship.direction)
        self.ships.append(ship.dots())
        print(f'ships = {self.ships}')

    def contoured_ships(self):  # точки всех кораблей + их контуров

        existing_ships_dots = []
        for i in range(len(self.ships)):
            existing_ships_dots += self.ships[i]

        contoured_ships_dots = []
        for dot in range(len(existing_ships_dots)):
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    tested_dot = (existing_ships_dots[dot][0] + i, existing_ships_dots[dot][1] + j)
                    if tested_dot in self.POSSIBLE_CELLS:
                        contoured_ships_dots.append(tested_dot)
        return list(set(contoured_ships_dots))

    def show_board(self):  # выводит доску в консоль в зависимости от параметра hid.
        ships_gui = self.start_cells_conditions.copy()

        existing_ships_dots = []
        for i in range(len(self.ships)):
            existing_ships_dots += self.ships[i]

        for i in existing_ships_dots:
            ships_gui[i[0]][i[1]] = self.__s

        if not hid:
            return self.gui_print(ships_gui)

    def out(self, dot):  # для точки (объекта класса Dot) возвращает True, если точка выходит за пределы поля
        print(111)
        if dot in self.POSSIBLE_CELLS:
            return False
        else:
            return True

    def shot(self):  # делает выстрел по доске (если есть попытка выстрелить за \
        # пределы и в использованную точку, нужно выбрасывать исключения
        while True:  # Loop для получения правильного ввода от Игрока

            try:
                player_shot = int(input("В какую ячейку будем стрелять?"))
                row = player_shot // 10 - 1
                col = player_shot % 10 - 1
            except Exception:
                print('Необходимо ввести двузначное число!')
                break

            if self.out((row, col)):
                raise BoardOutError(player_shot)
            else:
                shot = Dot(row, col)

                if shot not in self.player_shots_left:
                    err = NonEmptyError(player_shot)
                    print(err)
                else:
                    existing_ships_dots = []
                    for i in range(len(self.ships)):
                        existing_ships_dots += self.ships[i]
                    if (row, col) in existing_ships_dots:
                        self.cells_conditions[row][col] = 'X'
                        self.player_shots_left.remove(Dot(row, col))
                        print(self.cells_conditions)
                    else:
                        self.cells_conditions[row][col] = 'T'
                        self.player_shots_left.remove(Dot(row, col))
                        print(self.cells_conditions)
                    print('Ход компьютера:')
                    break

    def gui_print(self, L):
        print(*[" ", *[i for i in range(1, 7)]], sep=' | ')
        for i in range(6):
            print(i + 1, *L[i], sep=' | ')
        return
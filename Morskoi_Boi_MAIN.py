class Dot:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    @property
    def show(self):
        return (self.row, self.col)


class Board:
    POSSIBLE_CELLS = []
    for i in range(6):
        for j in range(6):
            POSSIBLE_CELLS.append((i, j))
    print(POSSIBLE_CELLS)

    def __init__(self, cells_conditions, ships, hid, alive_ships):
        self.cells_conditions = cells_conditions  # list
        self.ships = ships  # list
        self.hid = hid  # bool
        self.alive_ships = alive_ships  # int

    #     def add_ship(self):      #ставит корабль на доску (если ставить не получается, выбрасываем исключения)
    #         pass

    #     def contour(self):      #обводит корабль по контуру
    #         pass

    def show_board(self):  # выводит доску в консоль в зависимости от параметра hid.
        if not hid:
            return self.ships

    def out(self, dot):  # для точки (объекта класса Dot) возвращает True, если точка выходит за пределы поля
        if dot in self.POSSIBLE_CELLS:
            return False
        else:
            True

    def shot(self):  # делает выстрел по доске (если есть попытка выстрелить за \
        # пределы и в использованную точку, нужно выбрасывать исключения
        while True:  # Loop для получения правильного ввода от Игрока
            try:
                player_shot = int(input("В какую ячейку будем стрелять?"))
                row = player_shot // 10
                col = player_shot % 10
                print(row - 1, col - 1)
                print(self.POSSIBLE_CELLS)

                if self.out((row - 1, col - 1)):
                    err = BoardOutError(player_shot)
                    print(err)
                else:
                    player_shots_left = [Dot(1, 1), Dot(2, 2)]
                    shot = Dot(row, col)

                    if shot not in player_shots_left:
                        err = NonEmptyError(player_shot)
                        print(err)
                    else:
                        grid[row - 1][col - 1] = 'X'
                        print_grid(grid)
                        print('Ход компьютера:')
                        break

            except Exception:
                print('Необходимо ввести двузначное число!')


player = 'Player'
hid = True if player == 'AI' else False
AI_board = Board(1, 2, hid, 4)
# print(AI_board.show_board())
# print(len(AI_board.POSSIBLE_CELLS))
AI_board.shot()
